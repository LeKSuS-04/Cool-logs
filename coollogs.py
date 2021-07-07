import time

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def get_time():
    return f'[{time.strftime("%H:%M:%S", time.localtime())}]'

def get_type(type):
    length = 9
    if len(type) >= length:
        return f'[{type[:length]}]'
    else:
        prefix = ' ' * ((length + 1- len(type)) // 2)
        postfix = ' ' * ((length - len(type)) // 2)
        return f'[{prefix}{type}{postfix}]'

def critical(text = ''):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{colors.bg.red}{colors.bold}{get_type("CRITICAL")}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')

def error(text = ''):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{colors.fg.red}{colors.bold}{get_type("ERROR")}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')

def warning(text = ''):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{colors.fg.orange}{colors.bold}{get_type("WARNING")}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')

def log(text = ''):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{colors.fg.lightblue}{colors.bold}{get_type("LOG")}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')

def success(text = ''):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{colors.fg.green}{colors.bold}{get_type("SUCCESS")}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')

def new(text = ''):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{colors.fg.green}{colors.bold}{get_type("+")}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')

def debug(text = ''):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{colors.fg.purple}{colors.bold}{get_type("DEBUG")}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')

def custom(text = '', type = '', typecolor: colors = colors.fg.lightblue):
    time = f'{colors.fg.cyan}{colors.bold}{get_time()}{colors.reset}'
    type = f'{typecolor}{colors.bold}{get_type(type)}{colors.reset}'
    text = f'{text}'
    print(f'{time} {type} {text}')