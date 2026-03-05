from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = ""
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql:/PLACEHOLDER:PLACEHOLDER@PLACEHOLDER/PLACEHOLDER"
    db.init_app(app)

    from routes import register_routes
    register_routes(app,db)

    migrate = Migrate(app,db)

    return app