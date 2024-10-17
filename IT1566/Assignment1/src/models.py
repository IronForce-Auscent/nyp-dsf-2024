from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    """
    Schema reference:

    CREATE TABLE "accounts" (
        "id"	INTEGER NOT NULL,
        "username"	BLOB NOT NULL UNIQUE,
        "password"	BLOB NOT NULL,
        "points"	INTEGER NOT NULL,
        "priv_lvl"	INTEGER NOT NULL,
        "email"	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    priv_lvl = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<User {self.id}:{self.username}>"


class Transaction(db.Model):
    """
    Schema reference:

    CREATE TABLE "transactions" (
        "txn_id"	TEXT NOT NULL UNIQUE,
        "txn_date"	NUMERIC NOT NULL,
        "txn_type"	INTEGER NOT NULL,
        "amt"	INTEGER NOT NULL,
        "src_usr_id"	INTEGER NOT NULL,
        "dest_usr_id"	INTEGER NOT NULL,
        "data"	BLOB,
        PRIMARY KEY("txn_id"),
        FOREIGN KEY("src_usr_id") REFERENCES "accounts"("id")
    );
    """
    __tablename__ = "transactions"
    txn_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    txn_date = db.Column(db.DateTime, nullable=False)
    txn_type = db.Column(db.Integer, nullable=False)
    amt = db.Column(db.Integer, nullable=False)
    src_usr_id = db.Column(db.Integer, db.ForeignKey(
        "accounts.id"), nullable=False)
    dest_usr_id = db.Column(db.Integer, db.ForeignKey(
        "accounts.id"), nullable=False)
    data = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"<Transaction {self.id}>"

    def get_transactions_by_user(self, user_id: int) -> dict[list]:
        """
        Get all transactions for a user by user ID
        
        Args:
            user_id (int): User ID
        
        Returns:
            dict[list]: Dictionary containing lists of transactions
        """
        return {
            "from": Transaction.query.filter_by(src_usr_id=user_id).all(),
            "to": Transaction.query.filter_by(dest_usr_id=user_id).all()
        }


class CollectionPoint(db.Model):
    """
    Schema reference:

    CREATE TABLE "collection_points" (
        "id"	INTEGER NOT NULL,
        "loc_name"	TEXT NOT NULL UNIQUE,
        "capacity" INTEGER NOT NULL DEFAULT 0,
        "storage_lvl"	NUMERIC NOT NULL DEFAULT 0,
        PRIMARY KEY("id" AUTOINCREMENT)
    );  
    """
    __tablename__ = "collection_points"
    id = db.Column(db.Integer, primary_key=True)
    loc_name = db.Column(db.String(100), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    storage_lvl = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<CollectionPoint {self.id}:{self.loc_name}>"
    
    def get_collection_points(self, storage_lvl: int) -> list:
        """
        Get all collection points with storage level greater than or equal to the specified level
        
        Args:
            storage_lvl (int): Storage level
        
        Returns:
            list: List of collection points
        """
        return CollectionPoint.query.filter(CollectionPoint.storage_lvl >= storage_lvl).all()

class RewardItem(db.Model):
    """
    Schema reference:
    """
    __tablename__ = "rewards"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"<RewardItem {self.id}:{self.name}>"