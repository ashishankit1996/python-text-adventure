from Colors import colorprint
import os

def title():
    colorprint(
        '____              ___                                      \n' +
        '`Mb(      db      )d\'                                     \n' +
        ' YM.     ,PM.     ,P                                       \n' +
        ' `Mb     d\'Mb     d\' ____    ___ ___  __ ___  __    __   \n' +
        '  YM.   ,P YM.   ,P  `MM(    )M\' `MM 6MM `MM 6MMb  6MMb   \n' +
        '  `Mb   d\' `Mb   d\'   `Mb    d\'   MM69 "  MM69 `MM69 `Mb\n' +
        '   YM. ,P   YM. ,P     YM.  ,P    MM\'     MM\'   MM\'   MM\n' +
        '   `Mb d\'   `Mb d\'      MM  M     MM      MM    MM    MM \n' +
        '    YM,P     YM,P       `Mbd\'     MM      MM    MM    MM  \n' +
        '    `MM\'     `MM\'        YMP      MM      MM    MM    MM \n' +
        '     YP       YP          M      _MM_    _MM_  _MM_  _MM_  \n' +
        '                         d\'                               \n' +
        '                     (8),P                                 \n' +
        '                      YMM                                  \n', 'red')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
