from flask import Flask
from flask_cors import CORS
from routes import api_bp

def create_app(): 
    app = Flask(__name__)
    
    # Configure CORS to allow all origins
    CORS(app, resources={
        r"/*": {
            "origins": "*"
        }
    })
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    return app

app = create_app()
    
if __name__ == '__main__':
    app.run(debug=False)
