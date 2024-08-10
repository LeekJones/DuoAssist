import sqlite3

def create_database():
    """
    Creates the necessary tables in the SQLite database for storing progress, memos, and grocery lists.
    """
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS progress
                 (date TEXT, workout TEXT, completed BOOLEAN)''')
    c.execute('''CREATE TABLE IF NOT EXISTS memos
                 (id INTEGER PRIMARY KEY, memo TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS grocery_list
                 (id INTEGER PRIMARY KEY, item TEXT)''')
    conn.commit()
    conn.close()

def log_workout(date, workout, completed):
    """
    Logs a completed workout session into the database.

    Args:
        date (str): The date of the workout session.
        workout (str): The workout performed.
        completed (bool): Whether the workout was completed.
    """
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    c.execute("INSERT INTO progress (date, workout, completed) VALUES (?, ?, ?)", (date, workout, completed))
    conn.commit()
    conn.close()
