#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
import uuid

app = Flask(__name__)

@app.route('/3-hbnb/')
def hbnb():
    cache_id = uuid.uuid4()
    try:
        return render_template('3-hbnb.html', cache_id=cache_id)
    except FileNotFoundError:
        return render_template('8-hbnb.html', cache_id=cache_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
