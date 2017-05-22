import os

import praw

def get_reddit():
    try:
        return praw.Reddit(client_id=os.environ['REDDIT_CLIENT'],
                           client_secret=os.environ['REDDIT_SECRET'],
                           user_agent=os.environ['REDDIT_USER_AGENT'])
    except:
        raise RuntimeException('Error, is REDDIT_CLIENT, REDDIT_SECRET, REDDIT_USER_AGENT')
