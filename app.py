"""The main application module with create_app(), resources and error handlers."""
import sys
from flask import Flask
from flask import jsonify
from flask_essentials import database
from configuration.command_line_arguments import get_command_line_parser
from configuration.command_line_arguments import add_arguments
from configuration.command_line_arguments import parse_args
from resources.splash import Splash
from errors.APIErrors import BadRequestError

from flask_restful import Api


def create_app():
    """The application factory."""

    app = Flask('flask_web')
    database.init_app(app)
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

    return app


flask_web = create_app()


if __name__ == '__main__':
    PARSER = get_command_line_parser()
    add_arguments(PARSER)
    ARGS = parse_args(PARSER, sys.argv[1:])
    flask_web.run(ARGS['host'], ARGS['port'], ARGS['debug'])


