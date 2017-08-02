# !/usr/bin/env python

import tweepy, time, json


# enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''  # keep the quotes, replace this with your access token
ACCESS_SECRET = ''  # keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(auth)

query = "timbeta"
tweet_cursor = tweepy.Cursor(API.search, query, result_type="recent", include_entities=True, lang="es").items()

for tweet in tweet_cursor:
    tweet_id = tweet.id_str  # Id of the Tweet
    success = False
    try:
        a = API.retweet(tweet_id)
        # Sleep for 2 seconds, Thanks Twitter
        print("Aguardando 5 segundos ")
        time.sleep(5)
        print ("Voce retweetou o ID:" + tweet_id)
        success = True
    except tweepy.TweepError as e:
        a = e.response.text
        b = json.loads(a)
        error_code = b['errors'][0]['code']

        if (error_code == 327):
            success = True
