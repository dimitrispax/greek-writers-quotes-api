from flask import Flask, request, jsonify
from webscraper import quotes
app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

# The route to get all the quotes.
@app.route("/quotes")
def get_quotes():
    return jsonify(quotes), 200

if __name__ == "__main__":
    app.run(debug=True)
