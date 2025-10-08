import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import smtplib
from email.mime.text import MIMEText
# from config import EMAIL_SETTINGS

tweet_data = []

def log_tweet(tweet, sentiment):
    tweet_data.append({"tweet": tweet, "sentiment": sentiment})

def save_to_csv(filename="tweets_log.csv"):
    pd.DataFrame(tweet_data).to_csv(filename, index=False)
    print(f"[INFO] Tweets saved to {filename}")

def plot_hashtag_frequency(tweets):
    hashtags = [tag.lower() for tweet in tweets for tag in tweet.split() if tag.startswith("#")]
    freq = Counter(hashtags)
    plt.figure(figsize=(10, 5))
    plt.bar(freq.keys(), freq.values())
    plt.title("Hashtag Frequency")
    plt.xticks(rotation=45)
    plt.show()

def generate_wordcloud(tweets):
    text = " ".join(tweets)
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SETTINGS["sender"]
    msg["To"] = EMAIL_SETTINGS["receiver"]

    with smtplib.SMTP(EMAIL_SETTINGS["smtp_server"], EMAIL_SETTINGS["smtp_port"]) as server:
        server.starttls()
        server.login(EMAIL_SETTINGS["sender"], EMAIL_SETTINGS["password"])
        server.send_message(msg)

def check_sentiment_alert(sentiments):
    if len(sentiments) < 10:
        return
    avg_sentiment = sum(sentiments[-10:]) / 10
    if avg_sentiment < -0.5 or avg_sentiment > 0.5:
        send_email("Sentiment Alert", f"Recent average sentiment: {avg_sentiment:.2f}")
