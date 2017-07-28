from bs4 import BeautifulSoup
import requests
import time

class Test(object):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.heibanke.com",
        "Upgrade-Insecure-Requests": "1",
    }
    
    HOME_URL = 'http://www.heibanke.com/lesson/crawler_ex00/'
    LOGIN_URL = ''
    
    def __init__(self):
        self.__session = requests.Session()
        self.__session.headers = self.headers
    
    def login(self):
        pass
    
    def open(self, url, delay=0, timeout=10):
        if delay:
            time.sleep(delay)
        return self.__session.get(url, timeout=timeout)
     
    def getSession(self):
        pass
        
    def getNext(self, num):
        html = self.HOME_URL + str(num)
        content = self.open(html)
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.h3.get_text()[12:17]
        # print(self.ifNum(result))
        print(soup.h3.get_text())
        return result
        
    def ifNum(self, num):
        try:
            int(num)
            return int(num)
        except ValueError: 
            return ('okay. u got it')
            
        
        
def main():
    if __name__ == '__main__':
        next = ''
        for i in range(100):
            next = Test().getNext(next)
        
        
main()