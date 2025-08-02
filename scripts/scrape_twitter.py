# scripts/scrape_twitter.py

import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets(query, max_tweets=500, since="2024-08-01", until="2025-08-01"):
    full_query = f'{query} since:{since} until:{until} lang:en'
    tweets = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(full_query).get_items()):
        if i >= max_tweets:
            break
        tweets.append([tweet.date, tweet.user.username, tweet.content])
    
    df = pd.DataFrame(tweets, columns=['date', 'user', 'text'])
    df.to_csv('data/napa_tweets.csv', index=False)
    print(f"✅ Scraped {len(df)} tweets and saved to data/napa_tweets.csv")

if __name__ == "__main__":
    scrape_tweets('"napa valley wine" OR #napawine')
