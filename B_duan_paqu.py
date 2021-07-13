import requests       # self.url,指的是从初始化函数那   引用url这个变量  别的同理
from urllib.parse import urlsplit

class Download(object):

    def __init__(self):
        self.session = requests.session()
        self.session.verify = False   # 取消请求验证，主要针对https请求，过滤掉https
        self.session.headers.update({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) App leWebKit/537.36 (KHTML, like Gecko)"
                              "Chrome/81.0.4044.138 Safari/537.36",
            })

    def login(self, user, pwd):
        url = "http://p.le1bao.com/Home/LoginAjax"
        data = {
            "mobile": user,
            "password": pwd,
            "rememberPassword": True
        }
        self.session.headers.update({"Host": urlsplit(url).netloc})
        response = self.session.post(url, data=data)
        response.encoding = "utf-8"
        # print(response.text)

    def loop_page(self, page):
        url = "http://p.le1bao.com/Organization/CustomerListForAjax"
        data = {'Paging.PageIndex': page}
        res = self.session.post(url=url, data=data)
        new_res = res.json()      # new_res = json.loads(res.text)
        CustomerList = new_res['data']['list']
        CustomerPages = new_res['data']['pages']
        return CustomerList, CustomerPages

    def run(self):
        self.login(user="15201688501", pwd="123456")
        res_list_1, total_page = self.loop_page(1)
        for new_res_list_1 in res_list_1:
            print('电话：', new_res_list_1['Mobile'])
            print('姓名：', new_res_list_1['RealName'])
            print()
        for i in range(2, total_page + 1):
            response = self.loop_page(i)
            for list_response in response[0]:
                print('电话：', list_response['Mobile'])
                print('姓名：', list_response['RealName'])
                print()


        print("总共%s页" % total_page)
Download().run()













