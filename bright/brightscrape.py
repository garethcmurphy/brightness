#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup

from . import brightness

import pprint


class Scrape(object):
    """XML metadata"""

    def __init__(self):
        self.page = "test"
        self.deliv_abstracts = {}
        self.bright = brightness.Brightness()
        self.deliv = self.bright.deliverable_dict
        self.bright_url = "https://brightness.esss.se/about/deliverables/"

    def scrape(self, field_name):
        for key, value in self.deliv.items():
            url = self.bright_url + key + "-" + value
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            mydivs = soup.findAll("div", {"class": field_name})
            try:
                abstract = (" ".join(mydivs[0].strings))
            except IndexError:
                abstract = ' '
            abstract.strip('"')

            self.deliv_abstracts[key] = abstract

        pp = pprint.PrettyPrinter(indent=4)
        print(self.deliv_abstracts)

    def scrape_title(self):
        for key, value in self.deliv.items():
            url = self.bright_url + key + "-" + value
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            mydivs = soup.findAll("title")
            try:
                abstract = (" ".join(mydivs[0].strings))
            except IndexError:
                abstract = ' '
            abstract.strip('"')

            self.deliv_abstracts[key] = abstract

        pp = pprint.PrettyPrinter(indent=4)
        print(self.deliv_abstracts)


if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrape_title()
    field_name = "field field-name-body"
    scrape.scrape(field_name)
