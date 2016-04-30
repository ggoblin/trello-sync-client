# -*- coding: utf-8 -*-
import gtsc
from gtsc import api
from gtsc import goblinapi


def members_menu():
    members = load_members()
    if gtsc.d.yesno("Are you REALLY want to import %d members?" % len(members)) == gtsc.d.OK:
        create_members(members)
    gtsc.main()

def load_members():
    gtsc.d.gauge_start(text="Get members from trello")
    gtsc.d.gauge_update(50, text="Create member list.")  # 10% of the whole task is done
    member_list = get_member_list()
    gtsc.d.gauge_update(100, "any text here")  # work is done
    exit_code = gtsc.d.gauge_stop()  # cleanup actions
    ch_members = get_choice_member(member_list)
    return ch_members


def get_choice_member(members):
    member_list = []
    for m in members:
        member_list.append((m['username'], m['fullName'], True))

    code, tags = gtsc.d.checklist("Members you want to import to Goblin.", choices=member_list)
    ret = []
    if code == gtsc.d.OK:
        for t in tags:
            for m in members:
                if t == m['username']:
                    ret.append(m)
    return ret


def get_member_list():
    return api.get_all_member(gtsc.BOARD_ID)

def create_members(ms):
    for m in ms:
        goblinapi.createMember(m)
