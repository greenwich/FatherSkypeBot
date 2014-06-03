__author__ = 'Alexey'

import Skype4Py
from father.common.constants import CommonConstants

class SkypeConnection(object):

    def __init__(self, config):
        self._connection = None
        self._config = config

    def connect(self):
        self._connection = Skype4Py.Skype()
        self._connection.Attach()
        return self

    def add_event_handlers(self, handlers):
        for handler in handlers.keys():
            self._connection.__setattr__(handler, handlers[handler])

    def get_current_chat(self):
        chat = self._connection.Chat(Name = self._config[CommonConstants.ADMINISTRATION_TAG][CommonConstants.CHAT_ID_KEY])
        return Chat(chat)

class Chat(object):

    def __init__(self, chat):
        self._chat = chat
        self._name = chat.Name

    def get_chat_name(self):
        return self._name

    def send_message(self, message):
        self._chat.SendMessage(message)

    def get_all_messages(self):
        return {message.Id: ChatMessage(message.Body, message.Id, message.FromDisplayName) for message in self._chat.Messages}

class ChatMessage(object):
    def __init__(self, text, id, from_display_name, chat_name, status):
        self.text = text
        self.id = id
        self.from_display_name = from_display_name
        self.chat_name = chat_name
        self.status = status

