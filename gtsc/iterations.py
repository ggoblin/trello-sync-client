# -*- coding: utf-8 -*-
import gtsc
from gtsc import api


def iteration_menu():
    show_all = False
    if gtsc.d.yesno("Are you REALLY want to load all Iterations?") == gtsc.d.OK:
        show_all = True
    iterations = load_iteration(show_all)


def load_iteration(show_all):
    gtsc.d.gauge_start(text="Get Iterations.")
    gtsc.d.gauge_update(50, text="Create Iterations list.")  # 10% of the whole task is done
    it_list = get_iteration_list(show_all)
    gtsc.d.gauge_update(100, "any text here")  # work is done
    exit_code = gtsc.d.gauge_stop()  # cleanup actions
    ch_members = get_choice_iterations(it_list)
    return ch_members


def get_iteration_list(show_all):
    return api.get_all_iterations(show_all)


def get_choice_iterations(iterations):
    iteration_list = []
    for i in iterations:
        iteration_list.append((i['id'], i['name'], True))

    code, tags = gtsc.d.checklist("Iteration you want to import to Goblin.", choices=iteration_list)
    ret = []
    if code == gtsc.d.OK:
        for t in tags:
            for i in iteration_list:
                if t == i['id']:
                    ret.append(i)
    return ret
