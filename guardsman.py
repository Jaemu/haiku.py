import tweepy
import json
from haiku import Haiku

with open('access.json') as f:
	secrets = json.load(f)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret_key'])
auth.set_access_token(secrets['access_token'], secrets['secret_access_token'])


class CustomStreamListener(tweepy.StreamListener):
	def __init__(self):
		self.haiku = Haiku()
		# Load auth
		with open('access.json') as f:
			secrets = json.load(f)

		auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret_key'])
		auth.set_access_token(secrets['access_token'], secrets['secret_access_token'])
		self.api = tweepy.API(auth)

	def on_status(self, status):
		print status.text
		print status.user.screen_name
		self.api.update_status('@'+status.user.screen_name+' '+self.haiku.insult()['result'], in_reply_to_status_id = status.id)

	def on_error(self, status_code):
		print >> sys.stderr, 'Encountered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['@frenchguardsman'])
