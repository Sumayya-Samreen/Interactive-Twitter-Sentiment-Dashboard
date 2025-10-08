import time

MAX_TWEETS = 50
MAX_RETRIES = 3

def start_search(client, query):
    for attempt in range(MAX_RETRIES):
        try:
            print(f"Searching tweets for '{query}' (attempt {attempt + 1})...")
            result = client.search_recent_tweets(
                query=query,
                max_results=MAX_TWEETS
            )
            return result
        except Exception as e:
            if "429" in str(e):
                print("Rate limit hit. Waiting for 15 minutes...")
                time.sleep(15 * 60)  # wait 15 minutes
            else:
                print(f"Error: {e}")
            if attempt < MAX_RETRIES - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print(f"Max retries reached for '{query}'. Skipping search.")
                return None
