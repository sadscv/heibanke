from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.heibanke.com/lesson/crawler_ex02'
# login_url = 'http://www.heibanke.com/accounts/login/'
login_url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent': agent
}

logindata = {
    'csrfmiddlewaretoken' : '',
    'username' : 'sadscv',
    'password' : 'sadsad',
}

postdata = {
    'csrfmiddlewaretoken' : '',
    'username' :'sadscv',
    'password' :'0'
    }

print('#'*80)




def login(session):
    p1 = session.get(url)
    p1_cookies = p1.cookies
    logindata['csrfmiddlewaretoken'] = p1_cookies['csrftoken']
    login_result = session.post(login_url, data = logindata, headers = headers, cookies = p1_cookies)
    if login_result.status_code == 200:
        print('login success')
    else:
        print('login fail')

    
def is_correct_num(session,num):
    postdata['password'] = str(num)
    p2 = session.get(url)
    p2_cookies = p2.cookies
    postdata['csrfmiddlewaretoken'] = p2_cookies['csrftoken']
    print('posting %s' % postdata)
    test_result = session.post(url, data = postdata, headers = headers, cookies = p2_cookies)
    soup = BeautifulSoup(test_result.text, 'html.parser')
    print('%s : %s' %(num, soup.h3.text))
    
    
session = requests.Session()
login(session)
for x in range(30):
    is_correct_num(session,x)

    
    # 学习了session的重要性