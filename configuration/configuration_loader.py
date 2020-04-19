# -*- coding: utf-8 -*-
"""A general configuration magazine_loader that processes environment variables and files: extendable."""
import logging
import os
import yaml
from errors.configuration_loader_errors import ConfigurationLoadingError
from errors.configuration_loader_errors import ConfigurationFileNonExistentError
DictType = dict


class ConfigLoader(DictType):
    """The class that handles the loading of configurations from multiple sources."""

    def update_from_yaml_file(self, file_path, additional_dict=None):
        """Function to do the update given a YAML file."

        :param (str) file_path: The full file path the YAML file.
        :param (dict) additional_dict: update from YAML as well as the dictionary: configuration.
        :return (bool): result of call
        """
        if os.path.exists(file_path):
            try:
                with open(file_path) as file_obj:
                    yaml_conf = yaml.safe_load(file_obj)
                    if additional_dict:
                        self.update(additional_dict)
                    self.update(yaml_conf)
            except IOError as error:
                logging.debug(str(error))
                raise ConfigurationLoadingError(str(error))
        else:
            logging.debug('file non-existent: %s', file_path)
            raise ConfigurationFileNonExistentError('File does not exist: {}'.format(file_path))
        return True

    def update_from_env_variables(self, env_prefix):
        """A funtion to handle tagged environment variables.

        :param (str) env_prefix: Prefix to tagged environment variable, e.g. DEV in DEV_SECRET_KEY.
        :return (bool): result of call
        """
        self.update(ConfigLoader(os.environ).get_env_variables(env_prefix))
        return True

    @staticmethod
    def get_env_variables(env_prefix):
        """A function to get the tagged environment variables from the environment (os.environ).

        :param (str) env_prefix: Prefix to tagged environment variable, e.g. DEV in DEV_SECRET_KEY.
        :return (ConfigLoader): The tagged dictionary of environment variables with the tag stripped off.
        """
        prefix = env_prefix.rstrip('_') + '_'
        tagged_dict = {}
        for environment_key, environment_value in os.environ.items():
            if environment_key[:len(prefix)] == prefix:
                tagged_dict[environment_key[len(prefix):]] = environment_value
        return ConfigLoader(tagged_dict)

    def add_configuration_from_dict(self, additional_configuration):
        """Add an additional configuration dictionary to the current config.

        :param (dict) additional_configuration: new configuration
        """
        if additional_configuration:
            self.update(additional_configuration)
