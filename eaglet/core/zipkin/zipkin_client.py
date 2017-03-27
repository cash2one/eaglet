# -*- coding: utf-8 -*-
import time
import json
import logging
try:
	import settings
except:
	from django.conf import settings


try:
	IS_DEPLOY = (settings.MODE == 'deploy')
except BaseException as e:
	IS_DEPLOY = False


TYPE_CALL_SERVICE = 3
TYPE_CALL_REDIS = 1
TYPE_CALL_MYSQL = 2
TYPE_CALL_THIS_SERVICE = -1  # 在当前service里的数据

TYPE2STRING = {
	TYPE_CALL_MYSQL: 'call_mysql',
	TYPE_CALL_REDIS: 'call_redis',
	TYPE_CALL_SERVICE: 'call_service',
	TYPE_CALL_THIS_SERVICE: 'call_this_service'
}




class ZipkinClient(object):
	"""docstring for ZipkinClient"""
	def __init__(self, service_name, zid, zdepth, fZindex=0):
		super(ZipkinClient, self).__init__()
		self.zid = zid
		self.zdepth = int(zdepth)
		self.zindex = 1
		self.msg = '[zipkin:python]'
		self.service = service_name
		self.fZindex = fZindex
		self.zipkin_messages = []
		self.start = time.time()

	def sendMessge(self, type, responseTime, method='', resource='', data='', isCallDownstream=0):

		self.zindex += 1
		self.type = TYPE2STRING[int(type)]
		self.responseTime = responseTime
		self.method = method
		self.resource = resource
		self.data = data
		self.isCallDownstream = isCallDownstream
		data = self.getData()

		if IS_DEPLOY:
			# logging.info(json.dumps(data))
			self.zipkin_messages.append(data)


	def getData(self):
		return {
			"msg": self.msg,
			"service": self.service,
			"type": self.type,
			"zid": self.zid,
			"zdepth":  self.zdepth,
			"zindex": self.zindex,
			"isCallDownstream": self.isCallDownstream,
			"responseTime": self.responseTime,
			"resource": self.resource,
			"method": self.method,
			"data": self.data,
			'fZindex': self.fZindex
		}

zipkinClient = None #init none
