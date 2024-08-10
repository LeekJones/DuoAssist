import sqlite3
from .assistant import speak

def add_grocery_item(item):
    """
    Adds an item to the grocery list in the database and confirms the addition via speech.

    Args:
        item (str): The grocery item to be added.
    """
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    c.execute("INSERT INTO grocery_list (item) VALUES (?)", (item,))
    conn.commit()
    conn.close()
    speak("Item added to grocery list.")

def remove_grocery_item(item):
    """
    Removes an item from the grocery list in the database and confirms the removal via speech.

    Args:
        item (str): The grocery item to be removed.
    """
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    c.execute("DELETE FROM grocery_list WHERE item=?", (item,))
    conn.commit()
    conn.close()
    speak("Item removed from grocery list.")

def list_grocery_items():
    """
    Retrieves and reads aloud all items stored in the grocery list.
    """
    conn = sqlite3.connect('assistant.db')
    c = conn.cursor()
    c.execute("SELECT item FROM grocery_list")
    items = c.fetchall()
    conn.close()
    if items:
        for item in items:
            speak(f"Grocery item: {item[0]}")
    else:
        speak("No items in grocery list.")
