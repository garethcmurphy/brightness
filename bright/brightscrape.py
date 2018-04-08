#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

from ..bright import brightness

__author__ = "Gareth Murphy"
__credits__ = ["Gareth Murphy"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Gareth Murphy"
__email__ = "garethcmurphy@gmail.com"
__status__ = "Development"


class Scrape(object):
    """XML metadata"""

    def __init__(self):
        self.page = "test"
        self.deliverable_abstracts = {}
        self.bright = brightness.Brightness()
        self.deliverable_titles = self.bright.deliverable_dict
        self.bright_url = "https://brightness.esss.se/about/deliverables/"

    def scrape(self, field_name):
        for key, value in self.deliverable_titles.items():
            soup = self.get_page(key, value)
            my_divs = soup.findAll("div", {"class": field_name})
            self.get_abstract(key, my_divs)

    def get_page(self, key, value):
        url = self.bright_url + key + "-" + value
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def get_abstract(self, key, my_divs):
        try:
            abstract = (" ".join(my_divs[0].strings))
        except IndexError:
            abstract = ' '
        abstract.strip('"')
        self.deliverable_abstracts[key] = abstract

    def scrape_title(self):
        for key, value in self.deliverable_titles.items():
            soup = self.get_page(key, value)
            my_divs = soup.findAll("title")
            self.get_abstract(key, my_divs)


if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrape_title()
    print(scrape.deliverable_abstracts)
    search_field_name = "field field-name-body"
    scrape.scrape(search_field_name)
    print(scrape.deliverable_abstracts)
