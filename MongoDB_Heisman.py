
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:01:08 2016

@author: armand
code found at https://www.linkedin.com/pulse/collecting-twitter-stream-using-python-mongodb-shailendra
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json

# Insert your API Keys below
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


 

# Defining listener class for getting the streamingclass StdOutListener(StreamListener):
class StdOutListener(StreamListener):
    def on_data(self, testdata2):           

#Retrieving the details like Id, tweeted text and created at.
#        while (time.time() - self.time) < self.limit:
#            try:
                
        tweet=json.loads(testdata2)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind=collection.insert_one(obj).inserted_id

        print(obj)

        return True

def on_error(self, status):

    print(status)

if __name__ == '__main__':

 

#This handles Twitter authetification and the connection to Twitter Streaming AP

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

 

 # Below code  is for making connection with mongoDB

from pymongo import MongoClient   
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.Heisman_database2
collection = db.Heisman_collection2

#This line filters Twitter Streams to capture data with the keyword: 'Heisman'

stream.filter(track=['Heisman'])


