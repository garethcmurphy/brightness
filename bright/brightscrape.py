#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup

from . import brightness

import pprint

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
            url = self.bright_url + key + "-" + value
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            my_divs = soup.findAll("div", {"class": field_name})
            try:
                abstract = (" ".join(my_divs[0].strings))
            except IndexError:
                abstract = ' '
            abstract.strip('"')

            self.deliverable_abstracts[key] = abstract

        pprint.PrettyPrinter(indent=4)
        print(self.deliverable_abstracts)

    def scrape_title(self):
        for key, value in self.deliverable_titles.items():
            url = self.bright_url + key + "-" + value
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            my_divs = soup.findAll("title")
            try:
                abstract = (" ".join(my_divs[0].strings))
            except IndexError:
                abstract = ' '
            abstract.strip('"')

            self.deliverable_abstracts[key] = abstract

        pprint.PrettyPrinter(indent=4)
        print(self.deliverable_abstracts)


if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrape_title()
    search_field_name = "field field-name-body"
    scrape.scrape(search_field_name)
