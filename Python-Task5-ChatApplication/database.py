import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).parent / "chat.db"
SCHEMA_PATH = Path(__file__).parent / "database" / "schema.sql"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    connection = get_connection()

    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        schema = file.read()

    connection.executescript(schema)
    connection.commit()
    connection.close()