#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
import uuid

app = Flask(__name__)

@app.route('/4-hbnb/')
def hbnb():
    cache_id = uuid.uuid4()
    try:
        return render_template('4-hbnb.html', cache_id=cache_id)
    except FileNotFoundError:
        return render_template('8-hbnb.html', cache_id=cache_id)

@app.route('/100-hbnb', methods=['GET', 'POST'])
def hbnb_100():
    """ Method render a HTML template """
    if request.method == 'POST':
        amenities = request.form.getlist('amenities')
        states = request.form.getlist('states')
        cities = request.form.getlist('cities')
        places = storage.all('Place')
        return render_template('100-hbnb.html', amenities=amenities, states=states, cities=cities, places=places)
    amenities = storage.all('Amenity').values()
    states = storage.all('State').values()
    cities = storage.all('City').values()
    places = storage.all('Place')
    return render_template('100-hbnb.html', amenities=amenities, states=states, cities=cities, places=places)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
