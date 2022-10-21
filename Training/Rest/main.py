"""
Simple REST API to test service mesh functionality.
"""
from flask import Flask
import os
import json
import requests

app = Flask(__name__)

def get_env():
    info = {}
    info['app_name'] = os.getenv('APP_NAME')
    info['version'] = os.getenv('VERSION')
    info['namespace'] = os.getenv('NAMESPACE')
    info['pod'] = os.getenv('POD')
    info['node'] = os.getenv('NODE')
    return info

def configure_routes(app, info):
    @app.route("/")
    def hello_world():
        return f"Hello from {info['app_name']}"

    @app.route("/info")
    def get_info():
        info = {}
        info['app_name'] = os.getenv('APP_NAME')
        info['version'] = os.getenv('VERSION')
        info['namespace'] = os.getenv('NAMESPACE')
        info['pod'] = os.getenv('POD')
        info['node'] = os.getenv('NODE')
        return json.dumps(info)

    connect_url = os.getenv('CONNECT_URL')

    @app.route("/connect")
    def connect():
        response = {}
        response['action'] = f"Connecting from {info['app_name']} to {connect_url}"
        try:
            r = requests.get(url = connect_url)
            response['response'] = str(r.content)
            response['code'] = r.status_code
        except requests.exceptions.ConnectionError as e:
            response['error'] = str(e.args[0].reason)
        return json.dumps(response)

configure_routes(app, get_env())

if __name__ == '__main__':
    app.run()