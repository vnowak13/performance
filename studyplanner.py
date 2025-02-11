# Study Planner
# Author: Victoria Nowak
# Date: 02/05/2025
# Description: This program helps students plan out their study days and
#              send reminders for upcoming deadlines 

import datetime

def create_study_plan(deadlines, study_days):
    # Create an empty list to store the study plan
    study_plan = []

    # Get the current date to compare deadlines and study days
    today = datetime.date.today()
 # Loop through the deadlines and check if each deadline is coming soon
    for subject, deadline in deadlines.items():
        days_left = (deadline - today).days

        # Create a message based on how many days are left
        if days_left <= 1:
            reminder = f"Urgent: Study for {subject}, Deadline in {days_left} day!"
        elif days_left <= 3:
            reminder = f"Reminder: Study for {subject}, Deadline in {days_left} days."
        else:
            reminder = f"{subject}: No immediate deadline. Study at your pace."

        # Check if the subject is in the study_days list, meaning it's one of the study days
        if subject in study_days:
            study_plan.append(f"On {study_days[subject]}, {reminder}")

    return study_plan

def display_study_plan(study_plan):
    if study_plan:
        print("Your study plan:")
        for plan in study_plan:
            print(plan)
    else:
        print("No study plan created or no upcoming deadlines.")
