from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'

# @app.route('/world')
# def helloWorld():
#     return 'Hello World'
# Test Comment

if __name__ == '__main__':
    app.run(host="0.0.0.0")
