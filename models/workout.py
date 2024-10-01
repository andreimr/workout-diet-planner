class Workout:
    def __init__(self, user_id, workout_plan):
        self.user_id = user_id
        self.workout_plan = workout_plan

    def generate_workout_plan(self, goals):
        if goals == "weight loss":
            workout_plan = "Do 30 minutes of cardio 3 times a week. Eat a healthy diet with plenty of fruits and vegetables."
        elif goals == "muscle gain":
            workout_plan = "Do 30 minutes of weightlifting 3 times a week. Eat a healthy diet with plenty of protein."
        else:
            workout_plan = "Do 30 minutes of yoga 3 times a week. Eat a healthy diet with plenty of fruits and vegetables."

        return workout_plan