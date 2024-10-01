class User:
    def __init__(self, name, age, weight, height, goals):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.goals = goals

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi

    def calculate_daily_caloric_needs(self):
        daily_caloric_needs = 2500
        return daily_caloric_needs

    def calculate_macronutrient_requirements(self):
        macronutrient_requirements = {
            'protein': 100,
            'carbohydrates': 200,
            'fat': 50
        }
        return macronutrient_requirements