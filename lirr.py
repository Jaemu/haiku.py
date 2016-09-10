import tweepy
import json
import pickle

class lirr():

	def __init__():
		# Load list of stops pre-ordered east -> west
		with open('stops.p') as f:
			self.stops = pickle.load(f)

		with open('access.json') as f:
			secrets = json.load(f)

		auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret_key'])
		auth.set_access_token(secrets['access_token'], secrets['secret_access_token'])
		self.api = tweepy.API(auth)
		self.tweets = [tweet.text for tweet in self.api.user_timeline(screen_name='lirr', count=60)]
