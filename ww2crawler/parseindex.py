"""
Uses beautifulsoup to parse the stuff
"""
from bs4 import BeautifulSoup




class ParseIndexPage(object):
    """
    parse index page
    """
    
    def __init__(self, text):
        # remove all newlines from text
        # this makes it easier on the regex
        self.soup = BeautifulSoup(text, 'html.parser')

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

    
