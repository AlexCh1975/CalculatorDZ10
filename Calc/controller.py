from telegram import ForceReply, Update
from telegram.ext import ( 
    ContextTypes,
    CommandHandler
    )

import re
import model_sum as sum
import model_keyboard as kb
import model_sub as sub
import model_div as div
import model_mult as mult
import model_sqrt as sqrt



CHOICE = 0
number1 = 0
number2 = 0 
value = ''
args = []
sign = '+'

async def start(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard, value, args, sign
    user = update.effective_user
    await update.message.reply_html(
        rf'Привет {user.mention_html()}, я телеграм бот КАЛЬКУЛЯТОР!',
    )
    keyboard = kb.create_kb(update, context)
    await update.message.reply_text('0', reply_markup=keyboard)

    return CHOICE
    

async def cheice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global keyboard, value, args, sign
    data = update.callback_query.data
    
    if data =='no':
        pass
    elif data == 'C':
        value = ''
        number1 = 0
        number2 = 0
        args= []
        sign = '+'
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == '<=':
        value = value.rstrip(value[-1])
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=value, reply_markup=keyboard)
    elif data == '+/-':
        if sign == '+': 
            sign = '-'
            value += sign 
            await update.callback_query.answer()
            await update.callback_query.edit_message_text(text=value, reply_markup=keyboard)
            
        else: 
            sign = "+"
            value += sign
            await update.callback_query.answer()
            await update.callback_query.edit_message_text(text=value, reply_markup=keyboard)
            
    elif data == '=':
        args.append(value)
        args = transform(args)
        for i in args:
            print(type(i))
        
        value = ''
        if args[1] == 'plus':
            number1 = args[0]
            number2 = args[2]
            sum.init(number1, number2)
            result = sum.sum()
            args = []
        elif args[1] == 'minus':
            number1 = args[0]
            number2 = args[2]
            sub.init(number1, number2)
            result = sub.sub()
            args = []
        elif args[1] == '/':
            number1 = args[0]
            number2 = args[2]
            div.init(number1, number2)
            result = div.div()
            args = []
        elif args[1] == '//':
            number1 = args[0]
            number2 = args[2]
            div.init(number1, number2)
            result = div.int_div()
            args = []
        elif args[1] == '%':
            number1 = args[0]
            number2 = args[2]
            div.init(number1, number2)
            result = div.rem_of_div()
            args = []
        elif args[1] == '*':
            number1 = args[0]
            number2 = args[2]
            mult.init(number1, number2)
            result = mult.mult()
            args = []
        elif args[1] == '^':
            number1 = args[0]
            number2 = args[2]
            mult.init(number1, number2)
            result = mult.expo()
            args = []

        result = reverse_transform(result)
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=result, reply_markup=keyboard)
    elif data == 'plus':
        args.append(value)
        value = ''
        args.append('plus')
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == 'minus':
        args.append(value)
        value = ''
        args.append('minus')
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == '/':
        args.append(value)
        value = ''
        args.append('/')
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == '//':
        args.append(value)
        value = ''
        args.append('//')
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == '%':
        args.append(value)
        value = ''
        args.append('%')
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == '*':
        args.append(value)
        value = ''
        args.append('*')
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == '^':
        args.append(value)
        value = ''
        args.append('^')
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text='0', reply_markup=keyboard)
    elif data == 'sqrt':
        args.append(value)
        args = transform(args)
        value = ''
        number1 = args[0]
        sqrt.init(number1)
        result = sqrt.sqrt()
        result = reverse_transform(result)
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=result, reply_markup=keyboard)
        args = []
    elif re.findall(r'[0-9(\.){,1}(\(\d(\+|\-)\dj\))]', data):
        value += data 
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=value, reply_markup=keyboard)
    else:
        print('неполный ввод')


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await CommandHandler.END


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '''Кнопка "CE" не реализована.\n
        Чтобы поставить знак, в комплексном числе используйте “+/-”.\n
        Чтобы изменить знак на противоположный, с начало удалите
        предшествующий используя “<=”.\n
        Калькулятор может работать с комплексными числами.\n
        Примерный ввод: (5+6j).''')

def transform(args):
    for i, item in enumerate(args):
        if re.findall(r'^(\(\d+[\+|\-]\d+j\))$', item):
            args[i] = complex(item)
        elif re.findall(r'^(\d+\.\d+)$', item):
            args[i] = float(item)
        elif re.findall(r'^(\d+)$', item):
            args[i] = int(item)
        elif item == '':
            args[i] = '0'
            args[i] = int(args[i])
            
    return args

def reverse_transform(result):
    if type(result) == complex:
        result = str(result)
    return result