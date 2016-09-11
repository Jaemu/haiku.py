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
		self.pattern = [[
			[
				("NNS", 2),
				("VBG", 3)
			],[
				("VBG", 3),
				["in the", "with some", "like some", "without my", "like the", "of the"],
				("NNS", 2)
			],[
				("VBG", 2),
				("RB", 3)
			]],
			[[
				("NNS", 1),
				("VBG", 2),
				("IN", 2)
			],[
				["I", "He", "She", "They"],
				("VBD", 1),
				["in the", "with the", "like the", "without my"],
				("JJS", 2),
				("NN", 1)
			],[
				("VBG", 2),
				("RB", 3)
			]
			]
		]
		#self.insult_pattern = [
		#	"You're the",
		#	("JJS"),
		#	("NN"),
		#	("that ever"),
		#	("VBD")
		#]
		self.fart_pattern = [
			"I",
			("VB"),
			"in your general direction",
		]
		self.worse_insult_pattern = [
			"Your mother was a",
			("NN"),
			"and your father smelled of",
			("NNS")
		]
		self.grammar = [
			"CC",
			"CD",
			"DT",
			"EX",
			"FW",
			"IN",
			"JJ",
			"JJR",
			"JJS",
			"LS",
			"MD",
			"NN",
			"NNS",
			"NNP",
			"NNPS",
			"PDT",
			"POS",
			"PRP",
			"PRP$",
			"RB",
			"RBR",
			"RBS",
			"RP",
			"SYM",
			"TO",
			"UH",
			"VB",
			"VBD",
			"VBG",
			"VBN",
			"VBP",
			"VBZ",
			"WDT",
			"WP",
			"WP$",
		]

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
		currentHaiku = random.choice(self.pattern)
		for line in xrange(len(currentHaiku)):
			haiku[line] = []
			for i in xrange(len(currentHaiku[line])):
				if not (len(currentHaiku[line][i]) > 2):
					currentPattern = currentHaiku[line][i]
					category = currentPattern[0]
					syllable = currentPattern[1]
					similarWords = [x for x in self.tagged_words if x[1] == category and x[2] == syllable]
					haiku[line].append(random.choice(similarWords)[0])
				else:
					haiku[line].append(random.choice(currentHaiku[line][i]))
		return {
			'haiku': haiku
		}

	def insult(self, name="Sunshine"):
		currentInsult = ""
		insultPattern = random.choice([self.fart_pattern, self.worse_insult_pattern])
		#insultPattern = self.worse_insult_pattern
		for pattern in insultPattern:
			if pattern in self.grammar:
				similarWords = [x for x in self.tagged_words if x[1] == pattern]
				currentInsult = currentInsult + ' ' + random.choice(similarWords)[0]
			else:
				currentInsult = currentInsult + ' ' + pattern
		currentInsult = currentInsult + '!'
		return {
			'result': currentInsult
		}


