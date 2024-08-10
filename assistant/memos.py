import sqlite3
from .assistant import speak

def add_memo(memo):
    """
    Adds a memo to the database and confirms the addition via speech.

    Args:
        memo (str): The memo text to be stored.
    """
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    c.execute("INSERT INTO memos (memo) VALUES (?)", (memo,))
    conn.commit()
    conn.close()
    speak("Memo added successfully.")

def list_memos():
    """
    Retrieves and reads aloud all memos stored in the database.
    """
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    c.execute("SELECT id, memo FROM memos")
    memos = c.fetchall()
    conn.close()
    if memos:
        for memo in memos:
            speak(f"Memo {memo[0]}: {memo[1]}")
    else:
        speak("No memos found.")
