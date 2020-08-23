from termcolor import colored, cprint

class Output:
    def __init__(self):
        self.packagename=""

    def dect_end(self,import_dect,func_dect):
        print(end="\n\n")
        print(colored('import Detect','red'))
        for i in import_dect:
            print(i[1].description)
        print(end='\n\n')
        print(colored('Func Dectect','red'))
        for i in func_dect:
            print(i[1].description)
        print(end='\n\n')

    def print_packgename(self):
        print()
        print('==============', colored(self.packagename,'yellow'),'======================')
