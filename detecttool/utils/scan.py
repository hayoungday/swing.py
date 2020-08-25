from utils.parser import getter
from utils.engine.ruleset import Ruleset
import os
import pkg_resources

class scanner:
    def ruleadd(self,path):
        r = Ruleset()
        if 'json' in path:
            filepath = pkg_resources.resource_filename(__package__,path)            
            r.addrule(filepath)
        else:
            filelist = pkg_resources.resource_listdir(__package__,path)
            for p in filelist:
                p = path + p
                filepath = pkg_resources.resource_filename(__package__,p)
                r.addrule(filepath)
        return r

    def scan_import(self,node):
        if node is None:
            return
        r = self.ruleadd("rule/Import/Import.json")
        res = r.scan(node)
        return res

    def scan_def(self,node):
        if node is None:
            return
        func_call = []
        for i in node:
            func_call = getter.get_func_calls(node[i])
            r = self.ruleadd('rule/function/')
            res = r.scan(func_call)
        return res
