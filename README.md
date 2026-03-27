# 🚀 Flask To-Do App (No Database)

A modern, minimal, and user-friendly **To-Do List Web Application** built using **Flask (Python)** with a clean UI and file-based storage (JSON).

This project is perfect for **beginners, BTech students, and mini projects** — no SQL database required.

---

## ✨ Features

* 🔐 User Authentication (Login / Signup)
* 📝 Add Tasks
* ✅ Mark Tasks as Completed
* ❌ Delete Tasks
* 👤 User-specific task management
* 💾 JSON-based storage (No MySQL / SQLite)
* 🎨 Modern UI (Glassmorphism + Dark Theme)
* ⚡ Fast and lightweight

---

## 📁 Project Structure

```
flask_todo_project/
│── app.py
│── users.json
│── tasks.json
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
```

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Authentication:** Flask-Login
* **Security:** Werkzeug (Password Hashing)
* **Storage:** JSON (File-based)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/flask-todo-app.git
cd flask-todo-app
```

---

### 2️⃣ Install Dependencies

```
pip install Flask Flask-Login Werkzeug
```

---

### 3️⃣ Run the App

```
python app.py
```

---

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📸 Screens

* 🏠 Home Page
* 🔐 Login / Signup Page
* 📊 Dashboard (To-Do List)

---

## 🧠 How It Works

* User data is stored in `users.json`
* Task data is stored in `tasks.json`
* Each task is linked to a specific user using `user_id`
* Passwords are securely hashed using Werkzeug
* Flask handles routing and rendering templates

---

## 🎯 Use Cases

* 📚 Academic Mini Project (BTech / Diploma)
* 💡 Flask Practice Project
* 🧪 Learning Authentication System
* 🛠️ Beginner Full-Stack App

---

## 🔒 Security Notes

* Passwords are hashed (not stored in plain text)
* User sessions handled using Flask-Login
* No external database → simple but less scalable

---

## 🚀 Future Improvements

* ✏️ Edit Task
* ⏰ Deadline & Reminder System
* 🌙 Dark/Light Mode Toggle
* 📱 Fully Responsive UI (Bootstrap/Tailwind)
* ☁️ Deployment (Render / PythonAnywhere)
* 🔔 Notifications

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and improve the project.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Ashish Tabiyad**
BTech CSE Student

---

## ⭐ Support

If you like this project, please ⭐ star the repository and share it!
