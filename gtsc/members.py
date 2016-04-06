# -*- coding: utf-8 -*-
import gtsc
import trello
import io

def members_menu():
    load_members()

def load_members():
    gtsc.d.gauge_start(text="Get members from trello")
    gtsc.d.gauge_update(10)  # 10% of the whole task is done
    gtsc.d.gauge_update(100, "any text here")  # work is done
    exit_code = gtsc.d.gauge_stop()  # cleanup actions
