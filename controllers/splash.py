"""Controller for splash page."""
from models.splash import SplashModel
from flask_essentials import database


def get_splash():
    """The splash controller.

    :return (int) response: the response.
    """

    all_peters = database.session.query(SplashModel).filter_by(last_name='peters').all()
    return 200
