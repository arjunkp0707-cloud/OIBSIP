from flask import Flask
from flask_socketio import SocketIO

from database import init_database


app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-later"

socketio = SocketIO(app)


@app.route("/")
def index():
    return "Chat Application is running!"


if __name__ == "__main__":
    init_database()
    socketio.run(app, debug=True)