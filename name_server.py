from generator import givebacknames
import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/name_gen')
def giveNames():
    name = request.args.get('num', default = 12)
    data = givebacknames(name)
    return_data = json.dumps(data)
    return return_data


if __name__ == "__main__":
    app.run()