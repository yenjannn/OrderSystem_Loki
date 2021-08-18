#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for item

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_item = True
userDefinedDICT = {"hot": ["常溫", "溫飲", "熱飲", "燙"], "ice": ["冰", "正常冰", "少冰", "微冰", "去冰", "不要冰塊", "溫", "熱", "常溫", "溫飲", "熱飲", "不要加冰塊", "不加冰塊", "不加冰", "不要冰"], "size": ["大", "中"], "sugar": ["無糖", "微糖", "半糖", "少糖", "全糖", "正常糖", "零分糖", "二分糖", "五分糖", "八分糖", "0分糖", "2分糖", "5分糖", "8分糖", "零分", "二分", "五分", "八分", "0分", "2分", "5分", "8分", "不要糖", "不要加糖", "不加糖", "糖"], "原鄉四季": ["四季", "四季春", "原鄉", "四季茶", "四季春茶", "原鄉茶", "原鄉四季茶", "原鄉四季春茶", "原四季春茶", "四季元鄉"], "極品菁茶": ["極品菁", "菁茶", "極菁", "極菁茶"], "烏龍綠茶": ["烏龍", "烏龍綠", "烏"], "特級綠茶": ["綠茶", "綠", "特綠"], "特選普洱": ["特選普洱茶", "普洱", "普洱茶", "特普", "特級普洱茶", "特級普洱"], "翡翠烏龍": ["翡翠烏", "翡翠烏龍茶", "翡翠烏茶", "翡翠烏龍綠", "翡翠烏綠", "翠烏", "翠烏茶", "翡烏", "翡烏茶", "烏龍"], "錫蘭紅茶": ["錫蘭", "錫蘭紅", "紅茶", "錫茶", "蘭茶", "紅"], "嚴選高山茶": ["高山", "高山茶", "嚴選高山", "嚴選高"]}

itemLIST = userDefinedDICT["烏龍綠茶"] + userDefinedDICT["錫蘭紅茶"] + userDefinedDICT["特級綠茶"] + userDefinedDICT["極品菁茶"] + userDefinedDICT["原鄉四季"] + userDefinedDICT["特選普洱"] + userDefinedDICT["翡翠烏龍"] + userDefinedDICT["嚴選高山茶"]
itemLIST = itemLIST + ["烏龍綠茶", "特級綠茶", "錫蘭紅茶", "極品菁茶", "原鄉四季", "特選普洱", "翡翠烏龍", "嚴選高山茶"]

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_item:
        print("[item] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["item"] = []
    resultDICT["amount"] = []
    
    if utterance == "[一杯][大][冰][綠][半糖][少冰]":
        if args[3] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[3] in userDefinedDICT[k]:                     
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append(args[0])
                elif args[3] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append(args[0])                    

    if utterance == "[我]要[菁茶][半糖][不要冰塊]":
        if args[1] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[1] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")
                elif args[1] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")                   

    if utterance == "[普洱]微微":
        if args[0] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")
                elif args[0] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")                   


    if utterance == "[特選普洱][不要加糖]跟[冰]塊":
        if args[0] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")
                elif args[0] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")            


    if utterance == "[錫蘭紅茶][大]杯":
        if args[0] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")
                elif args[0] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")                   


    if utterance == "[錫蘭紅茶][大]杯[少糖][少冰]":
        if args[0] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")
                elif args[0] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")                   


    if utterance == "[一杯][錫蘭紅茶]和[烏龍綠茶]":
        for a in args[1:3]:
            if a in itemLIST:
                for k in userDefinedDICT.keys():
                    if a in userDefinedDICT[k]:                
                        resultDICT["item"].append(k)
                        resultDICT["amount"].append(args[0])
                    elif a == k:
                        resultDICT["item"].append(k)
                        resultDICT["amount"].append(args[0])                       

    if utterance == "[兩杯][熱]的[錫蘭紅茶]，[甜度][冰]塊[正常]":
        if args[2] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[2] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append(args[0])
                elif args[2] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append(args[0])                   

    if utterance == "[原鄉][兩杯][一杯][半糖][少冰][一杯][全糖][正常冰]":
        if args[0] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append(args[1])
                elif args[0] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append(args[1])                   

    if utterance == "冰[紅茶][不要冰]":
        if args[0] in itemLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")
                elif args[0] == k:
                    resultDICT["item"].append(k)
                    resultDICT["amount"].append("1")                   


    return resultDICT