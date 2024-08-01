#[KODA - INIT]

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import koda.config as config

db = SQLAlchemy()

def create_app() -> object:

   app = Flask(__name__)

   # Configure App Settings

   app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
   app.config['SECRET_KEY'] = config.SECRET
   app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

   # DB Setup
   db.init_app(app)

   # Register blueprints
   from koda.blueprints import register_blueprints
   register_blueprints(app)

   # with app.app_context():
   #    db.create_all()

   return app