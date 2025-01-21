from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Metadata and DB initialization
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Define the Earthquake model
class Earthquake(db.Model, SerializerMixin):
    # Define the table name in the database
    __tablename__ = 'earthquakes'

    # Define columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    magnitude = db.Column(db.Float)  # Magnitude of the earthquake (float)
    location = db.Column(db.String)  # Location of the earthquake (string)
    year = db.Column(db.Integer)  # Year of the earthquake (integer)

    def __repr__(self):
        # String representation of the Earthquake object
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"

# Add any other models here if needed

