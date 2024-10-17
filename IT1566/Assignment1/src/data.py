from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import *
from . import db

import os
import sqlite3

DB_PRIMARY_URI = os.getenv("DB_PRIMARY_URI", "sqlite:///db.sqlite3")

class DBAPI():
    def __init__(self, db_uri: str = DB_PRIMARY_URI, table_names: list = None):
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
