import os
import time
import json
from twitter_search import start_search
from preprocess import clean_tweet
from sentiment import analyze_sentiment
from summarizer import auto_summarize
from visualize import plot_sentiment
from advanced_features import save_to_csv
from dashboard import generate_dashboard
from config import BEARER_TOKEN, TRACK_KEYWORDS, MAX_TWEETS, USE_MOCK_DATA
import tweepy

def create_twitter_client(bearer_token):
    return tweepy.Client(bearer_token=bearer_token)

def load_mock_tweets():
    with open("mock_tweets.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("Device set to use CPU")
    print("Starting Twitter Sentiment Analysis...\n")

    os.makedirs("outputs", exist_ok=True)

    all_results = {}
    summaries = {}

    if USE_MOCK_DATA:
        print("[INFO] Using mock data instead of real Twitter API")
        mock_data = load_mock_tweets()
        for keyword in TRACK_KEYWORDS:
            if keyword in mock_data:
                tweets = [clean_tweet(tweet["text"]) for tweet in mock_data[keyword]]
                sentiments = [analyze_sentiment(tweet) for tweet in tweets]

                all_results[keyword] = sentiments

                print(f"Summarizing {len(tweets)} mock tweets for '{keyword}'...")
                summary = auto_summarize(" ".join(tweets))
                summaries[keyword] = summary
                print(f"Summary for '{keyword}': {summary}\n")

                plot_sentiment(sentiments, keyword)
                save_to_csv(os.path.join("outputs", f"{keyword}_tweets.csv"))
                with open(os.path.join("outputs", f"{keyword}_summary.txt"), "w", encoding="utf-8") as f:
                    f.write(summary)
            else:
                print(f"No mock data for '{keyword}'")
    else:
        client = create_twitter_client(BEARER_TOKEN)
        for keyword in TRACK_KEYWORDS:
            print(f"Searching tweets for '{keyword}'...")
            results = start_search(client, keyword)

            if not results or not results.data:
                print(f"No results for '{keyword}'\n")
                continue

            tweets = [clean_tweet(tweet.text) for tweet in results.data]
            sentiments = [analyze_sentiment(tweet) for tweet in tweets]

            all_results[keyword] = sentiments

            print(f"Summarizing {len(tweets)} tweets for '{keyword}'...")
            summary = auto_summarize(" ".join(tweets))
            summaries[keyword] = summary
            print(f"Summary for '{keyword}': {summary}\n")

            plot_sentiment(sentiments, keyword)
            save_to_csv(os.path.join("outputs", f"{keyword}_tweets.csv"))
            with open(os.path.join("outputs", f"{keyword}_summary.txt"), "w", encoding="utf-8") as f:
                f.write(summary)

    # Generate the HTML dashboard
    generate_dashboard(all_results, summaries)

    print("Twitter Sentiment Analysis Completed.")

if __name__ == "__main__":
    main()
