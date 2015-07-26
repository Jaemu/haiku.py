# Syllable counter c/o 
# Jordan Boyd-Graber (https://groups.google.com/forum/#!msg/nltk-users/mCOh_u7V8_I/HsBNcLYM54EJ)
# 
# 
import string
from nltk.corpus import cmudict

class Haiku:


	def __init__(self):
		self.dict = cmudict.dict()

	def userHaiku(self, name='bob'):
		haiku = {'1':"name is the coolest", 
		'2':"this is the worst haiku guys", 
		'3':"I am not clever"}
		haiku['1'] = haiku['1'].replace('name', name)
		return haiku

	def countSyllables(self, word='hello'):
		return {
			word : max([len([y for y in x if y[-1] in string.digits]) for x in self.dict[word.lower()]])
		}