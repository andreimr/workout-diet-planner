class Diet:
    def init(self, user_id, diet_plan):
        self.user_id = user_id
        self.diet_plan = diet_plan

    def generate_diet_plan(self, goals):
        if goals == "weight loss":
            diet_plan = "Eat 500 calories less than your daily maintenance level. Eat plenty of fruits and vegetables."
        elif goals == "muscle gain":
            diet_plan = "Eat 500 calories more than your daily maintenance level. Eat plenty of protein."
        else:
            diet_plan = "Eat a balanced diet with plenty of fruits and vegetables."

        return diet_plan
    
