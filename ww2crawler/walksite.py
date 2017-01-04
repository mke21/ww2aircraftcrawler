#!/usr/bin/env python3
"""
Crawler that crawles the site
"""
from .parseindex import ParseIndexPage, ParseThreadPage

import requests

def threat_urls(base, part):
    url = base + part
    while url:
        page_content = requests.get(url).text
        parser = ParseIndexPage(page_content)
        for c in parser.content():
            yield base+c['href']
        try:
            url = base + parser.next
        except TypeError:
            break
