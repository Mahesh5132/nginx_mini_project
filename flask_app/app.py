from flask import Flask

app = Flask(__name__)

@app.route('/flask')
def home():
    return "Hello from Flask App!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
