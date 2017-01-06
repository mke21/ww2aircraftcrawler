#!/usr/bin/env python3
"""
Crawler that crawles the site
"""
from .parseindex import ParseIndexPage, ParseThreadPage

import requests

def walk_index(base, part):
    """
    walks a forum for url's
    base = "https://ww2aircraft.net/forum/" mind the trailing '/'
    part = rest of the forum adres
    """
    url = base + part
    while url:
        page_content = requests.get(url).text
        parser = ParseIndexPage(page_content)
        for c in parser.content():
            yield base, c['href']
        try:
            url = base + parser.next
        except TypeError:
            break


def walk_thread(base, part):
    """
    Walks thread and gets all posts
    returns list of posts
    """
    url = base + part
    result = []
    while url:
        page_content = requests.get(url).text
        parser = ParseThreadPage(page_content)
        result += [i for i in parser.content()]
        try:
            url = base + parser.next
        except TypeError:
            break
    return result
    
