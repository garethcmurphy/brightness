#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup

from brightness import Brightness


class Scrape(object):
    """XML metadata"""

    def __init__(self):
        self.page = "test"

    def scrape(self):
        bright = Brightness()
        deliv = bright.deliverable_dict
        for key, value in deliv.items():
            url = "https://brightness.esss.se/about/deliverables/" + key + "-" + value
            print(url)
            page = requests.get(url)
            #print(page.status_code)
            soup = BeautifulSoup(page.content, 'html.parser')
            #print(soup.prettify())
            mydivs = soup.findAll("div", {"class": "field field-name-body"})
            print(mydivs)
            #x= ''.join(BeautifulSoup(mydivs[0], "html.parser").find_all(text=True))
            #print (key, x)



if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrape()
