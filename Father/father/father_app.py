__author__ = 'Alexey'

from father.chat import SkypeConnection,ChatMessage
from father.common.configuration import Configuration
from father.plugin_manager import PluginManager
from father.common.constants import CommonConstants
import logging
import time


class Father(object):

    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        config = Configuration.load()
        connection = SkypeConnection(config).connect()
        self._chat = connection.get_current_chat()

        connection.add_event_handlers({'OnMessageStatus': MessageHandler(config, self._chat).handle})

    def serve(self):
            self._logger.info('Connected to skype, chat: {0} at {1}'.format(self._chat.get_chat_name(), self._chat))
            raw_input("Press Enter to exit")

class MessageHandler(object):

    def __init__(self, config, chat):
        self._plugin_mgr = PluginManager(CommonConstants.PLUGINS_DIR)
        self._plugin_mgr.load()
        self._config = config
        self._logger = logging.getLogger(self.__class__.__name__)
        self._chat = chat

    def handle(self, message, status):
        if status == 'RECEIVED' and message.ChatName == self._chat.get_chat_name():
            chat_message = ChatMessage(message.Body, message.Id, message.FromDisplayName, message.ChatName, status)
            self._logger.info("Event processing started for message {0}".format(chat_message.id))
            try:
                answer = self._plugin_mgr.run(chat_message.text, chat_message.from_display_name, self._config)
                if answer is not None:
                    self._chat.send_message(answer)
            except:
                logging.exception("Got exception")
            self._logger.info("Event processing finished for message {0}".format(chat_message.id))