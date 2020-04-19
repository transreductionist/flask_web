"""The Resource entry point for the splash page."""
from controllers.splash import get_splash
from schemas.splash import SplashSchema
from flask_restful import Resource


class Splash(Resource):
    """Resource endpoint for the splash endpoint."""

    @staticmethod
    def get():
        splash = get_splash()
        schema = SplashSchema()
        result = schema.dump(splash)
        return result
