# -*- coding: utf-8 -*-

import locale
from dialog import Dialog
from gtsc import api

locale.setlocale(locale.LC_ALL, '')
d = Dialog(dialog="dialog")

GOBLIN_URL = ''
BOARD_ID = ''


def main():
    import gtsc.api
    global GOBLIN_URL
    global BOARD_ID
    d.set_background_title("Goblin Trello Sync client")
    print(gtsc.api.API_TOKEN)
    if gtsc.api.API_TOKEN == '':
        code, token = d.inputbox("Your trello api token")
        if code == d.OK:
            gtsc.api.API_TOKEN = token

    if gtsc.api.APP_KEY == '':
        code, key = d.inputbox("Your trello api app key")
        if code == d.OK:
            gtsc.api.APP_KEY = key

    if GOBLIN_URL == '':
        code, url = d.inputbox("Your Goblin Url")
        if code == d.OK:
            GOBLIN_URL = url

    if BOARD_ID == '':
        set_borad()

    code, tag = d.menu("What do you want to do?",
                       choices=[("(1)", "Import members from trello"),
                                ("(2)", "Import Interation from trello")])
    if code == d.OK:
        if tag == '(1)':
            import gtsc.members
            gtsc.members.members_menu()


def set_borad():
    global BOARD_ID
    try:
        borad_Dic = api.get_boards()
    except Exception as ex:
        d.msgbox(ex)
        main()

    choice_list = []
    for borad in borad_Dic:
        choice_list.append((borad['name'], borad['desc']))

    code, tag = d.menu('What borad you want to sync?',
                       choices=choice_list)
    if code == d.OK:
        for board in borad_Dic:
            if tag == board['name']:
                BOARD_ID = board['id']
                board_name = board['name']
        if BOARD_ID == '':
            d.msgbox('Get Board Fail.')
            main()
    d.msgbox('Use Board %s ID %s' % (board_name, BOARD_ID))
