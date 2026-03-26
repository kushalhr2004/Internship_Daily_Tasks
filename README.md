# 🌐 Flask Feedback Mini Project

## 📌 Project Overview

This is a **Flask-based web application** built to understand the fundamentals of full-stack development, including backend logic, frontend templating, and database integration using **Python, HTML, CSS, and MySQL**.

The project demonstrates how to:
* Create a Flask application and handle routes
* Use HTML templates with Jinja2 (`render_template`)
* Connect to a MySQL database and manage tables
* Process form submissions (POST requests)
* Keep sensitive configuration safe using environment variables (`.env`)

---

## 🚀 Features

* 🏠 **Home Page** (`/`) - Simple landing page.
* ℹ️ **About Page** (`/about`) - Information about the app.
* 📝 **Add Feedback** (`/add`) - A form to submit user feedback (Name, Email, Message), which is stored securely in a MySQL database.
* 🗄️ **Auto Database Initialization** - The app automatically creates the necessary `feedback` table upon startup if it doesn't exist.
* 🔒 **Secure Configuration** - Database credentials managed via a `.env` file configuration using `python-dotenv`.

---

## 🛠️ Technologies Used

* **Backend:** Python (Flask)
* **Frontend:** HTML5, CSS3, Jinja2
* **Database:** MySQL (`mysql-connector-python`)
* **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```
Task-2/
│
├── .env                 # Environment variables (DB credentials)
├── app.py               # Main Flask application file
├── config.py            # Optional configuration
│
├── templates/           # HTML templates
│   ├── home.html
│   ├── about.html
│   └── add_feedback.html
│
└── static/              # Static files (CSS, JS, Images)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kushalhr2004/Internship_Daily_Tasks.git
cd Internship_Daily_Tasks/Task-2
```

### 2️⃣ Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install Dependencies

You'll need Flask, MySQL Connector, and python-dotenv.

```bash
pip install flask mysql-connector-python python-dotenv
```

### 4️⃣ Configure the Environment

Create a `.env` file in the root of the project folder (if not already present) and configure your database credentials:

```ini
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
```
*(Make sure to create the database `your_database_name` in your MySQL server beforehand!)*

### 5️⃣ Run the Application

```bash
python app.py
```

### 6️⃣ Open in Browser

Access the application at:
```
http://127.0.0.1:5000/
```

---

## 📚 What I Learned

* Connecting Flask applications to a MySQL database using `mysql.connector`.
* Creating custom database initialization logic that runs whenever the server starts.
* Processing user inputs safely from an HTML form and executing `INSERT` queries.
* Hiding sensitive database credentials effectively using `python-dotenv`.
* Building resilient user interfaces that handle success states (like "Feedback submitted").

---

## 👨‍💻 Author

**Kushal HR**

---

⭐ If you like this project, give it a star on GitHub!
