from flask import *
from flask_login import login_required
from . import db

routes = Blueprint("routes", __name__)

@routes.route("/")
@login_required
def index():
    return render_template("index.html")

@routes.route("/account")
@login_required
def account():
    return render_template("account.html")