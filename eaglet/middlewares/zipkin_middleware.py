# -*- coding: utf-8 -*-

import settings
from eaglet.core.zipkin import zipkin_client
import logging
import time
import json
# ZipkinRecordTime = 0.5  # 秒
ZipkinRecordTime = 0  # 秒


class ZipkinMiddleware(object):
    """docstring for ZipkinMiddleware"""
    def process_request(self, request, response):

        zid = request.params.get('zid', None)
        fZindex = request.params.get('f_zindex', 0)
        zdepth = request.params.get('zdepth', 1)
        zipkin_client.zipkinClient = None

        if zid:
            zipkin_client.zipkinClient = zipkin_client.ZipkinClient(settings.SERVICE_NAME, zid, zdepth, fZindex)

            #request.params['zipkin_client'] = zipkin_client.zipkinClient

    def process_response(self, request, response, resource):

        if hasattr(zipkin_client, 'zipkinClient') and zipkin_client.zipkinClient:
            total_time = time.time() - zipkin_client.zipkinClient.start
            if total_time > ZipkinRecordTime:
                zipkin_client.zipkinClient.sendMessge(zipkin_client.TYPE_CALL_THIS_SERVICE, total_time)

                for message in zipkin_client.zipkinClient.zipkin_messages:
                    logging.info(json.dumps(message))
