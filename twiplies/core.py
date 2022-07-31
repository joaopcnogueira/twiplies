# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['Twiplies']

# %% ../nbs/00_core.ipynb 3
import tweepy
import pandas as pd
from fastcore.utils import *

class Twiplies:
    "Instantiate a Tweepy object to fetch tweets replies."
    def __init__(self, 
                 username, # twitter's account username
                 consumer_key, # twitter's account consumer_key
                 consumer_secret, # twiter's account consumer_secret
                 access_token, # twitter's account access_token
                 access_token_secret): # twitter's account access_token_secret 
        store_attr()
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
    def __str__(self): return f"{self.username}"
    __repr__ = __str__

    def get_replies_from_tweet(self, 
                              tweet_id): # tweet id, you can get it from the last part of the tweet url
        """Get replies from a specfic tweet."""
        tweet_ids = []
        replies = []
        for tweet in tweepy.Cursor(self.api.search_tweets, q='to:'+self.username, result_type='recent').items(10000):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                tweet_ids.append(tweet.in_reply_to_status_id_str)
                replies.append(tweet)

        df = pd.DataFrame({
            'tweet_original': [tweet_id for tweet_id in tweet_ids],
            'tweet_replies': [reply.text for reply in replies],
            'tweet_user': [reply.user.screen_name for reply in replies],
            'tweet_location': [reply.user.location for reply in replies]
        })

        return df
