"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request, redirect, jsonify
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


@app.route('/api', methods=['POST'])

def api():
    matchid = request.args['matchid']
    inning = request.args['inning']
    total_runs = request.args['total_runs']
    score_target = request.args['score_target']
    over = request.args['over']
    wickets = request.args['wickets']
    matchid = request.args['matchid']

    return jsonify ({'result' : 'Success!'})

@app.route('/json', methods=['POST'])
def json():
    return "Really", 200


# Reading the json and parsing it
# Parsed arg must be the input for the odds.py file 
# return Success


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
