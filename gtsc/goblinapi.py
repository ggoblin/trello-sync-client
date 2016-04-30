# -*- coding: utf-8 -*-

import requests
import json

GOBLIN_URL = ''


def createMember(m):
    payload = {}
    payload['MemberId'] = m['id']
    payload['Name'] = m['fullName']
    payload['DisplayName'] = m['username']
    payload['email']= m['username']
    header = {'content-type': 'application/json'}
    r = requests.post(GOBLIN_URL + "api/members", data=json.dumps(payload), headers=header)
    print(r.text)
