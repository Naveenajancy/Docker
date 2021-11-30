from flask import Flask
import uuid
app = Flask(__name__)

id = uuid.uuid4()

@app.route("/")
def hello():
    return "Hello from Python! {}".format(id)

@app.route("/welcome")
def welcome():
    return "Hello-welcome from desam! {}".format(id)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
