from flask import *
from flask_login import *
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False
    
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    return redirect(url_for("routes.index"))

@auth.route("/register")
def register():
    return render_template("register.html")

@auth.post("/register")
def register_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    
    user = User.query.filter_by(email=email).first()
    if user:
        flash("Username or email already exists.")
        return redirect(url_for("auth.register"))
    
    new_user = User(email=email, username=username, password=generate_password_hash(password, method="scrypt"), points=0, priv_lvl=0)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("auth.login"))

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))