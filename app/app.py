from flask import Flask, render_template, request
from models.user import User
from models.workout import Workout
from models.diet import Diet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = request.form
        user = User(user_data['name'], user_data['age'], user_data['weight'], user_data['height'], user_data['goals'])
        workout = Workout(user)
        diet = Diet(user)
        return render_template('workout.html', workout=workout, diet=diet)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)