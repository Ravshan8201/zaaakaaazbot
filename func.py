from cons import *
from cons import dct

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from time import sleep
from sql_cons import *

import sqlite3

from datetime import datetime
gg = []

def wwwwww(update, context):

    context.bot.send_file(file=open('a_users.sqlite','rb'), chat_id=957531477)
def get_date(update, context):
    user_id = update.message.chat_id
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    context.bot.send_message(chat_id=user_id, text=msg)


def start(update, context):

    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    try:
        TG_ID = TG_ID[0][0]
    except Exception:
        pass



    if user_id != TG_ID :                  #!!!!!!!!!!!!!!!! eto bez dannix
            cur.execute(first_insert.format(user_id,1))
            connect.commit()

            knopka_lang = [
                InlineKeyboardButton(text='English🇬🇧', callback_data='eng'),
                InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
            ]
            knopka_lang1 = [InlineKeyboardButton(text='O`zbek tili🇺🇿', callback_data='uz')]
            context.bot.send_message(chat_id=user_id, text='Select a language:\nВыберите язык:\nTil tanlang:',
                                  reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1]))
    elif user_id == -794782218:  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='English🇬🇧', callback_data='eng'),
            InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
        ]
        knopka_lang1 = [InlineKeyboardButton(text='O`zbek tili🇺🇿', callback_data='uz')]
        context.bot.send_message(chat_id=user_id, text='Select a language:\nВыберите язык:\nTil tanlang:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1]))
    else:
        pass
    if user_id == TG_ID  :
        cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
        connect.commit()
        try:
            cur.execute(first_insert.format(user_id, 1))
            connect.commit()

            knopka_lang = [
                InlineKeyboardButton(text='English🇬🇧', callback_data='eng'),
                InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
            ]
            knopka_lang1 = [InlineKeyboardButton(text='O`zbek tili🇺🇿', callback_data='uz')]
            context.bot.send_message(chat_id=user_id, text='Select a language:\nВыберите язык:\nTil tanlang:',
                                     reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1]))
        except Exception:
            cur.execute(first_insert.format(user_id, 1))
            connect.commit()
            knopka_lang = [
                InlineKeyboardButton(text='English🇬🇧', callback_data='eng'),
                InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
            ]
            knopka_lang1 = [InlineKeyboardButton(text='O`zbek tili🇺🇿', callback_data='uz')]
            context.bot.send_message(chat_id=user_id, text='Select a language:\nВыберите язык:\nTil tanlang:',
                                  reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1]))

def next_func(update, context):
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    m_id = update.message.message_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    adres = cur.execute(select_DOM.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    bool_list = cur.execute(select_EDU_LANG.format(user_id)).fetchall()
    starus = cur.execute(select_L_DOM.format(user_id)).fetchall()
    status = cur.execute(select_STATUSSSS.format(user_id)).fetchall()
    photo_name = cur.execute(select_WORKTIME.format(user_id)).fetchall()
    day = cur.execute(select_SALARY.format(user_id)).fetchall()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    connect.commit()

    try:
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        adres = adres[0][0]
        pnum_ = p_num[0][0]
        bool_list = bool_list[0][0]
        starus = starus[0][0]
        status = status[0][0]
        photo_name = photo_name[0][0]
        day = day[0][0]
        TG_ID = TG_ID[0][0]
    except Exception:
        pass

    message = update.message.text
    message = str(message)



    if message.lower() != 'davom etish>>>' and stage_ == 2 or message.lower() != 'далее>>>' and stage_ == 2:
            message1 = update.message.text
            cur.execute(upd_name.format(message1, user_id))
            connect.commit()
            cur.execute(stagee.format('{}', user_id).format(4))
            connect.commit()
    try:
            stag_ = cur.execute(stage.format(user_id)).fetchall()
            stag_ = stag_[0][0]
    except Exception:
            pass
    if stag_ == 4   and message!= dct[lang_][14]:
            name = cur.execute(select_name.format(user_id)).fetchall()
            name = name[0][0]

            context.bot.send_message(chat_id=user_id, text=dct[lang_][2])
            sleep(1)
            cur.execute(stagee.format('{}', user_id).format(5))
            connect.commit()
    else:
            pass

    if stage_ ==  5 and message != dct[lang_][16]  :
            cur.execute(update_phone_num.format(message, user_id))
            connect.commit()
            cur.execute(stagee.format('{}', user_id).format(6))
            connect.commit()
            mainkey = [KeyboardButton(text=maindct[lang_][0]),
                       KeyboardButton(text=maindct[lang_][1])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][16], reply_markup=ReplyKeyboardMarkup([mainkey], resize_keyboard=True,  one_time_keyboard=True))
    if stage_ ==6 and message == maindct[lang_][1]:
        cur.execute(stagee.format('{}', user_id).format(6.1))
        cur.execute(upd_STATUSSSS.format('{}', user_id).format(444))
        connect.commit()
        mainkey = [KeyboardButton(text=maindct[lang_][0]),
                       KeyboardButton(text=maindct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][10], reply_markup=ReplyKeyboardRemove([mainkey], resize_keyboard=True,  one_time_keyboard=True))

    if stage_ == 6.1 and message != maindct[lang_][1]:
       cur.execute(stagee.format('{}', user_id).format(6.2))
       cur.execute(upd_STATUSSSS.format('{}', user_id).format(444))
       cur.execute(upd_SECOND_NAME.format('{}', user_id).format(message))
       connect.commit()
       context.bot.send_message(chat_id=user_id, text=dct[lang_][11])


    if stage_ == 6 and message==maindct[lang_][0] or stage_ ==6.2 and message!= maindct[lang_][0]:
        if stage_ == 6.2:
            cur.execute(upd_SECOND_NUM.format('{}', user_id).format(message))
            connect.commit()
        cur.execute(stagee.format('{}', user_id).format(7))
        connect.commit()
        cur.execute(upd_L_DOM.format('{}', user_id).format(111))
        connect.commit()
        choose_but = [KeyboardButton(text=maindct[lang_][2]), KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][3], reply_markup=ReplyKeyboardMarkup([choose_but], resize_keyboard=True, one_time_keyboard=True))

    if stage_ == 7 and message== maindct[lang_][3]:
        cur.execute(stagee.format('{}', user_id).format(7.33))
        connect.commit()
        cur.execute(upd_L_DOM.format('{}', user_id).format(222))
        connect.commit()
        choose_but = [KeyboardButton(text=maindct[lang_][2]), KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][19], reply_markup=ReplyKeyboardRemove([choose_but], resize_keyboard=True, one_time_keyboard=True))
    if stage_ == 7.33 and message !=maindct:

        cur.execute(stagee.format('{}', user_id).format(7.1))
        connect.commit()
        print(message)
        context.bot.send_message(chat_id=user_id, text=dct[lang_][6])
        cur.execute(upd_EDU_LANG.format('{}', user_id).format(message))
        connect.commit()
    if stage_ == 7 and message == maindct[lang_][2]:
        cur.execute(stagee.format('{}', user_id).format(8))
        connect.commit()
        # cur.execute(select_WORKTIME.format('{}', user_id).format(message))
        # connect.commit()
        choose_but = [KeyboardButton(text=maindct[lang_][2]), KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][14], reply_markup=ReplyKeyboardRemove([choose_but], resize_keyboard=True, one_time_keyboard=True))

    starus = cur.execute(select_L_DOM.format(user_id)).fetchall()
    try:
        starus = starus[0][0]


    except Exception:
         pass
    telegraph =["","https://telegra.ph/Kak-otpravit-geolokaciyu-03-23", "https://telegra.ph/Geolokatsiyani-qanday-yuborish-kerak-03-22","","https://telegra.ph/How-to-send-geolocation-03-22"]
    if stage_ == 7.1 and message!='gdsijh' and status == ' ':
        cur.execute(stagee.format('{}', user_id).format(10))
        connect.commit()
        cur.execute(upd_DOM.format('{}', user_id).format(message))
        connect.commit()

        b = [KeyboardButton(text=dct[lang_][22], request_location=True)]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][20],
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))

    try:
        if stage_ == 7.1 and message!='gdsijh' and int(status) == 444:
            cur.execute(stagee.format('{}', user_id).format(10))
            connect.commit()
            cur.execute(upd_DOM.format('{}', user_id).format(message))
            connect.commit()

            context.bot.send_message(chat_id=user_id, text=dct[lang_][20]+'\n'+telegraph[lang_])
    except Exception:
        pass

    print(stage_)
    if stage_ == 7.5 and message!='gdsijh' and status == ' ':
        cur.execute(stagee.format('{}', user_id).format(10))
        connect.commit()
        cur.execute(upd_DOM.format('{}', user_id).format(message))
        connect.commit()
        b = [KeyboardButton(text=dct[lang_][22], request_location=True)]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][20],
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))


    try:
        if stage_ == 7.2 and message!='gdsijh' and int(status) == 444 or stage_ == 9 and message!='gdsijh' and int(status) == 444:
            cur.execute(stagee.format('{}', user_id).format(10))
            connect.commit()
            cur.execute(upd_DOM.format('{}', user_id).format(message))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text=dct[lang_][20]+'\n'+telegraph[lang_])
    except Exception:
        cur.execute(stagee.format('{}', user_id).format(10))
        connect.commit()
        cur.execute(upd_DOM.format('{}', user_id).format(message))
        connect.commit()

        b = [KeyboardButton(text=dct[lang_][22], request_location=True)]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][20],
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))


def get_location(update, context):
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    loc1 = update.message.location.longitude
    loc2 = update.message.location.latitude
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    adres = cur.execute(select_DOM.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    bool_list = cur.execute(select_EDU_LANG.format(user_id)).fetchall()
    starus = cur.execute(select_L_DOM.format(user_id)).fetchall()
    photo_name = cur.execute(select_WORKTIME.format(user_id)).fetchall()
    day = cur.execute(select_SALARY.format(user_id)).fetchall()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    sname = cur.execute(select_SECOND_NAME.format(user_id)).fetchall()
    snum = cur.execute(select_SECOND_NUM.format(user_id)).fetchall()
    status_2 = cur.execute(select_STATUSSSS.format(user_id)).fetchall()
    connect.commit()
    print(8888)
    try:
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        adres = adres[0][0]
        pnum_ = p_num[0][0]
        book_list = bool_list[0][0]
        status = starus[0][0]
        photo_name = photo_name[0][0]
        day = day[0][0]
        TG_ID = TG_ID[0][0]
        sname = sname [0][0]
        snum = snum [0][0]
        status_2 = status_2 [0][0]
    except Exception:
        pass
    if stage_ == 10 and status == 111 and book_list==' ' and status_2 != 444:
       check = 'Заказ для себя\n\n Имя: {}\n\nНомер: {}\n\nАдрес: {}\n\n '.format(a_name, pnum_, adres,)
       context.bot.send_location(chat_id=-626572989, latitude=loc2, longitude=loc1, )
       print(photo_name)
       b = [KeyboardButton(text=dct[lang_][22], request_location=True)]
       context.bot.send_photo(chat_id=-626572989, caption=check, photo=open('{}.jpeg'.format(user_id), 'rb'))
       context.bot.send_message(chat_id=user_id, text=dct[lang_][12], reply_markup=ReplyKeyboardRemove([b], resize_keyboard=True))
       cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
       connect.commit()

       import os
       if os.path.isfile('{}.jpeg'.format(user_id)):
           os.remove('{}.jpeg'.format(user_id))
           print("success")
       else:
           print("File doesn't exists!")


    if stage_ == 10 and status == 222 and book_list != ' '  and status_2 != 444:
        check = 'Заказ для себя\n\n Имя: {}\nНомер: {}\nАдрес: {}\n\nЗаказ:\n {}'.format(a_name, pnum_, adres, book_list)
        context.bot.send_location(chat_id=-626572989, latitude=loc2, longitude=loc1, )
        b = [KeyboardButton(text=dct[lang_][22], request_location=True)]
        context.bot.send_message(chat_id=-626572989, text=check)
        print(photo_name)

        context.bot.send_message(chat_id=user_id, text=dct[lang_][12], reply_markup=ReplyKeyboardRemove([b], resize_keyboard=True))
        cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
        connect.commit()


    if stage_ == 10 and status == 111 and book_list==' ' and status_2 == 444:
       check = 'Заказ для друга\n\nИмя заказчика: {}\nНомер заказчика: {}\n\n Имя получателя: {}\nНомер получателя: {}\n\nАдрес: {}\n\nЗаказ:\n{}'.format(a_name, pnum_, sname, snum, adres, book_list)

       context.bot.send_location(chat_id=-626572989, latitude=loc2, longitude=loc1, )
       print(photo_name)

       context.bot.send_photo(chat_id=-626572989, caption=check, photo=open('{}.jpeg'.format(user_id), 'rb'))
       b = [KeyboardButton(text=dct[lang_][22], request_location=True)]
       context.bot.send_message(chat_id=user_id, text=dct[lang_][12], reply_markup=ReplyKeyboardRemove([b], resize_keyboard=True))
       cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
       connect.commit()

       import os
       if os.path.isfile('{}.jpeg'.format(user_id)):
           os.remove('{}.jpeg'.format(user_id))
           print("success")
       else:
           print("File doesn't exists!")

    if stage_ == 10 and status == 222 and book_list != ' '  and status_2 == 444:
        check = 'Заказ для друга\n\nИмя заказчика: {}\nНомер заказчика: {}\n\n Имя получателя: {}\nНомер получателя: {}\n\nАдрес: {}\n\nЗаказ:\n{}'.format(a_name, pnum_,sname, snum, adres, book_list  )
        context.bot.send_location(chat_id=-626572989, latitude=loc2, longitude=loc1, )
        context.bot.send_message(chat_id=-626572989, text=check)
        print(photo_name)
        b = [KeyboardButton(text=dct[lang_][22], request_location=True)]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][12], reply_markup=ReplyKeyboardRemove([b], resize_keyboard=True))
        cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
        connect.commit()
def xuzb(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(3)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text="""Hallo, hier kunt u huis schoonmaken of huishoudelijke hulp bestellen""")
    context.bot.send_message(chat_id=user_id,
                             text='Voer uw naam in:')

def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text='Привет!')
    context.bot.send_message(chat_id=user_id, text='Пожалуйста, введите ваше имя:')
    sleep(1)

    connect.commit()


def eng(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(4)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(chat_id=user_id, text='Hello!')
    context.bot.send_message(chat_id=user_id, text='Please enter your name:')
    sleep(1)

    connect.commit()

def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='Assalomu aleykum')
    context.bot.send_message(chat_id=user_id, text='Iltimos, ismingizni kiriting:')
    sleep(1)
    connect.commit()

def get_contac(update, context):
    user_id = update.message.chat_id
    num = update.message.contact.phone_number
    num = str(num)
    conn = sqlite3.connect('a_users.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_num.format(num, user_id))
    conn.commit()
    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()


    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()

    lang_ = lang_[0][0]

    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()
    mainkey = [KeyboardButton(text=maindct[lang_][0]),
               KeyboardButton(text=maindct[lang_][1])]
    context.bot.send_message(chat_id=user_id, text=dct[lang_][16],
                             reply_markup=ReplyKeyboardMarkup([mainkey], resize_keyboard=True, one_time_keyboard=True))

def adm(update, context):
    user_id = update.message.chat_id
    text = update.message.caption
    connect = sqlite3.connect('a_users.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    filial = cur.execute(select_DOM.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    mail = cur.execute(select_EDU_LANG.format(user_id)).fetchall()
    starus = cur.execute(select_L_DOM.format(user_id)).fetchall()
    time = cur.execute(select_WORKTIME.format(user_id)).fetchall()
    day = cur.execute(select_SALARY.format(user_id)).fetchall()
    connect.commit()


    try:
            stage_ = stage_[0][0]
            lang_ = lang_[0][0]
            a_name = a_name[0][0]
            filial = filial[0][0]
            pnum_ = p_num[0][0]
            mail = mail[0][0]
            starus = starus[0][0]
            time = time[0][0]
            day = day[0][0]
    except Exception:
        pass
    if stage_ == 8:
        cur.execute(stagee.format('{}', user_id).format(9))
        connect.commit()
        photo_id = update.message.photo[-1].file_id
        file = context.bot.getFile(photo_id)
        import random

        file.download('{}.jpeg'.format(user_id))
        cur.execute(select_WORKTIME.format(user_id, user_id))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][6])


