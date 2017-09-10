#!/usr/bin/python
# coding=utf-8
__author__ = 'gisly'

import urllib
import urllib.request
import urllib.parse
import re

import json


def getJSONData(url, encoding, paramDict):
    urlData = getURLData(url, encoding, paramDict)
    if urlData is None:
        return None
    return json.loads(urlData)


def getURLData(url, encoding, paramDict):
    if paramDict:
        encodedParams = urllib.parse.urlencode(paramDict)
    else:
        encodedParams = None
    if encodedParams:
        url = url + '?%s' % encodedParams
    # urlEncoded = iriToUri(url)
    urlEncoded = url
    with urllib.request.urlopen(urlEncoded) as url_socket:
        data = url_socket.read()
    return data.decode(encoding)

