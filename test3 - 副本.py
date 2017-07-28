import requests
import re

login_data={'username':'sadscv','password':'sadsad'}
url='http://www.heibanke.com/lesson/crawler_ex02/'
login_url='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'

r2=requests.get(login_url)
c2=r2.cookies

login_data['csrfmiddlewaretoken']=c2['csrftoken']
r3=requests.post(login_url,data=login_data,allow_redirects=False,cookies=c2)
c3=r3.cookies

pass_data={'username':'tom','csrfmiddlewaretoken':c3['csrftoken']}
for passwd in range(31):
        print (passwd)
        pass_data['password']=passwd
        r5=requests.post(url,pass_data,cookies=c3)
        result=re.findall(r'密码错误',r5.text.encode('utf-8'))
        if not result:
                print (r5.text)
                break