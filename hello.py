# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! - RK updatenew2'

if __name__ == '__main__':
    app.run()

