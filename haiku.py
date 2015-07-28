# Syllable counter c/o 
# Jordan Boyd-Graber (https://groups.google.com/forum/#!msg/nltk-users/mCOh_u7V8_I/HsBNcLYM54EJ)
# 
# 
import string
import nltk
from nltk.downloader import download
from nltk.corpus import cmudict, ptb, brown
from nltk import word_tokenize,sent_tokenize

class Haiku:


	def __init__(self):
		self.cmudict = cmudict.dict()

	def userHaiku(self, name='bob'):
		haiku = {'1':"name is the coolest", 
		'2':"this is the worst haiku guys", 
		'3':"I am not clever"}
		haiku['1'] = haiku['1'].replace('name', name)
		return haiku

	def countSyllables(self, word='hello'):
		try:
			words = word.split(',')
			result = {}
			for word in words:
				result[word] = max([len([y for y in x if y[-1] in string.digits]) for x in self.cmudict[word.lower()]])
			return result
		except:
			return {
				word: 'Error: ' + word + ' is not a recognized word'
			}
	def getWordData(self, word="hello world", pos="UH"):
		try:
			words = word.replace(',', ' ')
			result = {}
			result['data'] = nltk.pos_tag(word_tokenize(words))
			return result
		except:
			return {
				word: 'Error: ' + word + ', bad data'
			}