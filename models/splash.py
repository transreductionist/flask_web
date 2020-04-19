"""The model for the splash screen."""

from flask_essentials import database


class SplashModel(database.Model):
    """Splash attributes."""

    __tablename__ = 'splash'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = database.Column(database.VARCHAR(36), nullable=True, default='')
    last_name = database.Column(database.VARCHAR(36), nullable=True, default='')
