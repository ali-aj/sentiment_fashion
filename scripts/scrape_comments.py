import tweepy
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

def setup_twitter_api():
    """Setup Twitter API v2 authentication"""
    client = tweepy.Client(
        bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
        wait_on_rate_limit=True
    )
    return client

def scrape_twitter(brands, max_tweets=1000):
    """Scrape tweets from brand accounts"""
    client = setup_twitter_api()
    all_tweets = []
    
    for brand in brands:
        try:
            # Get user ID first
            user = client.get_user(username=brand)
            if not user.data:
                print(f"Could not find user {brand}")
                continue
                
            user_id = user.data.id
            
            # Get tweets from user
            tweets = client.get_users_tweets(
                id=user_id,
                max_results=100,  # Max allowed per request
                tweet_fields=['created_at', 'public_metrics']
            )
            
            if not tweets.data:
                continue
                
            for tweet in tweets.data[:max_tweets]:
                all_tweets.append({
                    'brand': brand,
                    'date': tweet.created_at,
                    'content': tweet.text,
                    'platform': 'twitter',
                    'likes': tweet.public_metrics['like_count'],
                    'retweets': tweet.public_metrics['retweet_count']
                })
                
            print(f"Collected {len(all_tweets)} tweets from {brand}")
            time.sleep(2)  # Rate limiting
            
        except Exception as e:
            print(f"Error collecting tweets for {brand}: {str(e)}")
            continue
            
    return pd.DataFrame(all_tweets)

def scrape_mentions(brands, max_tweets=1000):
    """Scrape mentions of brands"""
    client = setup_twitter_api()
    all_mentions = []
    
    for brand in brands:
        try:
            # Search for mentions
            query = f"{brand} lang:en -is:retweet"
            tweets = client.search_recent_tweets(
                query=query,
                max_results=100,
                tweet_fields=['created_at', 'public_metrics']
            )
            
            if not tweets.data:
                continue
                
            for tweet in tweets.data[:max_tweets]:
                all_mentions.append({
                    'brand': brand,
                    'date': tweet.created_at,
                    'content': tweet.text,
                    'platform': 'twitter',
                    'likes': tweet.public_metrics['like_count'],
                    'retweets': tweet.public_metrics['retweet_count']
                })
                
            print(f"Collected {len(all_mentions)} mentions for {brand}")
            time.sleep(2)  # Rate limiting
            
        except Exception as e:
            print(f"Error collecting mentions for {brand}: {str(e)}")
            continue
            
    return pd.DataFrame(all_mentions)

def ensure_data_dirs():
    """Create necessary data directories if they don't exist"""
    os.makedirs('data/raw', exist_ok=True)

def main():
    # Ensure we have our data directories
    ensure_data_dirs()
    
    brands = ["Khaadi", "GulAhmedPK", "sapphirepak", "AlKaram", "Bareeze", "SanaSafinaz"]
    max_tweets = 1000
    
    try:
        # Get both brand posts and mentions
        df_posts = scrape_twitter(brands, max_tweets)
        df_mentions = scrape_mentions(brands, max_tweets)
        
        # Combine and save
        df_raw = pd.concat([df_posts, df_mentions])
        df_raw['scrape_date'] = datetime.now()
        df_raw.to_csv('data/raw/comments_twitter.csv', index=False)
        print(f"\nScraped {len(df_raw)} tweets total:")
        print(df_raw['brand'].value_counts())
        
    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()