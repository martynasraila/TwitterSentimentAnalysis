import tweepy
from textblob import TextBlob

consumer_key = 'HaMv68UGjwFEN61u1qhDmvKeo'
consumer_secret = '7JML6o0DMXWIMo0QPEepwsKGiUWiTYbctViKC9QDevTo1gkyQw'

access_token = '904635514342518784-o2nx60pW3RHJuRhIqQI35v47ce8GYDA'
access_token_secret = '03QTsn7jBHeWXSjfMWZtlaB4FS6oalnG1OXZqqIxjGXq6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)