# -*- coding: utf-8 -*-
import gtsc
from gtsc import api


def members_menu():
    load_members()


def load_members():
    gtsc.d.gauge_start(text="Get members from trello")
    gtsc.d.gauge_update(50, text="Create member list.")  # 10% of the whole task is done
    choise_list = get_member_list()
    gtsc.d.gauge_update(100, "any text here")  # work is done
    exit_code = gtsc.d.gauge_stop()  # cleanup actions
    code, tags = gtsc.d.checklist("Members you want to import to Goblin.", choices=choise_list)
    if code == gtsc.d.OK:
        print("")


def get_member_list():
    members = api.get_all_member(gtsc.BOARD_ID)
    print(members)
    ret = []
    for m in members:
        ret.append((m['username'], m['fullName'], True))
    return ret
