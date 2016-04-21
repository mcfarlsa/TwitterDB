#!/usr/local/bin/python

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv, sys, json, datetime, codecs

#Variables that contains the user credentials to access Twitter API 
access_token = '<INSERT_HERE>'
access_token_secret = '<INSERT_HERE>'
consumer_key = '<INSERT_HERE>'
consumer_secret = '<INSERT_HERE>'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

	filedate = datetime.datetime.now().strftime ('%Y%m%d')
	counter = 0
	tweet_list = []

	def on_data(self, data):
		json_data = json.loads(data)

		if 'limit' in json_data:
			return True

		else:
			StdOutListener.tweet_list.append(data)
	
			#IF BATCH FULL IS FULL THEN WRITE VALUES TO FILE
			if StdOutListener.counter == 999: #DEFINE NUMBER OF TWEETS FOR BATCH INSERT
				if StdOutListener.filedate != datetime.datetime.now().strftime ('%Y%m%d'):
					filename = '/media/data/daily_files/raw_files/tweets_' + StdOutListener.filedate + '.trg'
					with open(filename, 'w') as outfile:
						 outfile.write(StdOutListener.filedate)
				StdOutListener.filedate = datetime.datetime.now().strftime ('%Y%m%d')
				filename = '/media/data/daily_files/raw_files/tweets_' + StdOutListener.filedate + '.txt'
				with codecs.open(filename, 'a', 'utf8') as outfile:
					for item in StdOutListener.tweet_list:
						outfile.write(item)
			
				StdOutListener.counter = 0
				del StdOutListener.tweet_list[:]
		
			else:
				#UPDATE COUNTER FOR EACH TWEET (outside batch statement)
				StdOutListener.counter = StdOutListener.counter + 1
	
			return True

	def on_error(self, status):
		print status


if __name__ == '__main__':

	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

	#This line filters tweets to mainland US only
	stream.filter(locations=[-124.94,25.03,67.06,49.02])