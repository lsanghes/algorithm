from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/ws', methods=['GET'])
def getAllEmp():
    return "Hello World Again!"

if __name__ == "__main__":
    app.run()

# http://127.0.0.1:5000/
# http://127.0.0.1:5000/ws
