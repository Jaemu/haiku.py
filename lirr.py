import tweepy
import json
import pickle
import re

class lirr():

	def __init__():
		self.tweets = []
		self.delays = []
		self.cancels = []
		self.total_delay_times = {}
		# Load list of stops pre-ordered east -> west
		with open('stops.p') as f:
			self.stops = pickle.load(f)

		# Load auth
		with open('access.json') as f:
			secrets = json.load(f)

		# Load stop:branch map
		with open('stops.json') as f:
			self.station_map = json.load(f)

		self.delay_regex = re.compile('^.* is operating \d* .* late .*$')
		self.canceled_regex = re.compile('^.*canceled.*$')

		# Authenticate with Twitter
		auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret_key'])
		auth.set_access_token(secrets['access_token'], secrets['secret_access_token'])
		self.api = tweepy.API(auth)
	
	def load_tweets():	
		# Load 2 pages of tweets
		self.tweets = [tweet.text for tweet in self.api.user_timeline(screen_name='lirr', count=300, page=1)+
					   self.api.user_timeline(screen_name='lirr', count=300, page=2)]

	def get_relevant_tweets():
		for tweet in self.tweets:
			if self.delay_regex.match(tweet):
				self.delays.append(tweet)
			elif self.canceled_regex.match(tweet):
				self.cancels.append(tweet)

	def process_delay_times():
		line = ''
		for delay in self.delays:
			#get branch
			for station in station_map:
				if station in delay:
					line = station_map[station]
			#remove start/end times by starting at the 'is operating' substring
			delay = delay[delay.find('operating'):]
			delay_time = int(re.search(r'\d+',delay).group(0))
			if line in self.total_delay_times:
				total_delay_times[line] = total_delay_times[line] + delay_time
			else
				total_delay_times[line] = delay_time

	def return_delays():
		self.load_tweets()
		self.get_relevant_tweets()
		self.process_delay_times()
		return self.total_delay_times

