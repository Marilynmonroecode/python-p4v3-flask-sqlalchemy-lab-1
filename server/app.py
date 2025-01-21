#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Set up Flask-Migrate
migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# Add the view to get earthquake by ID
@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    # Query the database for the earthquake with the given ID
    earthquake = Earthquake.query.get(id)
    
    if earthquake:
        # If earthquake is found, return its attributes as JSON
        return jsonify({
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            'year': earthquake.year
        }), 200  # 200 OK status code
    else:
        # If no earthquake found, return an error message in JSON format
        return jsonify({
            'message': f'Earthquake {id} not found.'
        }), 404  # 404 Not Found status code


# Add the view to get earthquakes matching a minimum magnitude
@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    # Query the database for earthquakes with a magnitude greater than or equal to the given value
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Prepare the response data
    if earthquakes:
        # If earthquakes are found, return the count and list of earthquakes
        return jsonify({
            'count': len(earthquakes),
            'quakes': [{
                'id': quake.id,
                'location': quake.location,
                'magnitude': quake.magnitude,
                'year': quake.year
            } for quake in earthquakes]
        }), 200  # 200 OK status code
    else:
        # If no earthquakes match, return an empty list with a count of 0
        return jsonify({
            'count': 0,
            'quakes': []
        }), 200  # 200 OK status code, even though no earthquakes match


if __name__ == '__main__':
    app.run(port=5555, debug=True)
