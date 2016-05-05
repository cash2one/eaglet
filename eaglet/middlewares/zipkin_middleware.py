# -*- coding: utf-8 -*-

import settings
from eaglet.core.zipkin import zipkin_client

class ZipkinMiddleware(object):
    """docstring for ZipkinMiddleware"""
    def process_request(self, request, response):

        zid = request.params.get('zid', None)
        f_zindex = request.params.get('f_zindex', 0)
        zdepth = request.params.get('zdepth', 1)
        zipkin_client.zipkinClient = None
        if zid:
            zipkin_client.zipkinClient = zipkin_client.ZipkinClient(zid, zdepth, f_zindex)

            #request.params['zipkin_client'] = zipkin_client.zipkinClient 