# -*- coding: utf-8 -*-

# import logging
# try:
# 	import settings
# except Exception as e:
# 	print "Exception: {}".format(e)
# 	from django.conf import settings
#
# __all__ = []
#
# _DEFAULT_PASSWORD_LENGTH = 32
#
# _DEFAULTS = {
# 	'DEFAULT_GATEWAY_HOST': 'http://api.weapp.com',
# 	# 开启API Auth授权。若不开启，则不加载相应的model
# 	'ENABLE_API_AUTH': False,
# 	'DEFAULT_API_SCHEME': 'http',
# 	'DEFAULT_TIMEOUT': 30,
# 	'DEFAULT_RETRY_COUNT': 3,
# 	'CALL_SERVICE_WATCHDOG_TYPE': 'call_service_resource'
# }
#
# for key, value in _DEFAULTS.items():
# 	try:
# 		getattr(settings, key)
# 	except AttributeError:
# 		setattr(settings, key, value)
# 	except ImportError as e:
# 		logging.info("ImportError: {}".format(e))
# 		pass
__version__ = '1.0.5'

VERSION = __version__


def get_version():
	return __version__
