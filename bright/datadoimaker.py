#!/usr/bin/env python3
import sys

import requests
from requests.auth import HTTPBasicAuth

__author__ = "Gareth Murphy"
__credits__ = ["Gareth Murphy"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Gareth Murphy"
__email__ = "garethcmurphy@gmail.com"
__status__ = "Development"


class DataDOIMaker(object):
    """XML metadata"""

    def __init__(self):
        self.deliverables = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10,
                             5.1, 5.2, 5.3, 5.4, 6.1, 6.2]

        # self.deliv_tags = [11, 12, 13, 14, 21, 22, 23, 24, 41, 42, 43, 44, 45, 46, 47, 49, 410, 54, 61, 62]
        self.deliv_tags = [11, 12, 13, 14]

        self.deliverable_dict = {
            '11': 'NMX0001',
            '12': 'MG0001',
            '13': 'MB0001',
            '14': 'SONDE0001'
        }
        self.passw = 'tbc'
        self.user = 'tbc'

        self.deliverable_title = {'11': 'Sample data from NMX testing',
                                  '12': 'Sample data from Multigrid testing',
                                  '13': 'Sample data from Multiblade testing',
                                  '14': 'Sample data from SONDE testing',
                                  '62': '6.2: Results of target group online survey '}

        self.deliverable_abstracts = {
            '11': 'This data was collected as part of BrightnESS, funded by the European Union Framework Programme for Research and Innovation Horizon 2020, under grant agreement 676548. It consists of test data for the NMX detector',
            '12': 'This data was collected as part of BrightnESS, funded by the European Union Framework Programme for Research and Innovation Horizon 2020, under grant agreement 676548. It consists of test data for the Multigrid detector',
            '13': 'This data was collected as part of BrightnESS, funded by the European Union Framework Programme for Research and Innovation Horizon 2020, under grant agreement 676548. It consists of test data for the Multiblade detector',
            '14': 'This data was collected as part of BrightnESS, funded by the European Union Framework Programme for Research and Innovation Horizon 2020, under grant agreement 676548. It consists of test data for the SONDE detector'
        }

    def f(self):
        for key, value in self.deliverable_dict.items():
            print(key, value)
        return 0

    def generate_xml(self, doi, title, abstract):
        xml = """<?xml version="1.0" encoding="UTF-8"?>

<resource xmlns="http://datacite.org/schema/kernel-4" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://datacite.org/schema/kernel-4 http://schema.datacite.org/meta/kernel-4/metadata.xsd">  
  <identifier identifierType="DOI">{0}</identifier>  
  <creators> 
    <creator> 
      <creatorName>Richter, Tobias</creatorName>  
      <givenName>Tobias</givenName>  
      <familyName>Richter</familyName>  
      <affiliation>ESS</affiliation> 
    </creator> 
  </creators>  
  <titles> 
    <title>{1}</title> 
  </titles>  
  <publisher>European Spallation Source ERIC</publisher>  
  <publicationYear>2015</publicationYear>  
  <descriptions> 
    <description xml:lang="en-us" descriptionType="TechnicalInfo">{1}</description>  
    <description xml:lang="en-us" descriptionType="Abstract">{2}</description> 
  </descriptions>  
  <resourceType resourceTypeGeneral="Text">Deliverable</resourceType> 
</resource>"""

        return xml.format(doi, title, abstract)

    def doi_url(self, doi, url):
        doi_url = 'doi={0}\nurl={1}'
        xdoi = doi_url.format(doi, url)
        print(xdoi)
        return xdoi.strip()

    def request_post(self, doi, title, abstract, url):
        xml = self.generate_xml(doi, title, abstract)

        print(xml)
        headers = {'Content-Type': 'application/xml;charset=UTF-8'}
        response = requests.post('https://mds.datacite.org/metadata', data=xml.encode('utf-8'), headers=headers,
                                 auth=HTTPBasicAuth(self.user, self.passw))
        print(str(response.status_code) + " " + response.text)

        doi_url = self.doi_url(doi, url)
        headers2 = {'Content-Type': 'text/plain;charset=UTF-8'}

        response2 = requests.post('https://mds.datacite.org/doi', data=doi_url.encode('utf-8'), headers=headers2,
                                  auth=HTTPBasicAuth(self.user, self.passw))
        print(str(response2.status_code) + " " + response2.text)
        # print(response)
        print(response2)

    def get_password(self):
        with open('/tmp/auth') as f:
            user = f.readline()
            password = f.readline()
        self.user = user.strip()
        self.passw = password.strip()
        print(self.user, self.passw)

    def make_doi(self, source_str):
        pos = 1
        insert_str = '.'
        tag2 = source_str[:pos] + insert_str + source_str[pos:]
        doi = '10.17199/BRIGHTNESS/' + source_str
        return doi


if __name__ == '__main__':

    print(sys.version)
    bright = DataDOIMaker()
    bright.get_password()
    bright.f()
    deliv = bright.deliv_tags

    for tag1 in deliv:
        tag = str(tag1)
        print(tag)
        doi = bright.make_doi(bright.deliverable_dict[tag])
        title = bright.deliverable_title[tag]
        abstract = bright.deliverable_abstracts[tag]
        url = "https://doi.esss.se/detail/" + str(tag)
        print('DOI: ', doi, '\nTitle: ', title, '\nAbstract: ', abstract, '\n URL', url)
        bright.request_post(doi, title, abstract, url)
