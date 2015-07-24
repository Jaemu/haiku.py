from flask import Flask
import haiku


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello():
	"""Return a friendly HTTP greeting."""
	return 'Hello World!'


@app.route('/haiku/<name>')
def name_haiku(name='bob'):
	h = haiku.user(name)
	return Flask.jsonify(**h)


@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, nothing at this URL.', 404
