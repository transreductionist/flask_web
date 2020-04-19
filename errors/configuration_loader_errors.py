"""Exceptions for the configuration loader."""


class ConfigurationError(Exception):
    """Base class for the configuration laoder."""


class ConfigurationLoadingError(ConfigurationError):
    """Exception to handle error in loading a YAML configuration file."""

    def __init__(self, msg):
        super().__init__()
        self.message = 'Problems loading the YAML configuration: {}'.format(msg)


class ConfigurationFileNonExistentError(ConfigurationError):
    """Handle YAML file not found error."""

    def __init__(self, msg):
        super().__init__()
        self.message = 'YAML file not found: {}'.format(msg)
