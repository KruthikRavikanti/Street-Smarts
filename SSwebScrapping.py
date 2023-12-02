import tweepy
import pandas as pd
import time

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_SECRET'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Function to scrape tweets based on a search query
def scrape_tweets(query, max_tweets):
    tweets = tweepy.Cursor(api.search, q=query, lang="en", tweet_mode='extended').items(max_tweets)
    
    data = []
    for tweet in tweets:
        try:
            text = tweet.retweeted_status.full_text if 'retweeted_status' in dir(tweet) else tweet.full_text
            data.append([
                text,
                tweet.created_at,
                tweet.user.location,
                tweet.user.followers_count,
                tweet.favorite_count,
                tweet.retweet_count
            ])
        except Exception as e:
            print("Error on tweet:", str(e))
    
    return pd.DataFrame(data, columns=['Tweet', 'Timestamp', 'Location', 'Followers', 'Likes', 'Retweets'])

# Example usage
query = "#TrafficUpdate OR #NewBusiness -filter:retweets"
max_tweets = 100

try:
    df = scrape_tweets(query, max_tweets)
    print(df.head())

    # Save the dataset
    df.to_csv('city_updates.csv', index=False)
except Exception as e:
    print("An error occurred:", str(e))
