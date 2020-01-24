#dick
import textblob

def detect_polarity(text):
    return textblob.TextBlob(text).sentiment.polarity