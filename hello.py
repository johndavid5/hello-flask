from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    sWho = 'hello_world'
    print("%s: I'll be back, Bennett!"%(sWho))
    print("%s: Let off some steam, Bennett!"%(sWho))
    return 'Hello, World!'
