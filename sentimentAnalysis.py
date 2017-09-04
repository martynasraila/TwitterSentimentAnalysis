import sys
import tweepy
from textblob import TextBlob
import csv


#makes a csv file with tweets and their sentiments as two columns
def make_csv(public_tweets):
    with open("tweetAnalysis.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for tweet in public_tweets:
            writer.writerow([tweet.text])
            analysis = TextBlob(tweet.text)
            writer.writerow([analysis.sentiment])

consumer_key = 'HaMv68UGjwFEN61u1qhDmvKeo'
consumer_secret = '7JML6o0DMXWIMo0QPEepwsKGiUWiTYbctViKC9QDevTo1gkyQw'

access_token = '904635514342518784-o2nx60pW3RHJuRhIqQI35v47ce8GYDA'
access_token_secret = '03QTsn7jBHeWXSjfMWZtlaB4FS6oalnG1OXZqqIxjGXq6'
print ('Authenticating...')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

try:
    api = tweepy.API(auth)
    test_tweets = api.search('Test')
    print("Authenticated succesfully")
except tweepy.error.TweepError as e:
        print ('Couldnt Authenticate, Check APIKEYS')
        sys.exit(1)
print('Enter the topic for sentiment analysis: ')
tweet_name = input()
public_tweets = api.search(tweet_name)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

make_csv(public_tweets)