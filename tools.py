from datetime import datetime as d
import linecache
import sys


class Color:
    BLACK = 0
    RED = 1
    LIME = 2
    YELLOW = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    GRAY = 7


class timer:
    start_time = ''
    def start(self):
        self.start_time = d.datetime.now()

    def end(self):
        end_timer = d.datetime.now()
        return (end_timer - self.start_time).total_seconds()


class log:
    @classmethod
    def color_print(self,text,color):
        try:
            print '\033[1;3'+str(color)+'m'+str(text)+'\033[1;m'
        except Exception, e:
            print(e.message)

    @classmethod
    def get_exception(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
        # return 'EXCEPTION IN %s, LINE %s - %s : %'.format(filename, lineno, line.strip(), exc_obj)
