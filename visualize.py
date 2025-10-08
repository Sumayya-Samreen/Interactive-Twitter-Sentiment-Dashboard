import matplotlib.pyplot as plt
import os

def plot_sentiment(sentiments, keyword, save_path=None):
    plt.figure(figsize=(10, 5))
    plt.plot(sentiments, marker="o")
    plt.title(f"Sentiment Analysis for {keyword}")
    plt.xlabel("Tweet number")
    plt.ylabel("Sentiment score")
    plt.grid(True)

    if not save_path:
        os.makedirs("outputs", exist_ok=True)
        save_path = os.path.join("outputs", f"{keyword}_sentiment_plot.png")

    plt.savefig(save_path)
    plt.close()
