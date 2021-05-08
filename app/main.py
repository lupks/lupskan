import os
import json
import flask
import time

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, disconnect

import eventlet
eventlet.monkey_patch()

from app.blockchain import *

"""
Run Blockchain w/ scheduler
- Change epoch every minute
"""

blockchain = Blockchain()

with open('blockchain.json') as f:
    ledger = json.load(f)

"""
Flask App
"""
app = Flask(__name__, template_folder='templates', static_folder='templates/static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

# our global worker
workerObject = None
class Worker(object):
    def __init__(self, socketio):
        self.socketio = socketio

    def do_work(self):
        while True:
            index = blockchain.mine()

            if index is not False:
                self.socketio.emit("update", {"msg": f"{index}: {blockchain.chain[index]['hash']}"}, namespace="/work")
                self.socketio.emit("transaction", {"msg": list(blockchain.chain[index]['transactions'])}, namespace="/work")

                # important to use eventlet's sleep method
                eventlet.sleep(10)
            eventlet.sleep(10)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect', namespace='/work')
def connect():
    global worker
    worker = Worker(socketio)
    socketio.start_background_task(target=worker.do_work)

@app.route('/new_transaction', methods=['POST', 'GET'])
def transaction():
    transaction = request.args.get('msg')
    blockchain.add_new_transaction(transaction)

    return f"Transaction: {transaction}\n"
