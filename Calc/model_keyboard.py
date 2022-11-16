from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes
    )

def create_kb(update: Update, context:ContextTypes.DEFAULT_TYPE):
    global keyboard
    buttons = [
        [
            InlineKeyboardButton('CE ', callback_data='no'),
            InlineKeyboardButton('C', callback_data='C'),
            InlineKeyboardButton('<=', callback_data='<='),
            InlineKeyboardButton('/', callback_data='/')
        ],
        [
            InlineKeyboardButton('7', callback_data='7'),
            InlineKeyboardButton('8', callback_data='8'),
            InlineKeyboardButton('9', callback_data='9'),
            InlineKeyboardButton('*', callback_data='*')
        ],
        [
            InlineKeyboardButton('4', callback_data='4'),
            InlineKeyboardButton('5', callback_data='5'),
            InlineKeyboardButton('6', callback_data='6'),
            InlineKeyboardButton('-', callback_data='minus')
        ],
        [
            InlineKeyboardButton('1', callback_data='1'),
            InlineKeyboardButton('2', callback_data='2'),
            InlineKeyboardButton('3', callback_data='3'),
            InlineKeyboardButton('+', callback_data='plus')
        ],
        [
            InlineKeyboardButton('+/-', callback_data='+/-'),
            InlineKeyboardButton('0', callback_data='0'),
            InlineKeyboardButton(',', callback_data='.'),
            InlineKeyboardButton('j', callback_data='j')
        ],
        [
            InlineKeyboardButton('//', callback_data='//'),
            InlineKeyboardButton('%', callback_data='%'),
            InlineKeyboardButton('(', callback_data='('),
            InlineKeyboardButton(')', callback_data=')')
        ],
        [
            InlineKeyboardButton('^', callback_data='^'),
            InlineKeyboardButton('sgrt', callback_data='sqrt'),
            InlineKeyboardButton('=', callback_data='=')
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    return keyboard

