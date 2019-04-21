import os
import requests


class Tieba():


    def __init__(self, theme, path=''):
        self.path = path
        self.theme = theme
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(theme)
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
        url_list = self.get_url_list()
        self.make_dir()

        for url in url_list:
            content = self.parse_url(url)
            # save content
            filename = "tb{}_page{}.html".format(self.theme, url_list.index(url) + 1)
            file_path = os.path.join(self.path, filename)
            self.save_file(file_path, content)


if __name__ == '__main__':
    t = Tieba("python",path="./dd")
    t.run()
