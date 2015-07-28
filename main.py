from flask import Flask
from flask import json
from haiku import Haiku

haiku = Haiku()


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello():
	"""Return a friendly HTTP greeting."""
	return 'Hello World!'


@app.route('/haiku/<name>')
def name_haiku(name):
	h = haiku.userHaiku(name)
	return json.jsonify(**h)


@app.route('/syllable/<word>')
def count_syllables(word):
	count = haiku.countSyllables(word)
	return json.jsonify(**count)


@app.route('/info/<word>')
def get_word_data(word):
	return json.jsonify(**haiku.getWordData(word))

@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, nothing at this URL.', 404

#if __name__ == '__main__':
#		app.run()