__author__ = 'Alexey'

import logging
import os
import types
import re
from father.common.constants import CommonConstants

_plugins = {}

class Plugin(object):

    message_pattern = None
    plugin_name = None
    order = None

    @classmethod
    def register(cls):
        if cls.__name__ in _plugins:
            raise PluginException("Plugin with the name {0} has already been loaded".format(cls.__name__))

        if cls.order is None:
            raise PluginException("Plugin {0} execution order is unknown".format(cls.__name__))

        _plugins[str(cls.order) + cls.__name__] = cls

    def execute(self, *args, **kwargs):
        raise NotImplementedError

class PluginException(Exception):
    pass

class PluginManager(object):

    def __init__(self, plugins_dir):
        self._plugins_dir = plugins_dir
        self._logger = logging.getLogger(self.__class__.__name__)

    def load(self):
        files = os.listdir(self._plugins_dir)
        for file in files:
            if file not in ['__init__.py'] and file.endswith('.py'):

                module = __import__('{0}.{1}'.format(os.path.basename(self._plugins_dir), file[:-3]),
                                    globals(),
                                    locals(),
                                    self._plugins_dir)

                for local_argument_name in module.__dict__:
                    local_argument_instance = module.__dict__[local_argument_name]

                    if type(local_argument_instance) == types.TypeType \
                            and issubclass(local_argument_instance, Plugin) \
                            and local_argument_instance.__name__ != Plugin.__name__:
                        local_argument_instance.register()
                        break

    def run(self, message, user_name, config):
        for plugin in _plugins.values():

            message = message[:256]
            if plugin.message_pattern is not None \
                    and re.match(plugin.message_pattern, message, re.IGNORECASE):
                self._logger.info(u'Run the plugin: {0}, user: {1}'.format(plugin, user_name))
                return plugin().__getattribute__('execute')(message, unicode(user_name),
                                                            PluginContext.get(config, plugin))

    def get_plugins_dict(self):
        return _plugins

class PluginContext(object):

    @staticmethod
    def get(config, plugin):
        """
        Returns plugins context settings from config.yaml.
        See both random_plugin section in config.yaml and random_plugin
        """
        return config[CommonConstants.PLUGINS_TAG][plugin.__name__]
