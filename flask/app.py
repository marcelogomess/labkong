import os
import platform
from time import sleep
from flask import Flask, abort, url_for, json, jsonify, Response
import json

app = Flask(__name__,template_folder='.')

os_data = {"System": platform.uname()[0], "Version": platform.uname()[3], "Hostname":platform.node()}

@app.route("/", methods=['GET',])
def index():
    return jsonify(os_data)


@app.route("/delay", methods=['GET'])
def delay():
    sleep(10)
    return jsonify(os_data)


@app.route("/bugado", methods=['GET'])
def bugado():
    return Response(json.dumps(os_data), status=300, mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')