from flask import Flask, render_template, request

import requests

import json

app = Flask(__name__)


def get_repos(username):
    # All URLs for the GitHub API start with "https://api.github.com/"
    url = "https://api.github.com/users/" + username + "/repos"
    response = requests.get(url)  # Use the requests library to contact GitHub
    return json.loads(response.content)  # Parse content returned by the API


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/repos')
def repos():
    print request.form
    context = {  # This will be passed into the template
        'username': request.args['username'],
        'repos': get_repos(request.args['username']),
    }
    return render_template('repos.html', **context)


if __name__ == '__main__':
    app.run(debug=True)  # debug=True shows error messages in browser
