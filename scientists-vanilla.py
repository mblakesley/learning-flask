from flask import Flask, request, jsonify
from markupsafe import escape

app = Flask(__name__)
scientist_list = [
    {
        'name': 'einstein',
        'field': 'physics',
    },
    {
        'name': 'darwin',
        'field': 'biology',
    }
]


@app.route('/scientists')
def get_scientists():
    return jsonify(scientist_list)


@app.route('/scientists', methods=['POST'])
def post_scientists():
    new_sci_dict = request.get_json()
    scientist_list.append(new_sci_dict)
    return jsonify(new_sci_dict)


@app.route('/scientists/<string:scientist_name>')
def get_scientist(scientist_name):
    for sci_dict in scientist_list:
        if sci_dict['name'] == scientist_name:
            return jsonify(sci_dict)
    return 'YOU OUTTA LUCK, SON!'
