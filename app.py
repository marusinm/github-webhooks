from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/webhook_handler', methods=['POST'])
def webhook_handler():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return 'JSON posted'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
