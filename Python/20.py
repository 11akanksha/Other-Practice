import logging

logging.basicConfig(filename='random.log', level=logging.DEBUG)

logging.info('This is the information log')
print('Logged as info')
logging.debug('This is the debug log')
print('Logged as debug')
logging.error('This is the error log')
print('Logged as error')

#o/p:
INFO:root:This is the information log
DEBUG:root:This is the debug log
ERROR:root:This is the error log
