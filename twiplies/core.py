# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['Twiplies']

# %% ../00_core.ipynb 3
import tweepy
import pandas as pd
from fastcore.utils import *

class Twiplies:
    """Instantiate a Tweepy object to fetch tweets replies."""
    def __init__(self, username, consumer_key, consumer_secret, access_token, access_token_secret):
        store_attr()
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
    __repr__ = basic_repr('username')

    def get_replies_from_tweet(self, tweet_id):
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
