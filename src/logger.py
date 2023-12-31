# coding=utf-8

import sys
import logging

logging.getLogger('matplotlib').setLevel(logging.WARNING)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s] %(message)s',)
logger = logging.getLogger()
