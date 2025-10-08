import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"@\S+", "", tweet)
    tweet = re.sub(r"#\S+", "", tweet)
    tweet = re.sub(r"\s+", " ", tweet)
    tweet = tweet.translate(str.maketrans("", "", string.punctuation))
    tweet = tweet.lower()
    tweet = " ".join([word for word in tweet.split() if word not in stopwords.words('english')])
    return tweet
