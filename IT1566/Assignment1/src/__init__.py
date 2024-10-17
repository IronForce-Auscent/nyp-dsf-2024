from flask import Flask
from flask_login import *
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="../templates")
    
    load_dotenv()
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PRIMARY_URI")
    db.init_app(app)
    
    from . import models
    
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    
    from .models import User
    @login_manager.user_loader
    def load_user(user_id: int):
        return User.query.get(int(user_id))
    
    from src.auth import auth as auth_blueprint
    from src.routes import routes as routes_blueprint
    from src.api import api as api_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(routes_blueprint)
    
    return app