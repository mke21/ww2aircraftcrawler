"""
Uses beautifulsoup to parse the stuff
"""
from bs4 import BeautifulSoup

from datetime import datetime


class ParsePageBase(object):
    """
    base class for parsing pages
    """

    def __init__(self, text):
        # remove all newlines from text
        # this makes it easier on the regex
        self.soup = BeautifulSoup(text, 'html.parser')

    @property        
    def next(self):
        """
        gets url of next page, returns none if last
        content must contain 'Next'
        """
        all = self.soup.find_all('a', class_='text')
        for a in all:
            if 'Next' in a.contents[0]:
                return a['href']
        else:
            return None


class ParseIndexPage(ParsePageBase):
    """
    parse index page
    """
    
    def content(self):
        """
        will list all threads on this page with url
        """
        for t in self.soup.find_all('h3', class_="title"):
            yield(
                {
                    'title': t.a.contents[0],
                    'href': t.a['href']
                }
            )
            

class ParseThreadPage(ParsePageBase):
    """
    parses thread page 
    """

    def convert_datetime(self, message):
        m = message.find('span', class_='DateTime').string
        return datetime.strptime(m, '%b %d, %Y')
    
    def get_text(self, message):
        s = message.find('blockquote', class_ = 'messageText')
        text = ''.join(
            s.find_all(text=True, recursive=False)
            ).replace(
                '\n', ' '
                )
        
        return text
        
    def content(self):
        """
        will get all posts on page and return a dictionary with 
        date, author, postno and textual content.
        """
        for message in self.soup.find_all('div', class_='messageInfo'):
            yield {
                'author': message.find('a', class_='author').string,
                'postno': message.find('a', class_='postNumber').string,
                'date': self.convert_datetime(message), # converts date
                'text': self.get_text(message),
                }
                
