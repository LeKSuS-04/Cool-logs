import time

class Colors:
    class style:
        RESET         = '\033[0m'
        BOLD          = '\033[01m'
        DISABLE       = '\033[02m'
        UNDERLINE     = '\033[04m'
        REVERSE       = '\033[07m'
        STRIKETHROUGH = '\033[09m'
        INVISIBLE     = '\033[08m'
    class fg:
        BLACK         = '\033[30m'
        RED           = '\033[31m'
        GREEN         = '\033[32m'
        ORANGE        = '\033[33m'
        BLUE          = '\033[34m'
        PURPLE        = '\033[35m'
        CYAN          = '\033[36m'
        LIGHTGRAY     = '\033[37m'
        DARKGRAY      = '\033[90m'
        LIGHTRED      = '\033[91m'
        LIGHTGREEN    = '\033[92m'
        YELLOW        = '\033[93m'
        LIGHTBLUE     = '\033[94m'
        PINK          = '\033[95m'
        LIGHTCYAN     = '\033[96m'
    class bg:
        BLACK         = '\033[40m'
        RED           = '\033[41m'
        GREEN         = '\033[42m'
        ORANGE        = '\033[43m'
        BLUE          = '\033[44m'
        PURPLE        = '\033[45m'
        CYAN          = '\033[46m'
        LIGHTGRAY     = '\033[47m'


class LogLevels():
    CRITICAL = 1
    ERROR    = 2
    WARNING  = 4
    INFO     = 8
    DEBUG    = 16
    ALL      = 31

class Logger():
    def __init__(self, colorful: bool = True, loglevel: int = LogLevels.ALL, infolength: int = 9, timecolor: Colors = Colors.fg.CYAN):
        self._colorful = colorful
        self._infolength = infolength
        self._timecolor = timecolor
        self._loglevel = loglevel


    def _get_time(self):
        return '[' + time.strftime("%H:%M:%S", time.localtime()) + ']'

    def _get_info(self, infoname):
        length = self._infolength

        if len(infoname) >= length:
            prefix = '['
            postfix = ']'
            infoname = infoname[:length]
        else:
            prefix = '[' + ' ' * ((length + 1- len(infoname)) // 2)
            postfix = ' ' * ((length - len(infoname)) // 2) + ']'

        return prefix + infoname + postfix


    def set_level(self, loglevel: int):
        self._loglevel = loglevel


    def custom(self, *data, infoname='', infocolor: Colors = Colors.fg.CYAN):
        if self._colorful:
            time_color = self._timecolor + Colors.style.BOLD
            info_color = infocolor + Colors.style.BOLD
            reset = Colors.style.RESET
        else:
            time_color = info_color = reset = ''


        time = time_color + self._get_time() + reset

        info = info_color + self._get_info(infoname) + reset
        text = f'{" ".join([str(x) for x in data])}'

        print(f'{time} {info} {text}')
        

    def critical(self, *data):
        if self._loglevel & (1 << 0):
            self.custom(*data, infoname='CRITICAL', infocolor=Colors.bg.RED)

    def error(self, *data):
        if self._loglevel & (1 << 1):
            self.custom(*data, infoname='ERROR', infocolor=Colors.fg.RED)

    def warning(self, *data):
        if self._loglevel & (1 << 2):
            self.custom(*data, infoname='WARNING', infocolor=Colors.fg.ORANGE)

    def info(self, *data):
        if self._loglevel & (1 << 3):
            self.custom(*data, infoname='INFO', infocolor=Colors.fg.CYAN)

    def debug(self, *data):
        if self._loglevel & (1 << 4):
            self.custom(*data, infoname='DEBUG', infocolor=Colors.fg.PURPLE)


    def plus(self, *data):
        self.custom(*data, infoname='+', infocolor=Colors.fg.GREEN)

    def minus(self, *data):
        self.custom(*data, infoname='-', infocolor=Colors.fg.RED)

    
    def success(self, *data):
        self.custom(*data, infoname='SUCCESS', infocolor=Colors.fg.GREEN)

    def failure(self, *data):
        self.custom(*data, infoname='FAILURE', infocolor=Colors.fg.RED)



    def demo(self):
        self.critical('This is .critical()')
        self.error('This is .error()')
        self.warning('This is .warning()')
        self.info('This is .info()')
        self.debug('This is .debug()')
        print()
        self.plus('This is .plus()')
        self.minus('This is .minus()')
        print()
        self.success('This is .success()')
        self.failure('This is .failure()')
        print()
        self.custom('This is custom one, with infocolor = Colors.fg.ORANGE', infoname='CUSTOM #1', infocolor=Colors.fg.ORANGE)
        self.custom('This is custom one, with infocolor = Colors.bg.PURPLE', infoname='CUSTOM #2', infocolor=Colors.bg.PURPLE)
        self.custom('This is custom one, with infocolor = Colors.fg.BLACK + Colors.bg.ORANGE', infoname='CUSTOM #3', infocolor=Colors.fg.BLACK + Colors.bg.ORANGE)

if __name__ == '__main__':
    log = Logger()
    log.demo()