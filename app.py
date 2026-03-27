import json
import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

USER_FILE = 'users.json'
TASK_FILE = 'tasks.json'

# ---------- USER CLASS ----------
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# ---------- FILE FUNCTIONS ----------
def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

@login_manager.user_loader
def load_user(user_id):
    users = load_data(USER_FILE)
    for user in users:
        if user['id'] == int(user_id):
            return User(user['id'], user['username'], user['password'])
    return None

# ---------- ROUTES ----------

@app.route('/')
def index():
    return render_template('index.html')

# ---------- SIGNUP ----------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = load_data(USER_FILE)

        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        for user in users:
            if user['username'] == username:
                flash("User already exists!", "danger")
                return redirect(url_for('signup'))

        new_user = {
            "id": len(users) + 1,
            "username": username,
            "password": password
        }

        users.append(new_user)
        save_data(USER_FILE, users)

        flash("Account created!", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_data(USER_FILE)

        for user in users:
            if user['username'] == request.form['username'] and \
               check_password_hash(user['password'], request.form['password']):
                login_user(User(user['id'], user['username'], user['password']))
                return redirect(url_for('dashboard'))

        flash("Invalid credentials", "danger")

    return render_template('login.html')

# ---------- DASHBOARD (TODO LIST) ----------
@app.route('/dashboard')
@login_required
def dashboard():
    tasks = load_data(TASK_FILE)

    user_tasks = [t for t in tasks if t['user_id'] == current_user.id]

    return render_template('dashboard.html', tasks=user_tasks, name=current_user.username)

# ---------- ADD TASK ----------
@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
    tasks = load_data(TASK_FILE)

    new_task = {
        "id": len(tasks) + 1,
        "user_id": current_user.id,
        "task": request.form['task'],
        "done": False
    }

    tasks.append(new_task)
    save_data(TASK_FILE, tasks)

    return redirect(url_for('dashboard'))

# ---------- COMPLETE TASK ----------
@app.route('/complete/<int:task_id>')
@login_required
def complete(task_id):
    tasks = load_data(TASK_FILE)

    for task in tasks:
        if task['id'] == task_id and task['user_id'] == current_user.id:
            task['done'] = True

    save_data(TASK_FILE, tasks)
    return redirect(url_for('dashboard'))

# ---------- DELETE TASK ----------
@app.route('/delete/<int:task_id>')
@login_required
def delete(task_id):
    tasks = load_data(TASK_FILE)

    tasks = [t for t in tasks if not (t['id'] == task_id and t['user_id'] == current_user.id)]

    save_data(TASK_FILE, tasks)
    return redirect(url_for('dashboard'))

# ---------- LOGOUT ----------
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)