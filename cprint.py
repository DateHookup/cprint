# Variables
#-----------------------------------------------------------------------------#

version = (0,0,1)

esc = '\033['
reset = esc + '0m'

colors = { 'black'  : esc + '30m'
         , 'red'    : esc + '31m'
         , 'green'  : esc + '32m'
         , 'yellow' : esc + '33m'
         , 'blue'   : esc + '34m'
         , 'magenta': esc + '35m'
         , 'cyan'   : esc + '36m'
         , 'white'  : esc + '37m'
         }

# Functions
#-----------------------------------------------------------------------------#

def cprint (text, color):
    code = colors.get(color)
    print(code + text + reset if code else text)

def black   (text): cprint(text, 'black')
def red     (text): cprint(text, 'red')
def green   (text): cprint(text, 'green')
def yellow  (text): cprint(text, 'yellow')
def blue    (text): cprint(text, 'blue')
def magenta (text): cprint(text, 'magenta')
def cyan    (text): cprint(text, 'cyan')
def white   (text): cprint(text, 'white')

# Main
#-----------------------------------------------------------------------------#

if __name__ == '__main__': 
    for color in colors.keys(): cprint(color, color)
