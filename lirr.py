import tweepy
import json
import pickle
import re

class lirr():

	def __init__(self):
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
	
	def load_tweets(self):	
		self.total_delay_times['first'] = {}
		# Load 2 pages of tweets
		self.tweets = [(tweet.text, tweet.created_at) for tweet in self.api.user_timeline(screen_name='lirr', count=300, page=1)+
					   self.api.user_timeline(screen_name='lirr', count=300, page=2)]
		self.total_delay_times['first']['day'] = self.tweets[-1][1].day
		self.total_delay_times['first']['month'] = self.tweets[-1][1].month
		self.total_delay_times['first']['year'] = self.tweets[-1][1].year

	def get_relevant_tweets(self):
		for tweet in self.tweets:
			if self.delay_regex.match(tweet[0]):
				self.delays.append(tweet[0])
			elif self.canceled_regex.match(tweet[0]):
				self.cancels.append(tweet[0])

	def process_delay_times(self):
		self.total_delay_times['delays'] = {}
		line = ''
		start_times = {}
		for delay in self.delays:
			delay = delay.lower()
			start_time = re.search(r'\d*:\d*..',delay).group(0)
			#get branch
			for station in self.station_map:
				if station in delay:
					line = self.station_map[station]
			#remove start/end times by starting at the 'is operating' substring
			delay = delay[delay.find('operating'):]
			delay_time = int(re.search(r'\d+',delay).group(0))
			start_times[start_time] = [delay_time, line]

		for pair in start_times.values():
			if pair[1] in self.total_delay_times['delays']:
				self.total_delay_times['delays'][pair[1]] = self.total_delay_times['delays'][pair[1]] + pair[0]
			else:
				self.total_delay_times['delays'][pair[1]] = pair[0]

	def get_cancellation_counts(self):
		pass

	def return_delays(self):
		self.load_tweets()
		self.get_relevant_tweets()
		self.process_delay_times()
		return self.total_delay_times

