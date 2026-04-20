from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/db")
def db():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            dbname="postgres"
        )
        return "DB connection successful!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
