#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
try:
    from intent import Loki_temperature
    from intent import Loki_ice
    from intent import Loki_size
    from intent import Loki_item
    from intent import Loki_sugar
except:
    from .intent import Loki_temperature
    from .intent import Loki_ice
    from .intent import Loki_size
    from .intent import Loki_item
    from .intent import Loki_sugar


#LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
#USERNAME = ""
#LOKI_KEY = ""

import json
    
with open('account.info', encoding='utf-8') as f:
    accountDICT = json.loads(f.read())
    
    
LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["loki_project_key"]

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # temperature
                if lokiRst.getIntent(index, resultIndex) == "temperature":
                    resultDICT = Loki_temperature.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ice
                if lokiRst.getIntent(index, resultIndex) == "ice":
                    resultDICT = Loki_ice.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # size
                if lokiRst.getIntent(index, resultIndex) == "size":
                    resultDICT = Loki_size.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # item
                if lokiRst.getIntent(index, resultIndex) == "item":
                    resultDICT = Loki_item.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # sugar
                if lokiRst.getIntent(index, resultIndex) == "sugar":
                    resultDICT = Loki_sugar.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # temperature
    #print("[TEST] temperature")
    #inputLIST = ['溫','熱','冰紅茶不要冰','錫蘭紅茶大杯','熱錫蘭紅茶大杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','錫蘭紅茶大杯少糖少冰','一杯錫蘭紅茶和烏龍綠茶','兩杯熱的錫蘭紅茶甜度冰塊正常','原鄉兩杯一杯半糖少冰一杯全糖正常冰']
    #testLoki(inputLIST, ['temperature'])
    #print("")

    # ice
    #print("[TEST] ice")
    #inputLIST = ['微微','冰紅茶不要冰','錫蘭紅茶大杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','錫蘭紅茶大杯少糖少冰','一杯錫蘭紅茶和烏龍綠茶','特選普洱不要加糖跟冰塊','兩杯熱的錫蘭紅茶甜度冰塊正常','原鄉兩杯一杯半糖少冰一杯全糖正常冰']
    #testLoki(inputLIST, ['ice'])
    #print("")

    # size
    #print("[TEST] size")
    #inputLIST = ['普洱微微','冰紅茶不要冰','錫蘭紅茶大杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','錫蘭紅茶大杯少糖少冰','一杯錫蘭紅茶和烏龍綠茶','兩杯熱的錫蘭紅茶，甜度冰塊正常','原鄉兩杯一杯半糖少冰一杯全糖正常冰']
    #testLoki(inputLIST, ['size'])
    #print("")

    # item
    #print("[TEST] item")
    #inputLIST = ['普洱微微','冰紅茶不要冰','錫蘭紅茶大杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','錫蘭紅茶大杯少糖少冰','一杯錫蘭紅茶和烏龍綠茶','特選普洱不要加糖跟冰塊','兩杯熱的錫蘭紅茶，甜度冰塊正常','原鄉兩杯一杯半糖少冰一杯全糖正常冰']
    #testLoki(inputLIST, ['item'])
    #print("")

    # sugar
    #print("[TEST] sugar")
    #inputLIST = ['微微','都不要糖','都去冰半糖','一杯半糖少冰','冰紅茶不要冰','錫蘭紅茶大杯','一杯大冰綠半糖少冰','我要菁茶半糖不要冰塊','錫蘭紅茶大杯少糖少冰','一杯錫蘭紅茶和烏龍綠茶','特選普洱不要加糖跟冰塊','兩杯熱的錫蘭紅茶甜度冰塊正常','原鄉兩杯一杯半糖少冰一杯全糖正常冰']
    #testLoki(inputLIST, ['sugar'])
    #print("")
    
    from ArticutAPI import Articut
    articut = Articut(username=accountDICT["username"], apikey=accountDICT["apikey"])
        
    # 輸入其它句子試看看
    #inputLIST = ["我要菁茶，半糖不要冰塊"]
    #inputLIST = ["冰紅茶不要冰"]
    #inputLIST = ["兩杯大冰紅半糖少冰"]
    #inputLIST = ["一杯錫蘭紅茶和烏龍綠茶"]
    inputLIST = ["普洱微微"]
    #inputLIST = ["特選普洱不要加糖跟冰塊"]
    #inputLIST = ["兩杯熱的錫蘭紅茶，甜度冰塊正常"]
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    
    for a in range(0, len(resultDICT["amount"])):
        articutLv3ResultDICT = articut.parse(resultDICT["amount"][a], level="lv3")
        amount = articutLv3ResultDICT["number"][resultDICT["amount"][a]]
        resultDICT["amount"][a] = amount
    print("Result => {}".format(resultDICT))
    
    if("不確定") in resultDICT["ice"]:
        print("哈囉~飲料不能又冷又熱的，你是要冰的還是熱的?")
    elif("不確定") in resultDICT["sugar"]:
        print("哈囉~甜度可以請你再說一次嗎?")
    else:    
        print("\n您點的是：")
        for k in range(len(resultDICT["amount"])):
            print("{} x {} ( {}、{} )".format(resultDICT["item"][k], resultDICT["amount"][k], resultDICT["sugar"][k], resultDICT["ice"][k]))