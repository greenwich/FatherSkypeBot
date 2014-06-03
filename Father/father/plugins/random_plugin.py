# -*- coding: utf-8 -*-
__author__ = 'Alexey'

from father.plugin_manager import Plugin
from father.plugins.libs.messages import MessagesProcessor

class RandomAnswerPlugin(Plugin):
    message_pattern = u'(?i)(.|\r|\n)*(father|отец).*'
    order = 0

    def execute(self, message, name, config):
        mp = MessagesProcessor(config)
        mp.parse()
        return u'{0}: {1}'.format(name, mp.get_random_message())






