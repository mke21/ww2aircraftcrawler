"""
Uses beautifulsoup to parse the stuff
"""
from bs4 import BeautifulSoup


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
        a = self.soup.find('a', class_='text')
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
            

class ParseThreadPage(object):
    """
    parses thread page 
    """

    def __init__(self, text):
        self.soup = BeautifulSoup(text, 'html.parser')
        
