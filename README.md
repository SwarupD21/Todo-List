# ✅ Django To-Do List Application

A modern **To-Do List web application** built using **Django**, featuring a clean UI, authentication system, and full task management (Create, Update, Complete, Delete).  
Designed with a **premium gradient theme**, **glass-style cards**, and **responsive layout**.

---

## 🚀 Features

- 🔐 User Authentication (Login / Register / Logout)
- 🏠 Beautiful Home Page (Landing UI)
- 📝 Create Tasks with Title & Description
- ✏️ Update Existing Tasks
- ✅ Mark Tasks as Complete / Undo
- 🗑️ Delete Tasks
- 🎨 Premium UI (Gradient background + Glass cards)
- 📱 Fully Responsive Design
- ⚡ Fast & Simple User Experience

---

## 🗂️ Project Structure

TO DO LIST/  
│  
├── todo/ # Django project settings  
│ ├── settings.py  
│ ├── urls.py  
│ ├── wsgi.py  
│ └── asgi.py  
│  
├── list/ # Main app  
│ ├── migrations/  
│ ├── templates/  
│ │ ├── home.html  
│ │ ├── login.html  
│ │ ├── register.html  
│ │ ├── taskform.html  
│ │ └── update_taskform.html  
│ ├── views.py  
│ ├── urls.py  
│ └── models.py  
│  
├── static    
├── templates/  
│ └── layout.html # Base template  
│  
├── db.sqlite3  
├── manage.py  
└── README.md  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Auth:** Django Authentication System

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/todo-django.git
cd todo-django
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
``` 
### 3️⃣ Install Dependencies
```bash
pip install django
```
### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Run Server
```bash
python manage.py runserver
```
# 👨‍💻 Developed By
Swarup Dash  
B.Tech IT — VSSUT Burla  
  
