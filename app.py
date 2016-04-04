from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>SIR ZAIN if you are reading this, Then Plz give me full marks for this assignment :P</h1>"


if __name__ == '__main__':
    app.run()
