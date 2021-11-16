import time
import json
from server import db, features
from flask import Flask, request, jsonify

app = Flask(__name__)

triggers = db.triggers()
triggers.create_triggers_table()
users = db.users()
users.create_user_table()

@app.route('/' ,methods=['GET'])
def response_get():
    return jsonify({'status':'OK'})

@app.route('/triggers' ,methods=['POST'])
def response():

    if not request.json:
        abort(400)

    else:
        name = request.json['name']
        message = request.json['message']
        device_mac = request.json['device_mac']
        response = triggers.trigger_data_entry(device_mac,name,message)
        if response:
            features.features.send_message(name,message,device_mac)
            return jsonify({'response': True})
        else:
            return jsonify({'response': False})

@app.route('/users', methods=['GET'])
def users_response_get():
    response = users.read_users_data()
    json_data = []
    for result in response:
        data = {"name":result[0],
                "lastname":result[1],
                "username":result[2],
                "passwd":result[3],
                "chat_id":result[4],
                "device_mac":result[5],
                "fecha":result[6]}
        json_data.append(data)
    return jsonify(json_data)

@app.route('/users', methods=['POST'])
def users_response():
    if not request.json:
        abort(400)

    else:
        name = request.json['name']
        lastname = request.json['lastname']
        username = request.json['username']
        passwd = request.json['passwd']
        chat_id = request.json['chat_id']
        device_mac = request.json['device_mac']

        if None:
            return jsonify({'Response':  False})        
        else:
            users.user_data_entry(name,lastname,username,passwd,device_mac,chat_id)
            return jsonify({'Response': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)