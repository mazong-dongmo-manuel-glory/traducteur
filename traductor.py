import requests
import json
class Traductor:
    def __init__(self,text,first,second):
        self.text = str(text)
        self.first = str(first)
        self.second = str(second)
        self.key = "trnsl.1.1.20200524T135627Z.66b8ab01df9d01c6.1b0104e2e13ddc7343b3704ee6525dbed2a02147"
        self.Parse()
    def Parse(self):
        if len(self.first)>2:
            self.first = self.first[:2]
        if len(self.second)>2:
            self.second = self.second[:2]
    def trans(self):
        self.req =f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={self.key}&text={self.text}&lang={self.first}-{self.second}"
        self.res = requests.get(self.req).content
        self.res = json.loads(self.res)
        return self.res