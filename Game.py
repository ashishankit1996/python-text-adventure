from Colors import colorprint
import os

def title():
    colorprint(
        '███████╗███████╗ █████╗ ██████╗ \n' + 
        '██╔════╝██╔════╝██╔══██╗██╔══██╗\n' +
        '█████╗  █████╗  ███████║██████╔╝\n' +
        '██╔══╝  ██╔══╝  ██╔══██║██╔══██╗\n' +
        '██║     ███████╗██║  ██║██║  ██║\n' +
        '╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝\n', 'green')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def resize(l, newsize, filling=None):                                                                                  
    if newsize > len(l):                                                                                 
        l.extend([filling for x in range(len(l), newsize)])                                                 
    else:                                                                                                
        del l[newsize:]
