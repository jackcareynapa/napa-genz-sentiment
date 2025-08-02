# scripts/sentiment.py

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(file_path='data/napa_tweets.csv'):
    df = pd.read_csv(file_path)
    sid = SentimentIntensityAnalyzer()

    df['sentiment_score'] = df['text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
    df['sentiment_label'] = df['sentiment_score'].apply(
        lambda x: 'positive' if x > 0.2 else 'negative' if x < -0.2 else 'neutral'
    )

    df.to_csv('data/napa_tweets_sentiment.csv', index=False)
    print(f"✅ Analyzed sentiment for {len(df)} tweets. Saved to data/napa_tweets_sentiment.csv")

if __name__ == "__main__":
    analyze_sentiment()