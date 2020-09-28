from flask import Flask
import json

app = Flask(__name__)


class MyValue:
    def __init__(self):
        self.value_number = 0

    def return_json(self):
        return json.dumps({"value": self.value_number})

    def change_value(self, change_by_amount):
        self.value_number += change_by_amount
        return self.return_json()


my_value = MyValue()


@app.route('/', methods=['GET'])
def index():
    return my_value.return_json()


@app.route('/inc', methods=['PUT'])
@app.route('/inc/<int:value>', methods=['PUT'])
def inc(value=1):
    return my_value.change_value(value)


@app.route('/dec', methods=['PUT'])
@app.route('/dec/<int:value>', methods=['PUT'])
def dec(value=1):
    return my_value.change_value(int(value * -1))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
