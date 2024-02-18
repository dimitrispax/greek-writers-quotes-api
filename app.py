from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_shuffled_quotes, get_randomized_quote

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return 'You have reached the root route, try /api/quotes or /api/quote.'

# The route to get all the quotes shuffled.
@app.route('/api/quotes')
def get_quotes():
    shuffled_quotes = get_shuffled_quotes()
    return jsonify(shuffled_quotes), 200

# The route to get a random quote.
@app.route('/api/quote')
def get_quote():
    random_quote = get_randomized_quote()
    return jsonify(random_quote), 200

@app.errorhandler(404)
def not_found_handler(e):
    return 'Not Found.', 404
    
if __name__ == '__main__':
    app.run(debug=False)
