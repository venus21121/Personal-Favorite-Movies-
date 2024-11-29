from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from .route import main_bp
    app.register_blueprint(main_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
