import json
import os
from pprint import pprint

import requests


class Db():


    def __init__(self,  path=''):
        self.path = path

        # self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(theme)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def get_url_list(self):
        url_list = []
        for i in range(0, 100):
            url_list.append(self.url + "&pn=" + str(i * 50))
        return url_list

    def hd(self, headers):
        """处理文件头"""
        a = headers.strip('\n')
        try:
            l = a.split("\n")
            l1 = []
            l2 = []
            head = dict()

            for each in l:
                key = each.split(":")[0].strip()
                val = each.split(":", maxsplit=1)[1].strip()
                head[key] = val

            return head
        except:
            print("输入的header有错误")

    def parse_url(self, url):
        r = requests.get(url)
        return r.content.decode()

    def make_dir(self):
        """如果文件夹不存在则新建"""
        if not self.path:
            return ""
        dir = self.path
        if not os.path.exists(dir):
            os.mkdir(dir)

    def save_file(self, file, content):

        """保存到文件中去"""


        try:
            with open(file, 'w', encoding="utf-8") as f:
                f.write(content)

                print("完成")
        except OSError as r:
            print("打开文件出错了,原因是：", r)

    def run(self):
        """1获得贴吧网址列表"""
        h="""Host: m.toutiao.com
                Connection: keep-alive
                User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
                Accept: */*
                Referer: https://m.toutiao.com/
                Accept-Encoding: gzip, deflate, br
                Accept-Language: zh-CN,zh;q=0.9
                Cookie: UM_distinctid=16a390fbeff670-002488f6c2c90d-3e7e045d-100200-16a390fbf006cc; tt_webid=6681829763000714763; csrftoken=b03b347143a7861317ef549587fddfb8; W2atIF=1; _ga=GA1.2.722972698.1555735507; _gid=GA1.2.984200046.1555735507; _ba=BA0.2-20190420-51225-9WKXCNZzyqaNzN9nq81Y; __tasessionId=4lj0pv93c1555735545546"""
        url="https://m.toutiao.com/list/?count=20&format=json_raw&as=A1C57C8B8A0A3F9"
        headers=self.hd(h)


        reponse=requests.get(url=url,headers=headers)
        re_content=reponse.content.decode()
        a=json.loads(re_content)
        pprint(a)  # pprint打印美化
        # print(type(a))
        # b=json.dumps(a,ensure_ascii=False,indent=4)
        with open("jrtt2.txt","w",encoding="utf-8") as f:
            json.dump(a,f,ensure_ascii=False,indent=4)




if __name__ == '__main__':
    t = Db(path="./dd")
    t.run()
