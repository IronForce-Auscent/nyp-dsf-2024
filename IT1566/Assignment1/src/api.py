from flask import Blueprint, jsonify
from . import db

api = Blueprint("api", __name__)

# Public API routes

@api.get("/api/points")
def get_user_points():
    return jsonify({"points": "Not implemented yet"})

@api.get("/api/rewards/list")
def get_rewards_list():
    return jsonify({"rewards": "Not implemented yet"})

@api.post("/api/rewards/exchange")
def exchange_rewards():
    return jsonify({"exchange": "Not implemented yet"})

@api.get("/api/collection/list")
def get_collection_points_list():
    return jsonify({"collection_points": "Not implemented yet"})

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