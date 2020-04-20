"""Build application configuration."""
import importlib
import os


def set_flask_web_configuration(env_prefix):
    """Set the configuration using the project YAML and environment variables."""
    importlib.import_module('configuration')
    configuration_module = importlib.import_module('.configuration_loader', package='configuration')
    configuration = configuration_module.ConfigLoader()

    configuration_directory = os.path.join(os.path.dirname(__file__), 'configuration')
    yml_filename = 'flask_web.yml'
    yml_full_file_path = os.path.join(configuration_directory, yml_filename)
    configuration.update_from_yaml_file(yml_full_file_path)
    configuration.update_from_env_variables(env_prefix)
    return configuration
