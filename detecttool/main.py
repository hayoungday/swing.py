import sys
import ast
import subprocess
from utils import *
from utils.output import Output
from utils.parser import getter

def setup(pakagename):
    pypirul = "https://pypi.org/pypi/"+pakagename+"/json"
    pypi_content = crawl.getcontent(pypirul, False)
    if pypi_content is None:
        m = f"{pakagename} does not exits"
        print(m)
        return
    url, filename, filetype = crawl.gettar(pypi_content) 
    content = crawl.getcontent(url, True)
    if content is None:
        m = f"{pakagename} does not exits"
        return
    filename = f'{filename}/setup.py'
    setupfile = crawl.getsetup(content,filename,filetype)
    if setupfile is None:
        return
    return setupfile


def getnode(content):
    node = ast.parse(content)
    import_dic = getter.get_import(node)
    func_def = getter.get_func(node)
    class_def = getter.get_class(node)
    ##func_def and class_def Deduplication
    for key in class_def :
        tmp=getter.get_func(class_def[key])
        ts = set(func_def.items())^set(tmp.items())
        func_def = dict(ts)
    return import_dic,func_def, class_def

def getscan(import_dic,func_def,class_def):
    s = scan.scanner()
    import_dect = s.scan_import(import_dic)
    if len(import_dect)==0:
        return [],[]
    func_dect = s.scan_def(func_def)
    tmp = s.scan_def(class_def)
    if len(tmp)>0:
        func_dect.append(tmp)
    return import_dect, func_dect


def install(packagename):
    print(f'No items detected in {packagename}')
    print("Start Install")
    subprocess.check_call([sys.executable, "-m", "pip", "install", packagename])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Package name is not entered")
        sys.exit()
    packagename = sys.argv[1]
    o = Output()
    o.packagename=packagename
    o.print_packgename()
    setuppy = setup(packagename)
    if setuppy is None :
        sys.exit()
    import_dic, func_def, class_def = getnode(setuppy)
    if len(import_dic)+len(func_def)+len(class_def) == 0:
        install(packagename)
        sys.exit()
    import_dect, func_dect = getscan(import_dic,func_def,class_def)
    if len(import_dect)+len(func_dect)==0:
        install(packagename)
        sys.exit()
    else:
        o.dect_end(import_dect,func_dect)
