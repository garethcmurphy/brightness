#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup

from brightness import Brightness

import pprint


class Scrape(object):
    """XML metadata"""

    def __init__(self):
        self.page = "test"
        self.deliv_abstracts = {}

    def scrape(self, field_name):
        bright = Brightness()
        deliv = bright.deliverable_dict
        for key, value in deliv.items():
            url = "https://brightness.esss.se/about/deliverables/" + key + "-" + value
            print(url)
            page = requests.get(url)
            # print(page.status_code)
            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup.prettify())
            mydivs = soup.findAll("div", {"class": field_name})
            # print(mydivs)
            try:
                abstract = (" ".join(mydivs[0].strings))
            except IndexError:
                abstract = mydivs
                abstract = ' '
            abstract.strip('"')
            # print(abstract)

            self.deliv_abstracts[key] = abstract
            # x= ''.join(BeautifulSoup(mydivs[0], "html.parser").find_all(text=True))
            # print (key, x)

        pp = pprint.PrettyPrinter(indent=4)
        print(self.deliv_abstracts)

    def scrape_title(self):
        bright = Brightness()
        deliv = bright.deliverable_dict
        for key, value in deliv.items():
            url = "https://brightness.esss.se/about/deliverables/" + key + "-" + value
            print(url)
            page = requests.get(url)
            # print(page.status_code)
            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup.prettify())
            mydivs = soup.findAll("title")
            # print(mydivs)
            try:
                abstract = (" ".join(mydivs[0].strings))
            except IndexError:
                abstract = mydivs
                abstract = ' '
            abstract.strip('"')
            # print(abstract)

            self.deliv_abstracts[key] = abstract
            # x= ''.join(BeautifulSoup(mydivs[0], "html.parser").find_all(text=True))
            # print (key, x)

        pp = pprint.PrettyPrinter(indent=4)
        print(self.deliv_abstracts)


if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrape_title()
    field_name = "field field-name-body"
    scrape.scrape(field_name)
