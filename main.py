import tkinter as tk
from tkinter import ttk
from models import User
from models import Workout
from models import Diet

class GUI:
    def init(self):
        self.root = tk.Tk()
        self.root.title("Workout Planner")
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.goals_label = tk.Label(self.root, text="Goals:")
        self.goals_label.pack()

        self.goals_entry = tk.Entry(self.root)
        self.goals_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        goals = self.goals_entry.get()

        # Create a new user object and save it to the database
        user = User(name, email, "", goals)

        # Create a new workout and diet plan based on the user's goals
        workout_plan = ""
        diet_plan = ""

        # Display the workout and diet plan to the user
        self.workout_label = tk.Label(self.root, text="Workout Plan:")
        self.workout_label.pack()

        self.workout_text = tk.Text(self.root)
        self.workout_text.pack()

        self.diet_label = tk.Label(self.root, text="Diet Plan:")
        self.diet_label.pack()

        self.diet_text = tk.Text(self.root)
        self.diet_text.pack()

    def run(self):
        self.root.mainloop()


    def submit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        goals = self.goals_entry.get()

        # Create a new user object and save it to the database
        user = User(name, email, "", goals)

        # Create a new workout and diet plan based on the user's goals
        workout = Workout(user.id, "")
        workout_plan = workout.generate_workout_plan(goals)

        diet = Diet(user.id, "")
        diet_plan = diet.generate_diet_plan(goals)

        # Display the workout and diet plan to the user
        self.workout_label = tk.Label(self.root, text="Workout Plan:")
        self.workout_label.pack()

        self.workout_text = tk.Text(self.root)
        self.workout_text.pack()
        self.workout_text.insert(tk.END, workout_plan)

        self.diet_label = tk.Label(self.root, text="Diet Plan:")
        self.diet_label.pack()

        self.diet_text = tk.Text(self.root)
        self.diet_text.pack()
        self.diet_text.insert(tk.END, diet_plan)
        
if __name__ == "__main__":
    gui = GUI()
    gui.run()