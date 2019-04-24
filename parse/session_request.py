import requests

def save_file(file, content):
    """保存到文件中去"""

    try:
        with open(file, 'w', encoding="utf-8") as f:
            f.write(content)

            print("完成")
    except OSError as r:
        print("打开文件出错了,原因是：", r)


session=requests.Session()
data={"email":'','password':''}
url='http://www.renren.com/PLogin.do'
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}
r=session.post(url,data=data)
# print(r.cookies)
# a=requests.utils.dict_from_cookiejar(r.cookies)
url_user='http://www.renren.com/970482943'
re2=session.get(url_user).content.decode()
# 970482943

save_file("renren.html",re2)

url3='http://www.renren.com/970482943/profile'
r3=session.get(url3).content.decode()
# 970482943
save_file("renren3.html",r3)







