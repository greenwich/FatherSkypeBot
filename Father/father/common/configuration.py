__author__ = 'Alexey'

import yaml

from father.common.constants import CommonConstants


class Configuration(object):

    @staticmethod
    def load():
        return yaml.load(open(CommonConstants.MESSAGES_FILE).read())
