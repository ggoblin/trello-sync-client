# -*- coding: utf-8 -*-
import requests
import gtsc

API_TOKEN = ''
APP_KEY = ''
TRELLO_API_URL = 'https://api.trello.com/1/'


def get_boards():
    method_name = 'members/me/boards'
    api_url = get_full_api_url(method_name)
    print(api_url)
    reslut = requests.get(api_url)
    if reslut.status_code != 200:
        gtsc.d.msgbox("Api error %s" % reslut.text)
        gtsc.main()
    return reslut.json()


def get_all_member():
    method_name = 'boards/%s/members' % gtsc.BOARD_ID
    api_url = get_full_api_url(method_name)
    print(api_url)
    reslut = requests.get(api_url)
    if reslut.status_code != 200:
        gtsc.d.msgbox("Api error %s" % reslut.text)
        gtsc.main()
    return reslut.json()


def get_all_iterations(show_all=False):
    method_name = 'boards/%s/lists' % gtsc.BOARD_ID
    api_url = get_full_api_url(method_name)
    if show_all:
        api_url += '&filter=all'
    print(api_url)
    reslut = requests.get(api_url)
    if reslut.status_code != 200:
        gtsc.d.msgbox("Api error %s" % reslut.text)
        gtsc.main()
    lists = reslut.json()
    ret = []
    for l in lists:
        if 'Iteration' in l['name']:
            ret.append(l)
    return ret


def get_full_api_url(method):
    url = TRELLO_API_URL + method + '?key=%s&token=%s' % (APP_KEY, API_TOKEN)
    return url
