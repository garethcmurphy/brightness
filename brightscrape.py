#!/usr/bin/env python3
import requests

from bs4 import BeautifulSoup


class Scrape(object):
    """XML metadata"""

    def __init__(self):
        self.page = "test"

    def scrape(self):
        page = requests.get("https://brightness.esss.se/about/deliverables/53-beta-version-data-aggregator-software")
        print(page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify())
        mydivs = soup.findAll("div", {"class": "field field-name-body"})
        print(mydivs)


if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrape()
