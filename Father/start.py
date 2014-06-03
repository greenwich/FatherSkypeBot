__author__ = 'Alexey'

from father.father_app import Father
from father.common.constants import CommonConstants
import logging

if __name__ == '__main__':
    format = u"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format = format, filename = CommonConstants.LOG_FILE, level = logging.INFO)

    Father().serve()