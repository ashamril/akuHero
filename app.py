from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    print("Handling request to home page.")
    return "Hello Beautiful World! This is a test!"

if __name__ == '__main__':
    app.run()

