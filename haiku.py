# Syllable counter c/o 
# Jordan Boyd-Graber (https://groups.google.com/forum/#!msg/nltk-users/mCOh_u7V8_I/HsBNcLYM54EJ)
# 
# 
import random
import string
import nltk
import pickle
from nltk.corpus import cmudict, ptb, brown
from nltk import word_tokenize,sent_tokenize

class Haiku:


	def __init__(self):
		self.cmudict = cmudict.dict()
		self.words = self.cmudict.keys()
		self.tagged_words = pickle.load(open('tagged_words_syl.p', "rb"))
		#for i in xrange(len(self.tagged_words)):
		#	self.tagged_words[i] = [self.tagged_words[i][0], self.tagged_words[i][1], self._syllableHelper(self.tagged_words[i][0])]
		#pickle.dump(self.tagged_words, open("tagged_words_syl.p", "wb"))
		self.pattern = {
			'line 1': [
				("NNS", 2),
				("VBG", 3)
			],
			'line 2': [
				("VBG", 3),
				("JJ", 2),
				("NNS", 2)
			],
			'line 3': [
				("JJS", 2),
				("NNS", 1)

			]
		}

	def userHaiku(self, name='bob'):
		haiku = {'1':"name is the coolest", 
		'2':"this is the worst haiku guys", 
		'3':"I am not clever"}
		haiku['1'] = haiku['1'].replace('name', name)
		return haiku

	def countSyllables(self, query='hello'):
		result = {}
		words = query.strip().split(',')
		for word in words:
			try:
				result[word] = max([len([y for y in x if y[-1] in string.digits]) for x in self.cmudict[word.lower()]])
			except:
				result[word] = 'Error - ' + word + ' is not a recognized word'
		return result

	def _syllableHelper(self, query='hello'):
		return max([len([y for y in x if y[-1] in string.digits]) for x in self.cmudict[query.lower()]])

	def getWordData(self, word="hello world"):
		try:
			words = word.replace(',', ' ')
			result = {}
			result['data'] = nltk.pos_tag(word_tokenize(words))
			return result
		except:
			return {
				word: 'Error: ' + word + ', bad data'
			}


	def getSimilarWords(self, word="hello"):
		wordData = nltk.pos_tag(word_tokenize(word))
		category = wordData[0][1]
		syllable = self._syllableHelper(word)
		similarWords = [x for x in self.tagged_words if x[1] == category and x[2] == syllable]
		return {
			word: similarWords,
			'category': category
		}

	def makeHaiku(self):
		haiku = {}
		for line in self.pattern:
			haiku[line] = []
			for i in xrange(len(self.pattern[line])):
				currentPattern = self.pattern[line][i]
				category = currentPattern[0]
				syllable = currentPattern[1]
				similarWords = [x for x in self.tagged_words if x[1] == category and x[2] == syllable]
				haiku[line].append(random.choice(similarWords)[0])
		return haiku


