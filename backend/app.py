from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():

    config_message = os.getenv("APP_MESSAGE", "Default Message")
    secret_message = os.getenv("SECRET_MESSAGE", "No Secret")

    return f"{config_message} | {secret_message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)