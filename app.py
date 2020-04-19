"""The main application module with create_app(), resources and error handlers."""
import sys
from flask import Flask
from flask import jsonify
from configuration.command_line_arguments import get_command_line_parser
from configuration.command_line_arguments import add_arguments
from configuration.command_line_arguments import parse_args
from resources.splash import Splash
from errors.api_errors import BadRequestError
from errors.configuration_loader_errors import ConfigurationLoadingError
from app_helpers import set_flask_web_configuration
from flask_restful import Api
from flask_essentials import database


def create_app():
    """The application factory."""

    app = Flask('flask_web')
    set_flask_web_configuration('FLASK_WEB')

    database.init_db()

    api = Api(app)

    api.add_resource(Splash, '/')

    @app.errorhandler(BadRequestError)
    def handle_400(error):
        """HTTP status 400 (bad request) error handler.

         :param (obj) error: Error message raised by exception.
         :return (int) response: the response code
         """
        response = jsonify(error)
        response.status_code = 400
        return response

    @app.errorhandler(ConfigurationLoadingError)
    def handle_config_loading_errors(error):
        """Error handler for pronblems loading configuration.

         :param (obj) error: Error message raised by exception.
         :return (int) response: the response code
         """
        response = jsonify(error)
        response = 78
        return response

    return app


flask_web = create_app()


if __name__ == '__main__':
    PARSER = get_command_line_parser()
    add_arguments(PARSER)
    ARGS = parse_args(PARSER, sys.argv[1:])
    flask_web.run(ARGS['host'], ARGS['port'], ARGS['debug'])


