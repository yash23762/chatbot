from flask import Flask, render_template, request

app = Flask(__name__)


# ------------------------------------Chatbot------------------------------------------------
import random
import time

user_query = {"greeting": ["hi", "hello","hey","hlw"],
              "bit" : ["tell me something about bit", "what is bit", "bit"],
              'branches':["tell me about branches in bit", "engineering branches in bit"]
}


bot_reply = {"greeting":["hi", "hello","hey","hlw"],
        "bit":[ "Birla institute of Technology","Birla institute of Technology, Mesra", "Birla institute of Technology, Jaipur"],
        "branches":["CS/ECE/EEE","Computer Science", "ECE"],
        "default":["Sorry! I didn't understand. Please repeat."]
        }


def intent_match(user_msg): 
    for intent, entity in user_query.items():
        if(user_msg.lower() in entity):
            return intent
    return "default"


def respond(user_msg):
    intent = intent_match(user_msg)
    return random.choice( bot_reply[intent] )   

def get_response(user_msg):
    bot_msg = ""
    #user_msg = ""
    while(1):
        if(user_msg == "get out"):
            return "Bye. Nice to talk."
            break
        bot_msg = respond(user_msg)
        #time.sleep(5)
        return bot_msg
        



# ------------------------------------Flask App -------------------------------------

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/get')
def Chatbot():
    user_msg = request.args.get('msg')
    bot_reply  = str(get_response(user_msg))
    return bot_reply

if __name__=="__main__":
    app.run()
