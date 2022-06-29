#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import numpy as np
import pandas as pd
import time


# In[2]:


geo_coordinates = {"Argentina":"-38.4161,-63.6167",
                   "Bolivia": "-16.2902,-63.5887",
                   "Chile": "-35.6751,-71.5430",
                   "Colombia":"4.5709,-74.2973",
                   "Costa_Rica":"9.7489,-83.7534", 
                   "Cuba":"21.5218,-77.7812",
                   "Dominican_Republic":"18.7357,-70.1627",
                   "Ecuador":"-1.8312,-78.1834",
                   "El_Salvador":"13.7942,-88.8965",
                   "Guatemala":"15.7835,-90.2308",
                   "Honduras":"15.2000,-86.2419",
                   "Mexico":"23.6345,-102.5528",
                   "Nicaragua":"12.8654,-85.2072",
                   "Panama":"8.5380,-80.7821",
                   "Paraguay":"-23.4425,-58.4438",
                   "Peru":"-9.1900,-75.0152",
                   "Uruguay":"-32.5228,-55.7658",
                   "Venezuela":"6.4238,-66.5897"
                  }


# In[3]:


CONSUMER_KEY = 'pBVHBFfc7Wb6BplJXAnSIWU10'
CONSUMER_TOKEN = 'bE9b3g4m8J3ul5nloDhII5kpWnLxNH6Gqy0Rd7IpR51JQ4qq1E'

ACCESS_KEY = '471369623-JSGbfk2TNoGRFvo8NWEMd8mfjuNAswayIixX5MtF'
ACCESS_TOKEN = 'WsD9nrUnCXZogUHdHiMIhMOyy4qutSN5IWNfO8kVVBSn7'


# In[4]:


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_TOKEN)
auth.set_access_token(ACCESS_KEY, ACCESS_TOKEN)
api = tweepy.API(auth)


# In[5]:


def scrap_tweets(coord):
    keywords = ''
    tweets = tweepy.Cursor(api.search_tweets, q=keywords, tweet_mode='extended', lang='es', geocode=coord, count=200).items()
    number_of_tweets = 0
    count = 0
    tweet = list()
    tweet_id = list()
    user_id = list()
    coordinates = list()
    location = list()
    created_at = list()
    for i in tweets:
        tweet.append(i._json['full_text'])
        tweet_id.append(i._json['id'])
        user_id.append(i._json['user']['id'])
        coordinates.append(i._json['coordinates'])
        location.append(i._json['user']['location'])
        created_at.append(i._json['created_at'])
        count += 1
        number_of_tweets += 1
        if (count == 15000):
            time.sleep(1000)
            count = 0
        if (number_of_tweets == 1000000):
            df = pd.DataFrame(zip(tweet,tweet_id, user_id,created_at,coordinates, location), columns=['tweets','tweet_id','user_id','time-date','coordinates','location'])
            return df


# In[ ]:


for i in geo_coordinates:
    start_time = time.time()
    
    geo = geo_coordinates[i]+",300km"
    tweet_df = scrap_tweets(geo)
    print('Extraction time for tweets: ' + str(time.time() - start_time) + " seconds")
    print('Tweets for ' + i + ' extracted.')
    print(tweet_df)
    
    tweet_df.to_csv('tweets_'+i+'.csv',sep='\t', index=False)
    time.sleep(1000)


# In[ ]:




