#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template, jsonify
import uuid

app = Flask(__name__)

@app.route('/101-hbnb', methods=['GET', 'POST'])
def hbnb_101():
    """ Method render a HTML template """
    if request.method == 'POST':
        amenities = request.form.getlist('amenities')
        states = request.form.getlist('states')
        cities = request.form.getlist('cities')
        places = storage.all('Place')
        reviews = get_reviews()  # Assume you have a function to get reviews
        return render_template('101-hbnb.html', amenities=amenities, states=states, cities=cities, places=places, reviews=reviews)
    amenities = storage.all('Amenity').values()
    states = storage.all('State').values()
    cities = storage.all('City').values()
    places = storage.all('Place')
    reviews = get_reviews()  # Assume you have a function to get reviews
    return render_template('101-hbnb.html', amenities=amenities, states=states, cities=cities, places=places, reviews=reviews)

@app.route('/get_reviews', methods=['GET'])
def get_reviews():
    """ Get reviews """
    # Logic to fetch reviews, assuming you have a function for this
    reviews = ["Review 1", "Review 2", "Review 3"]  # Example list of reviews
    return jsonify(reviews)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)