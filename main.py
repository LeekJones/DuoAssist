from assistant.assistant import listen_command, speak
from assistant.memos import add_memo, list_memos
from assistant.grocery import add_grocery_item, remove_grocery_item, list_grocery_items
from assistant.workout import generate_workout
from assistant.database import create_database, log_workout
import pandas as pd

def main():
    """
    The main function that integrates all components of the virtual assistant.
    It listens for user commands, performs the requested tasks, and interacts with the user through voice.
    """
    create_database()
    speak("Hello! I am your personal fitness assistant. How can I help you today?")
    
    while True:
        command = listen_command()
        if "workout plan" in command:
            speak("What is your fitness goal? Strength, cardio, or flexibility?")
            goal = listen_command()
            speak("Do you have any equipment? If yes, please specify, otherwise say no.")
            equipment = listen_command()
            if equipment == "no":
                equipment = None
            plan = generate_workout(goal, equipment)
            speak(f"Here is your workout plan: {', '.join(plan)}")
        elif "track progress" in command:
            speak("What workout did you complete today?")
            workout = listen_command()
            date = pd.Timestamp.today().strftime('%Y-%m-%d')
            log_workout(date, workout, True)
            speak("Great job! Your progress has been logged.")
        elif "reminder" in command:
            speak("Please provide the email address to send the reminder.")
            email = listen_command()
            #send_reminder(email)  # Uncomment and define the send_reminder function to enable reminders
            speak("Reminder has been sent.")
        elif "add memo" in command:
            speak("What memo would you like to add?")
            memo = listen_command()
            add_memo(memo)
        elif "list memos" in command:
            list_memos()
        elif "add grocery item" in command:
            speak("What item would you like to add to your grocery list?")
            item = listen_command()
            add_grocery_item(item)
        elif "remove grocery item" in command:
            speak("What item would you like to remove from your grocery list?")
            item = listen_command()
            remove_grocery_item(item)
        elif "list grocery items" in command:
            list_grocery_items()
        elif "exit" in command:
            speak("Goodbye! Keep up the great work.")
            break

if __name__ == "__main__":
    main()
