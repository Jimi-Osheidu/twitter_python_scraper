
import pandas as pd
import tweepy
import configparser


# read configs 
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter'] ['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

# search tweets
keywords = 'world cup 2022'
limit=20000

tweets= tweepy.Cursor(api.search_tweets, q=keywords, count=300, tweet_mode='extended') .items(limit)
# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
#create DataFrame
columns= ['User', 'Tweet', 'Date']
data =[]

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text, tweet.created_at])
df =pd.DataFrame(data, columns=columns)
print(df)