from utils.engine.rule import Rule
import json


class Ruleset:
    def __init__(self):
        self.listrule = list()

    def addrule(self, path):
        with open(path, 'r')as jsonfile:
            datas = json.load(jsonfile)
        for data in datas:
            r = Rule()
            r.name = data['name']
            r.description = data['Description']
            r.severity = data['Severity']
            r.expression = data['expression']
            self.listrule.append(r)

    def scan(self, dic):
        detect = []
        for i in dic:
            tmp = []
            for r in self.listrule:
                t = r.scan(i)
                if t:
                    s = {i: dic[i]}
                    tmp.append(s)
                    tmp.append(r)
                    detect.append(tmp)
                    break
        return detect
