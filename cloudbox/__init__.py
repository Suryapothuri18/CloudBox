from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import bp  # Import the blueprint

# Initialize the database and migration
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # App configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Update your DB URI as needed
    app.config['SECRET_KEY'] = 'your_secret_key'  # Use a proper secret key in production
    
    # Initialize the database and migrations with the app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register the blueprint
    app.register_blueprint(bp)
    
    return app
