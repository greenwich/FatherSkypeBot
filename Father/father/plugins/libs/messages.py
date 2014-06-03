__author__ = 'Alexey'

import random

from father.common.constants import CommonConstants


class Message(object):
    """
    Class represents message that will be posted/checked in the chat
    """

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return unicode(self._message)

class Wisdom(Message):
    pass

class MessagesProcessor(object):

    def __init__(self, config):
        self._wisdoms = None
        self._config = config

    def parse(self):
        self._wisdoms = [Wisdom(message) for message in self._config
        ['wisdoms']]

    def get_all_messages(self):
        return self._wisdoms

    def get_random_message(self):
        if len(self._wisdoms) > 0:
            return self._wisdoms[
                random.randrange(0, len(self._wisdoms))]
        raise Exception("Messages list is empty")
