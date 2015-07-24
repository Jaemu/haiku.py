class Haiku:


	def __init__(self):
		self.haikuNameSet = ['bob']
		self.syllablesToNames = {'1': 'bob'}
		self.haikus = {}


	def userHaiku(self, name='bob'):
		haiku = {'1':"name is the coolest", 
		'2':"this is the worst haiku guys", 
		'3':"I am not clever"}
		haiku['1'] = haiku['1'].replace('name', name)
		return haiku
