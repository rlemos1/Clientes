from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

SERVER_URL = 'http://127.0.0.1:5000'

@app.route('/')
def index():
    response = requests.get(f'{SERVER_URL}/favorites?format=json')
    favorites = response.json() if response.status_code == 200 else []
    return render_template('index.html', favorites=favorites)

@app.route('/add', methods=['POST'])
def add_favorite():
    url = request.form.get('url')
    if url:
        response = requests.post(f'{SERVER_URL}/favorites?format=json', json={'url': url})
        if response.status_code == 200:
            return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5001, debug=True)
