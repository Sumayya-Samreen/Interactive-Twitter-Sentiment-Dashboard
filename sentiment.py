from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(tweet):
    score = analyzer.polarity_scores(tweet)
    return score['compound']
