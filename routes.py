import json
import random
from pathlib import Path
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

DATA_DIR = Path(__file__).parent / 'data'

QUOTES_FILE = DATA_DIR / 'quotes.json'

# Load quotes data
def load_quotes():
    try:
        with open(QUOTES_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Quotes file not found at {QUOTES_FILE}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in quotes file: {e}", e.doc, e.pos)


try:
    quotes = load_quotes()
except Exception as e:
    quotes = []

@api_bp.route("/")
def root():
    return jsonify({
        "message": "Greek Writers Quotes API",
        "endpoints": {
            "/api/quotes": "Get all quotes in shuffled order",
            "/api/quote": "Get a single random quote",
            "/health": "Health check endpoint"
        }
    }), 200

@api_bp.route('/health')
def health():
    health_status = {
        "status": "healthy",
        "quotes": {
          "loaded": len(quotes) > 0,
          "total": len(quotes)
        }
    }
    
    if len(quotes) == 0:
        health_status["status"] = "degraded"

        health_status["warning"] = "No quotes loaded"

        return jsonify(health_status), 503
    
    return jsonify(health_status), 200

# Get all quotes in shuffled order
@api_bp.route('/api/quotes')
def get_quotes():
    if not quotes:
        return jsonify({"error": "No quotes available"}), 500
    
    shuffled = quotes.copy()

    random.shuffle(shuffled)

    return jsonify(shuffled), 200

# Get a single random quote.
@api_bp.route('/api/quote')
def get_quote():
    if not quotes:
        return jsonify({"error": "No quotes available"}), 500
    
    random_quote = random.choice(quotes)

    return jsonify(random_quote), 200

@api_bp.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@api_bp.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500
