from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import *
from . import db

import os
import sqlite3

DB_CORE_URI = "instance/primary.db"

class DBAPI():
    def __init__(self, db_uri: str = DB_CORE_URI, table_names: list = None):
        self.__db_uri: str = db_uri
        self.__table_names: list = table_names
        
    def query_data(self, filters: dict | None = None) -> dict:
        results = {}
        with sqlite3.connect(self.__db_uri) as __conn:
            __cursor = __conn.cursor()
            
            for table in self.__table_names:
                query = f"SELECT * FROM {table}"
                parameters = []
                if filters:
                    query += " WHERE " + " AND ".join([f"{col} = ?" for col in filters.keys()])
                    parameters.extend(filters.values())
                
                results[table] = __cursor.execute(query, parameters).fetchall()
        return results

    
    def insert_data(self, table_name: str, data: dict) -> None:
        query = f"INSERT INTO {table_name} ({','.join(data.keys())}) VALUES ({','.join(['?' for _ in data])})"
        with sqlite3.connect(self.__db_uri) as __conn:
            __cursor = __conn.cursor()
            __cursor.execute(query, tuple(data.values()))
            __conn.commit()
        return True
    
    def update_data(self, table_name: str, data: dict, filters: dict) -> None:
        query = f"UPDATE {table_name} SET {','.join([f'{key} = ?' for key in data])} WHERE {','.join([f'{key} = ?' for key in filters])}"
        with sqlite3.connect(self.__db_uri) as __conn:
            __cursor = __conn.cursor()
            __cursor.execute(query, tuple(data.values()) + tuple(filters.values()))
            __conn.commit()
        return True
    
    def delete_data(self, table_name: str, filters: dict) -> None:
        query = f"DELETE FROM {table_name} WHERE {','.join([f'{key} = ?' for key in filters])}"
        with sqlite3.connect(self.__db_uri) as __conn:
            __cursor = __conn.cursor()
            __cursor.execute(query, tuple(filters.values()))
            __conn.commit()
        return True


class AccountsHandler():
    def __init__(self):
        self.db_api = DBAPI(
            table_names=["accounts"]
        )
    
    def check_for_existing_user(self, username: str, email: str) -> bool:
        results = self.db_api.query_data({"username": username, "email": email})
        return results["accounts"] != []
    
    def register_new_user(self, username: str, email: str, password: str) -> bool:
        if self.check_for_existing_user(username, email):
            return False
        hashed_password = generate_password_hash(password)
        self.db_api.insert_data("accounts", {"username": username, "email": email, "password": hashed_password, "points": 0, "priv_lvl": 0})
        return True
    
    def login_user(self, email: str, password: str) -> bool:
        results = self.db_api.query_data({"email": email})
        if results["accounts"] == []:
            return False
        user = results["accounts"][0]
        if not check_password_hash(user[2], password):
            return False
        class User(UserMixin):
            pass
        logged_user = User()
        logged_user.id = user[0]
        login_user(logged_user)
        return True