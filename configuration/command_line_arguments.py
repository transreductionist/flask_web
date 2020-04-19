"""Parse the command line arguments."""
import textwrap
import argparse


def get_command_line_parser():
    """Get an argument parser.

    :return (obj): instantiated parser
    """

    parser = argparse.ArgumentParser(description='Flask application server parameters.')
    return parser


def parse_args(parser, arguments):
    """Given the sys.argv return parsed arguments.

    :param (obj) parser: instantiated parser
    :param (list) arguments: sys.argv, or a list of arguments from the command line.
    :return (dict): Namespace arguments as normalized dictionary.
    """
    parsed_arguments = parser.parse_args(arguments)
    arguments = dict()
    argument_keys = list(vars(parsed_arguments).keys())
    for arg_key in argument_keys:
        arg_value = getattr(parsed_arguments, arg_key)
        nomalized_arg_value = normalize_argument_value(arg_value)
        arguments[arg_key] = nomalized_arg_value
    return arguments


def normalize_argument_value(arg_value):
    """Normalize the namespace argument to Python built-in types.

    :param (obj) arg_value: a namespace key value.
    :return (obj): the Python builtin type
    """
    if arg_value in ['True', 'False']:
        if arg_value == 'False':
            return False
        return True
    elif arg_value.isdigit():
        if '.' not in arg_value:
            return int(arg_value)
        else:
            return float(arg_value)
    elif arg_value == 'None':
        return None
    else:
        return arg_value


def add_arguments(parser):
    """Add arguments to the parser.

    :param (obj) parser: an instantiated parser.
    """

    text = '''The host for the app server.'''
    parser.add_argument(
        '--host',
        default='127.0.0.1',
        action='store',
        nargs='?',
        help=textwrap.dedent(text),
    )

    text = '''The port for the server.'''
    parser.add_argument(
        '--port',
        default='5000',
        action='store',
        nargs='?',
        help=textwrap.dedent(text),
    )

    text = '''Start in debug mode.'''
    parser.add_argument(
        '--debug',
        default='True',
        action='store',
        nargs='?',
        help=textwrap.dedent(text),
    )
