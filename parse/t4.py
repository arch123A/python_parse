import json
import pprint
with open("jrtt.txt","r",encoding="utf-8") as f:
    dic=json.load(f,encoding="utf-8")
    print(dic)
    print(type(dic))