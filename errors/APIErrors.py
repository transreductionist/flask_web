"""Exception handlers for the API request errors."""


class RequestError(Exception):
    """Base class for some custom exceptions for the API requests."""


class BadRequestError(RequestError):
    """Exception to handle a bad request error."""

    def __init__(self):
        super().__init__()
        self.message = 'A status code of 400 was returned.'
