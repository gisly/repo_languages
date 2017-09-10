#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = "gisly"

import web_utils
import time
import urllib.error

GITHUB_URL = 'https://api.github.com/'
GITHUB_ENCODING = 'utf-8'
MAX_PAUSE_SEC = 120
ATTEMPT_NUM = 5
RATE_LIMIT_METHOD = 'rate_limit'


def search_repos(text_to_search):
    params = {'q' : text_to_search}
    result = call_github_method('search/repositories', params)
    if 'total_count' in result and result['total_count'] > 0:
        return result['items']
    return []


def call_github_method(method_name, params):
    github_url = GITHUB_URL + method_name
    for i in range(0, ATTEMPT_NUM):
        try:
            if i > 0:
                print('attempt # %s' % i)
            return web_utils.getJSONData(github_url, GITHUB_ENCODING, params)
        except urllib.error.HTTPError as e:
            if method_name == RATE_LIMIT_METHOD:
                raise e
            current_rate = call_github_method(RATE_LIMIT_METHOD, {})

            if method_name.startswith('search'):
                reset_time_key = 'search'
            else:
                reset_time_key = 'core'
            reset_time = current_rate['resources'][reset_time_key]['reset']
            cur_time = time.time()
            seconds_remaining = reset_time - cur_time
            if seconds_remaining > MAX_PAUSE_SEC:
                raise e
            print('rate limit hit. Waiting for %s seconds' % seconds_remaining)
            time.sleep(seconds_remaining)



