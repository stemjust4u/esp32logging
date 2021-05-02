'''
https://github.com/peterhinch
'''
import ulogging

'''
CRITICAL = 50
ERROR    = 40
WARNING  = 30
INFO     = 20
DEBUG    = 10
NOTSET   = 0
'''
a = "test"

ulogging.basicConfig(level=10)

ulogging.info('root logger info: {0}'.format(a))
ulogging.debug('root logger debugging')

logger = ulogging.getLogger(__name__)
logger.setLevel(10)
logger.info('logger info: {0}'.format(a))
logger.debug('logger debug')