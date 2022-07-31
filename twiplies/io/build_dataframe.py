# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_build_dataframe.ipynb.

# %% auto 0
__all__ = ['build_dataframe']

# %% ../nbs/01_build_dataframe.ipynb 2
import pandas as pd
from typing import List


def build_dataframe(tweet_ids: List, replies: List):
    "Build a dataframe with each tweet's replies for line."
    
    df = pd.DataFrame({
        'tweet_original': [tweet_id for tweet_id in tweet_ids],
        'tweet_replies': [reply.text for reply in replies],
        'tweet_user': [reply.user.screen_name for reply in replies],
        'tweet_location': [reply.user.location for reply in replies]
    })

    return df
