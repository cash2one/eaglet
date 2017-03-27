# -*- coding: utf-8 -*-

import settings
from eaglet.core.zipkin import zipkin_client
import logging
import time
import json
# ZipkinRecordTime = 0.5  # 秒
ZipkinRecordTime = 0  # 秒
start = 0

class ZipkinMiddleware(object):
    """docstring for ZipkinMiddleware"""
    def process_request(self, request, response):

        zid = request.params.get('zid', None)
        fZindex = request.params.get('f_zindex', 0)
        zdepth = request.params.get('zdepth', 1)
        zipkin_client.zipkinClient = None
        zipkin_client.zipkin_messages = []
        global start
        start = 0
        if zid:
            start = time.time()
            zipkin_client.zipkinClient = zipkin_client.ZipkinClient(settings.SERVICE_NAME, zid, zdepth, fZindex)

            #request.params['zipkin_client'] = zipkin_client.zipkinClient

    def process_response(self, request, response, resource):

        total_time = time.time() - start

        if hasattr(zipkin_client, 'zipkinClient') and zipkin_client.zipkinClient and total_time > ZipkinRecordTime:

            zipkin_client.zipkinClient.sendMessge(zipkin_client.TYPE_CALL_THIS_SERVICE, total_time)

            for message in zipkin_client.zipkin_messages:
                logging.info(json.dumps(message))
