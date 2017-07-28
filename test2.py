from bs4 import BeautifulSoup
import requests
import json
import logging

url = 'http://www.heibanke.com/lesson/crawler_ex01/'
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent': agent
}
  
postdata = {
    'csrfmiddlewaretoken' : 'Yw0LEOktxaa06SkFoSKtnu2p7kfmVJDh',
    'username' : 'sadscv',
    'password' : '0',
}

def is_correct_password(password):
    session = requests.session()  
    postdata['password'] = password
    login_page = session.post(url, data = postdata, headers = headers)
    soup = BeautifulSoup(login_page.text, 'html.parser')
    print(soup.h3)
    result = '您输入的密码错误, 请重新输入'
    # print(soup.h3.get_text())
    if (soup.h3.get_text() != result):
        return True
    else:
        return False
        
        
for x in range(30):
    print( '%s:%s' % (x, is_correct_password(str(x))))
    
    

