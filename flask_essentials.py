"""Create application instantiations of SQLAlchemy and Marshmallow, synchronizing sessions."""
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
marshmallow = Marshmallow()
