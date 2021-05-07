from app.main import app, socketio
import os

if __name__ == "__main__":
    socketio.run(app, debug=True)

