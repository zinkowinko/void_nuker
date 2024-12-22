from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Void Nuke Bot is Online! Thanks for checking!"

port = 8080
print(f"Starting the server on port {port}...")
app.run(host="0.0.0.0", port=port)