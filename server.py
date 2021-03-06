import time
import os
import telepot
from flask import Flask, request, jsonify

app = Flask(__name__)
bot = telepot.Bot(os.environ.get('API_KEY'))
chat_id_1 =  os.environ.get('MAIN_CHAT_ID')
chat_id_2 = os.environ.get('SECONDARY_CHAT_ID')

@app.route('/' ,methods=['GET'])
def response_get():
    return jsonify({'status':'OK'})

@app.route('/triggers' ,methods=['POST'])
def response():

    if not request.json:
        return jsonify({"error":"theres an error"})
    
    else:
        name = request.json['name']
        message = request.json['message']
        print("%s : %s" %(name,message))
        bot.sendMessage(chat_id_1, '%s : %s' %(name,message))
        bot.sendMessage(chat_id_2, '%s : %s' %(name,message))
        return jsonify({'status':'OK'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)