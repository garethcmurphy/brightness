#!/usr/bin/env python3
import requests

from requests.auth import HTTPBasicAuth


class Brightness(object):
    """XML metadata"""

    def __init__(self):
        self.deliverables = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10,
                             5.1, 5.2, 5.3, 5.4, 6.1, 6.2]

        self.deliverable_dict = {
            '11': 'agenda-and-minutes-general-assembly-kick-meeting',
            '12': 'data-management-plan',
            '13': '1st-agenda-and-minutes-yearly-general-assembly',
            '14': '2nd-agenda-and-minutes-yearly-general-assembly',
            '21': 'risk-assessment-and-mitigation-plan',
            '22': 'launch-ikc-best-practice-online-platform',
            '23': 'deployment-management-information-system',
            '24': '1st-annual-ikc-progress-assessment',
            '41': 'integration-plan-detector-readout',
            '410': 'test-technology-demonstrator',
            '42': 'counting-rate-capability',
            '43': 'natural-and-enriched-gadolinium-convertors-design',
            '44': 'report-engineering-design-brr-low-dimensional-moderator',
            '45': 'simulation-and-generic-multi-grid-design',
            '46': 'detector-characterisation',
            '47': 'report-conception-design-ess-and-brr-test-beamline',
            '49': 'detector-electronics-chain',
            '51': 'design-report-data-aggregator-software',
            '52': 'report-processing-choices-detector-types',
            '53': 'beta-version-data-aggregator-software',
            '54': 'report-filed-data-acquisition',
            '61': 'brightess-section-wwweuropeanspallationsourcesei',
            '62': 'results-target-group-online-survey'
        }
        self.password = 'tbc'
        self.user = 'tbc'

    def f(self):
        for key, value in self.deliverable_dict.items():
            print(key, value)
        return (0)

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
        doi_url = """{0} 
{1}"""
        return doi_url.format(doi, url)

    def request_post(self, doi, title, abstract, url):
        xml = self.generate_xml(doi, title, abstract);

        print(xml)
        headers = {'Content-Type': 'application/xml'}
        requests.post('https://mds.test.datacite.org/metadata', data=xml, headers=headers,
                      auth=HTTPBasicAuth(self.user, self.password))

        doi_url = self.doi_url(doi, url)
        requests.post('https://mds.test.datacite.org/metadata', data=doi_url, headers=headers,
                      auth=HTTPBasicAuth(self.user, self.password))

    def get_password(self):
        import itertools
        with open('/tmp/auth') as f:
            for user, password in itertools.izip_longest(*[f] * 2):
                print(user, password)
        self.user = user
        self.password = password


if __name__ == '__main__':
    bright = Brightness()
    bright.get_password()
    bright.f()
    doi = '10.17199/BRIGHTNESS.D5.2'
    title = 'test title'
    abstract = 'test abstract'
    url = 'www.test.com'
    bright.request_post(doi, title, abstract, url)
