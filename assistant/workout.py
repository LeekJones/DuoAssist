import pandas as pd
import numpy as np

def generate_workout(goal, equipment):
    """
    Generates a workout plan based on the user's fitness goal and available equipment.

    Args:
        goal (str): The fitness goal, such as 'strength', 'cardio', or 'flexibility'.
        equipment (str or None): The equipment available, or None if no equipment is specified.

    Returns:
        list: A list of exercises tailored to the user's goal and equipment.
    """
    workouts = {
        "strength": ["Push-ups", "Squats", "Deadlifts"],
        "cardio": ["Running", "Cycling", "Jump Rope"],
        "flexibility": ["Yoga", "Stretching"]
    }
    if goal in workouts:
        if equipment:
            plan = [f"{exercise} with {equipment}" for exercise in workouts[goal]]
        else:
            plan = workouts[goal]
    else:
        plan = ["No workout available for this goal"]
    return plan
