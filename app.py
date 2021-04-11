from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    print("Handling request to home page.")
    return "Hello World! This is a test 12345!"

if __name__ == '__main__':
    app.run()

