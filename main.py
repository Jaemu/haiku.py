from flask import Flask, render_template
from flask import json
from haiku import Haiku

haiku = Haiku()


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def root():
	return render_template('index.html')



@app.route('/haiku')
def name_haiku():
	h = haiku.makeHaiku()
	return json.jsonify(**h)


@app.route('/syllable/<word>')
def count_syllables(word):
	count = haiku.countSyllables(word)
	return json.jsonify(**count)


@app.route('/info/<word>')
def get_word_data(word):
	return json.jsonify(**haiku.getWordData(word))

@app.route('/similar/<word>')
def similar_words(word):
	return json.jsonify(**haiku.getSimilarWords(word))

@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, nothing at this URL.', 404

if __name__ == '__main__':
		app.run()