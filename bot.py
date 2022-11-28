# -*- coding: utf8 -*-
# 5791567885:AAEKkykMnrEiizrBEIxjRPJ-t4L9crW4BpY

import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from py_currency_converter import convert

bot = telebot.TeleBot('5791567885:AAEKkykMnrEiizrBEIxjRPJ-t4L9crW4BpY')

@bot.message_handler(commands=['start'])
def courses(message):
    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('Получить курс криптовалюты ₿'), types.KeyboardButton('💶Получить курс валют💷'))
    cr = bot.send_message(message.chat.id, 'Главная', reply_markup=button1)
    bot.register_next_step_handler(cr, step1)

def step1(message):
    if message.text == 'Получить курс криптовалюты ₿':
        step2(message)
    elif message.text == '💶Получить курс валют💷':
        wallet(message)

def wallet(message):
    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('USD'), types.KeyboardButton('RUB'), types.KeyboardButton('CNY(Китайский юань)'), types.KeyboardButton('EUR'), types.KeyboardButton('GBP(Фунт стерлингов)'), types.KeyboardButton('Главная'))
    pr = bot.send_message(message.chat.id, 'Курсы валют', reply_markup=button1)
    bot.register_next_step_handler(pr, wallet2)

def wallet2(message):
    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('Назад'))
    if message.text == 'USD':
        price = convert(base='USD', amount=1, to=['RUB', 'CNY', 'GBP', 'JPY', 'EUR', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 USD: {price["RUB"]} RUB\n'
                                          f'1 USD: {price["CNY"]} CNY\n'
                                          f'1 USD: {price["GBP"]} GBP\n'
                                          f'1 USD: {price["JPY"]} JPY\n'
                                          f'1 USD: {price["EUR"]} EUR\n'
                                          f'1 USD: {price["UAH"]} UAH\n'
                                          f'1 USD: {price["KZT"]} KZT\n')
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, wallet)

    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('Назад'))
    if message.text == 'RUB':
        price = convert(base='RUB', amount=1, to=['USD', 'CNY', 'GBP', 'JPY', 'EUR', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 RUB: {price["USD"]} USD\n'
                                          f'1 RUB: {price["CNY"]} CNY\n'
                                          f'1 RUB: {price["GBP"]} GBP\n'
                                          f'1 RUB: {price["JPY"]} JPY\n'
                                          f'1 RUB: {price["EUR"]} EUR\n'
                                          f'1 RUB: {price["UAH"]} UAH\n'
                                          f'1 RUB: {price["KZT"]} KZT\n')
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, wallet)

    if message.text == 'CNY(Китайский юань)':
        price = convert(base='CNY', amount=1, to=['USD', 'RUB', 'GBP', 'JPY', 'EUR', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 CNY: {price["USD"]} USD\n'
                                          f'1 CNY: {price["RUB"]} RUB\n'
                                          f'1 CNY: {price["GBP"]} GBP\n'
                                          f'1 CNY: {price["JPY"]} JPY\n'
                                          f'1 CNY: {price["EUR"]} EUR\n'
                                          f'1 CNY: {price["UAH"]} UAH\n'
                                          f'1 CNY: {price["KZT"]} KZT\n')
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, wallet)

    if message.text == 'EUR':
        price = convert(base='EUR', amount=1, to=['USD', 'RUB', 'GBP', 'CNY', 'JPY', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 EUR: {price["USD"]} USD\n'
                                          f'1 EUR: {price["RUB"]} RUB\n'
                                          f'1 EUR: {price["GBP"]} GBP\n'
                                          f'1 EUR: {price["CNY"]} CNY\n'
                                          f'1 EUR: {price["JPY"]} JPY\n'
                                          f'1 EUR: {price["UAH"]} UAH\n'
                                          f'1 EUR: {price["KZT"]} KZT\n')
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, wallet)

    if message.text == 'GBP(Фунт стерлингов)':
        price = convert(base='GBP', amount=1, to=['USD', 'RUB', 'EUR', 'CNY', 'JPY', 'UAH', 'KZT'])
        bot.send_message(message.chat.id, f'1 GBP: {price["USD"]} USD\n'
                                          f'1 GBP: {price["RUB"]} RUB\n'
                                          f'1 GBP: {price["EUR"]} EUR\n'
                                          f'1 GBP: {price["CNY"]} CNY\n'
                                          f'1 GBP: {price["JPY"]} JPY\n'
                                          f'1 GBP: {price["UAH"]} UAH\n'
                                          f'1 GBP: {price["KZT"]} KZT\n')
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, wallet)

    if message.text == 'Главная':
        courses(message)


def step2(message):
    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('Курс USD'), types.KeyboardButton('Курс RUB'),types.KeyboardButton('Курс CNY(Китайский юань)'), types.KeyboardButton('Курс EUR'), types.KeyboardButton('Курс GBP(Фунт стерлингов)'), types.KeyboardButton('Главная'))
    pr = bot.send_message(message.chat.id, 'Курсы', reply_markup=button1)
    bot.register_next_step_handler(pr, step3)

def step3(message):
    button1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1.add(types.KeyboardButton('Назад'))
    if message.text == 'Курс USD':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, usd-coin, dogecoin', vs_currencies='usd')
        bot.send_message(message.chat.id, f'Bitcoin: {price["bitcoin"]["usd"]}$\n'
                                          f'Ethereum: {price["ethereum"]["usd"]}$\n'
                                          f'Litecoin: {price["litecoin"]["usd"]}$\n'
                                          f'USD Coin: {price["usd-coin"]["usd"]}$\n'
                                          f'Dogecoin: {price["dogecoin"]["usd"]}$\n', reply_markup=button1)
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, step2)

    elif message.text == 'Курс RUB':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, usd-coin, dogecoin', vs_currencies='rub')
        bot.send_message(message.chat.id, f'Bitcoin: {price["bitcoin"]["rub"]}₽\n'
                                          f'Ethereum: {price["ethereum"]["rub"]}₽\n'
                                          f'Litecoin: {price["litecoin"]["rub"]}₽\n'
                                          f'USD Coin: {price["usd-coin"]["rub"]}₽\n'
                                          f'Dogecoin: {price["dogecoin"]["rub"]}₽\n', reply_markup=button1)
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, step2)

    elif message.text == 'Курс CNY(Китайский юань)':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, usd-coin, dogecoin', vs_currencies='cny')
        bot.send_message(message.chat.id, f'Bitcoin: {price["bitcoin"]["cny"]}¥\n'
                                          f'Ethereum: {price["ethereum"]["cny"]}¥\n'
                                          f'Litecoin: {price["litecoin"]["cny"]}¥\n'
                                          f'USD Coin: {price["usd-coin"]["cny"]}¥\n'
                                          f'Dogecoin: {price["dogecoin"]["cny"]}¥\n', reply_markup=button1)
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, step2)

    elif message.text == 'Курс EUR':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, usd-coin, dogecoin', vs_currencies='eur')
        bot.send_message(message.chat.id, f'Bitcoin: {price["bitcoin"]["eur"]}€\n'
                                          f'Ethereum: {price["ethereum"]["eur"]}€\n'
                                          f'Litecoin: {price["litecoin"]["eur"]}€\n'
                                          f'USD Coin: {price["usd-coin"]["eur"]}€\n'
                                          f'Dogecoin: {price["dogecoin"]["eur"]}€\n', reply_markup=button1)
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, step2)

    elif message.text == 'Курс GBP(Фунт стерлингов)':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, usd-coin, dogecoin', vs_currencies='gbp')
        bot.send_message(message.chat.id, f'Bitcoin: {price["bitcoin"]["gbp"]}£\n'
                                          f'Ethereum: {price["ethereum"]["gbp"]}£\n'
                                          f'Litecoin: {price["litecoin"]["gbp"]}£\n'
                                          f'USD Coin: {price["usd-coin"]["gbp"]}£\n'
                                          f'Dogecoin: {price["dogecoin"]["gbp"]}£\n', reply_markup=button1)
        go_courses = bot.send_message(message.chat.id, '^_^', reply_markup=button1)
        bot.register_next_step_handler(go_courses, step2)

    elif message.text == 'Главная':
        courses(message)

bot.polling()
