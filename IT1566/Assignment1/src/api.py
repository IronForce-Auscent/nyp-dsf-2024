from werkzeug.security import generate_password_hash, check_password_hash
from flask import *
from .models import *
from .logging import LoggingHandler
from . import db
import os
import json
import datetime

api = Blueprint("api", __name__)
DEV_TOKEN = os.getenv("DEV_TOKEN_NOPROD")
logs = LoggingHandler(__name__)

# Public API routes

@api.get("/api/points")
def get_user_points():
    user_id = request.args.get("user_id")
    if user_id and User.query.get(user_id):
        logs.create_log(f"Requested user points for {user_id}", 1)
        return jsonify({"user_id": user_id, "points": User.query.get(user_id).points})
    logs.create_log(f"Failed to retrieve user points for {user_id}", 2)
    return jsonify({"status": "400"})

@api.get("/api/rewards/list")
def get_rewards_list():
    with open("static/data/rewards.json", "r") as f:
        logs.create_log("Requested rewards list", 1)
        return jsonify({"rewards": json.load(f)})

@api.post("/api/rewards/exchange")
def exchange_rewards():
    user_id = request.form.get("user_id")
    if user_id and User.query.get(user_id):
        user_obj = User.query.get(user_id)
        user_points = int(user_obj.points)
        reward_id = int(request.form.get("reward_id"))
        quantity = int(request.form.get("quantity"))
        if not reward_id or not quantity: 
            logs.create_log(f"Failed to exchange rewards for user {user_id} due to missing parameters", 2)
            return jsonify({"status": "400", "message": "Missing parameters"})
        
        reward_item = RewardItem.query.get(reward_id)
        if reward_item:
            total_cost = quantity * reward_item.cost
            if user_points >= total_cost:
                user_obj.points -= total_cost
                
                new_txn = Transaction(
                    txn_date=datetime.datetime.now(),
                    txn_type="CLAIMED",
                    amt=total_cost,
                    src_usr_id=user_id,
                    dest_usr_id=User.query.filter_by(username="RedeemDest").first().id,
                    data=f"Redeemed {quantity}x {reward_item.name}",
                )
                db.session.add(new_txn)
                db.session.commit()
                logs.create_log(f"Redeemed {total_cost} points for user {user_id} (txn {new_txn.txn_id})", 1)
                return jsonify({"status": "200", "message": "Reward claimed"})
            
            logs.create_log(f"User {user_id} attempted to claim more points than is available. Available: {user_points}; Tried to claim: {total_cost}", 2)
            return jsonify({"status": "400", "message": "Insufficient points"})
        
        logs.create_log(f"Failed to find reward item with ID {reward_id}", 2)
        return jsonify({"status": "400", "message": f"No matching records found for reward ID {reward_id}"})
    
    logs.create_log(f"Failed to retrieve user points for {user_id}", 2)
    return jsonify({"status": "400"})

@api.get("/api/collection/list")
def get_collection_points_list():
    with open("static/data/collection_points.json", "r") as f:
        logs.create_log("Requested collection points list", 1)
        return jsonify({"collection_points": json.load(f)})

# Internal API routes

@api.get("/api/internal/accounts")
def get_accounts():
    return jsonify({"accounts": "Not implemented yet"})

@api.get("/api/internal/transactions")
def get_transactions():
    return jsonify({"transactions": "Not implemented yet"})

@api.get("/api/internal/collection")
def get_collection_status():
    return jsonify({"collection_points": "Not implemented yet"})

@api.get("/api/internal/transaction-history/<int:account_id>")
def get_account_transactions():
    return jsonify({"transactions": "Not implemented yet"})

@api.put("/api/internal/accounts/<int:account_id>/points")
def modify_account_points():
    return jsonify({"status": "Not implemented yet"})

# Development endpoints
@api.route("/dev/user/create", methods=["POST"])
def dev_create_user():
    auth_key = request.headers.get("Authorization")
    if auth_key == DEV_TOKEN:
        try:
            email = request.form.get("email")
            username = request.form.get("username")
            password = request.form.get("password")
            points = request.form.get("points")
            priv_lvl = request.form.get("priv_lvl")
            new_user = User(email=email, username=username, password=generate_password_hash(password), points=points, priv_lvl=priv_lvl)
            db.session.add(new_user)
            db.session.commit()
            logs.create_log(f"Created new user {username} (Auth key: {auth_key})", 1)
            return jsonify({"status": "User created"})
        except Exception as e:
            logs.raise_exception(f"Failed to create user: {str(e)}")
            return jsonify({"status": "Error", "message": str(e)})
    logs.raise_exception(f"Unauthorized access attempt (Auth key: {auth_key})")
    return jsonify({"status": "Unauthorized"})

@api.route("/dev/user/delete", methods=["POST"])
def dev_delete_user():
    auth_key = request.headers.get("Authorization")
    if auth_key == DEV_TOKEN:
        try:
            user_id = request.form.get("user_id")
            user = User.query.get(user_id)
            db.session.delete(user)
            db.session.commit()
            logs.create_log(f"Deleted user {user_id} (Auth key: {auth_key})", 1)
            return jsonify({"status": "User deleted"})
        except Exception as e:
            logs.raise_exception(f"Failed to delete user: {str(e)}")
            return jsonify({"status": "Error", "message": str(e)})
    logs.raise_exception(f"Unauthorized access attempt (Auth key: {auth_key})")
    return jsonify({"status": "Unauthorized"})

@api.route("/dev/points/set", methods=["POST"])
def dev_set_points():
    auth_key = request.headers.get("Authorization")
    if auth_key == DEV_TOKEN:
        try:
            user_id = request.form.get("user_id")
            user = User.query.get(user_id)
            points = request.form.get("points")
            user.points = points
            db.session.commit()
            logs.create_log(f"Set points for user {user_id} (Auth key: {auth_key})", 1)
            return jsonify({"status": "Points set"})
        except Exception as e:
            logs.raise_exception(f"Failed to set points: {str(e)}")
            return jsonify({"status": "Error", "message": str(e)})
    logs.raise_exception(f"Unauthorized access attempt (Auth key: {auth_key})")
    return jsonify({"status": "Unauthorized"})