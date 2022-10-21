from flask import Flask
import os
import json
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello from {os.getenv('APP_NAME')}"

@app.route("/info")
def get_info():
    info = {}
    info['appName'] = os.getenv('APP_NAME')
    info['version'] = os.getenv('VERSION')
    info['namespace'] = os.getenv('NAMESPACE')
    info['pod'] = os.getenv('POD')
    info['node'] = os.getenv('NODE')
    return json.dumps(info)

connect_url = os.getenv('CONNECT_URL')

@app.route("/connect")
def connect():
    response = {}
    response['action'] = f"Connecting from {os.getenv('APP_NAME')} to {connect_url}"
    try:
        r = requests.get(url = connect_url)
        response['response'] = str(r.content)
        response['code'] = r.status_code
    except requests.exceptions.ConnectionError as e:
        response['error'] = str(e.args[0].reason)
    return json.dumps(response)