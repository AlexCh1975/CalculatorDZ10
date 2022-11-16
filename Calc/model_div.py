# import logger as log
x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def div():
    if y == 0:
        return 'На 0 делить нельзя!'
    return x / y

def int_div():
    if isinstance(x, complex) or isinstance(y, complex):
        result = "С этим типом данных нельзя проводить подобные операции!"
        # log.all_logger(result, ['int_div', x, y])
        # print("С этим типом данных нельзя проводить подобные операции!")
        # exit()
        return result
    else:
        return x // y

def rem_of_div():
    if isinstance(x, complex) or isinstance(y, complex):
        result = "С этим типом данных нельзя проводить подобные операции!"
        # log.all_logger(result, ['rem_of_div', x, y])
        # print("С этим типом данных нельзя проводить подобные операции!")
        # exit()
        return result
    else:
        return x % y