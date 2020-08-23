import re


class Rule:
    def __init__(self):
        self._name = ""
        self._description = ""
        self._severity = ""
        self._expression = {}

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property    
    def severity(self):
        return self._severity

    @property
    def expression(self):
        return self._expression

    @name.setter
    def name(self, text):
        self._name = text

    @description.setter
    def description(self, text):
        self._description = text

    @severity.setter
    def severity(self, text):
        self._severity = text

    @expression.setter
    def expression(self, expr):
        self._expression = dict(expr[0])

    def scan(self, text):
        if self._expression["type"] == "regx":
            pattern = re.compile(self._expression['expr'])
            m = pattern.search(text)
            if m is not None:
                return True
            else:
                return False
        elif self._expression["type"] == "string":
            pattern = self._expression['expr']
            if pattern in text:
                return True
            else:
                return False
