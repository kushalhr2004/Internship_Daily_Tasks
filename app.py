from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

app = Flask(__name__)
# A secret key to use optional features like flash messages safely.
app.secret_key = 'some_secret_key'

# ✅ Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=3306
    )

# ✅ Create Table
def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database Initialization Error (it may not exist yet, or incorrect credentials): {e}")

# Initialize DB on startup
init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            conn = get_db_connection()
            cursor = conn.cursor()

            query = "INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)"
            values = (name, email, message)

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            return render_template("add_feedback.html", success=True)
        except Exception as e:
            return f"Error: {str(e)}"
            
    return render_template("add_feedback.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)