import urllib2
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re

#class for storing the info about a youtube page
#strings stored in unicode
#html characters resolved to unicode characters

class YoutubePage:
    def __init__(self,url):
        self.url = url
        self.title = None
        self.description = None
        self.page_html = self.get_page()
        self.set_info()
    
    #read page into html
    def get_page(self):
        try:
            page = urllib2.urlopen(self.url)
            page_html = page.read()
            return page_html
        except urllib2.HTTPError, e:
            print(e.code)
            return None
        except urllib2.URLError, e:
            print(e.code)
            return None
    
    #get information about youtube page
    #sets self.title and self.description
    def set_info(self):
        #if we couldn't parse page, set everything to None
        if(self.page_html == None):
            self.title = None
            self.description = None
            return

        #parse with BeautifulSoup
        soup = BeautifulSoup(self.page_html)
        title_list = soup.select('meta[name="title"]')
        if(len(title_list)>0):
            self.title = title_list[0]['content']
        else:
            self.title = None
        
        description_list = soup.select('meta[name="description"]')
        if(len(description_list)>0):
            self.description = description_list[0]['content']
        else:
            self.description = None

def youtube_url(url_string):
    """
    if the string contains a youtube url, it returns that url
    it strips out https and parentheses used in reddit's markup
    for example, if url_string = "(https://www.youtube.com/watch?v=asdfasdf)",
    it will return "http://www.youtube.com/watch?v=asdfasdf"

    :param url_string: a string
    """
    youtube_pattern = r'(?:http://|https://)?(www.youtube.com/watch\?v=[a-zA-Z0-9_\-]*)'
    match = re.search(youtube_pattern, url_string)
    if not match:
        return None
    else:
        return 'http://' + match.group(1)

        

if(__name__ == "__main__"):
    youtube = YoutubePage('https://www.youtube.com/watch?v=1SCMZWyJy2Y')
    print(youtube.title)
    print(youtube.description)