import os
import flask
from flask import Flask, request, render_template
from apscheduler.schedulers.background import BackgroundScheduler

from app.blockchain import *

"""
Run Blockchain w/ scheduler
- Change epoch every hour
"""


def new_epoch():
    blockchain.mine()

    chain_data = []
    print(blockchain.chain[-1].__dict__)
    # for block in blockchain.chain:
    #     chain_data.append(block.__dict__)
    # print({"length": len(chain_data), "chain": chain_data[-1]})


sched = BackgroundScheduler(daemon=True)
sched.add_job(new_epoch, 'interval', seconds=60)
sched.start()

"""
Flask App
"""
app = Flask(__name__, template_folder='templates', static_folder='templates/static')
blockchain = Blockchain()



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send")
def send():
    return render_template("send.html")

@app.route("/receive")
def receive():
    return render_template("receive.html")

@app.route('/transaction', methods=['GET', 'POST'])
def get_divinfo():
    new_transaction = request.form.to_dict()
    print(new_transaction)
    blockchain.add_new_transaction(new_transaction)
    return flask.jsonify({"result":f'ok'})


# app.run(debug=True, port=5004)
