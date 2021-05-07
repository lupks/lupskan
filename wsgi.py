from app.main import app, socketio
import os

if __name__ == "__main__":
    socketio.run(app, debug=True)

# if __name__ == "__main__":
#     socketio.run(app, debug=True, port=int(os.environ.get('PORT', '5000')))


