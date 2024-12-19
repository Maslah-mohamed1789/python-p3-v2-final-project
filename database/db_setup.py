import sqlite3
from contextlib import closing

# SQLite database file
DB_NAME = 'voting_system.db'

def init_db():
    """Initializes the SQLite database and creates tables."""
    with closing(sqlite3.connect(DB_NAME)) as conn:
        with conn:
            cursor = conn.cursor()
            # Create tables for candidates, voters, and votes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS candidates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    party TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS voters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS votes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    voter_id INTEGER NOT NULL,
                    candidate_id INTEGER NOT NULL,
                    FOREIGN KEY(voter_id) REFERENCES voters(id),
                    FOREIGN KEY(candidate_id) REFERENCES candidates(id)
                )
            ''')
            print("Database initialized and tables created.")

def execute_query(query, params=()):
    """Executes a given query with parameters."""
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

def fetch_all(query, params=()):
    """Fetch all results from a query."""
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()  # Returns a list of tuples

def fetch_one(query, params=()):
    """Fetch one result from a query."""
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()  # Returns a single tuple (or None if no result)
