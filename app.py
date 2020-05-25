import logging
logging.basicConfig(
    format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=u'mylog.log')

logging.debug('This is a debug message')
# Сообщение информационное
logging.info('This is an info message')
# Сообщение предупреждение
logging.warning('This is a warning')
# Сообщение ошибки
logging.error('This is an error message')
# Сообщение критическое
logging.critical('FATAL!!!')
