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
        self.passw = 'tbc'
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
        doi_url = 'doi={0}\nurl={1}'
        xdoi = doi_url.format(doi, url)
        print(xdoi)
        return xdoi.strip()

    def request_post(self, doi, title, abstract, url):
        xml = self.generate_xml(doi, title, abstract);

        print(xml)
        headers = {'Content-Type': 'application/xml;charset=UTF-8'}
        # response = requests.post('https://mds.datacite.org/metadata', data=xml.encode('utf-8'), headers=headers,
        #                         auth=HTTPBasicAuth(self.user, self.passw))

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


if __name__ == '__main__':
    bright = Brightness()
    bright.get_password()
    bright.f()
    doi = '10.17199/BRIGHTNESS.D5.2'
    title = '5.2: Report processing choices for detector types'
    abstract = 'Task 5.1 Creating a standard neutron event data stream for different detector types focuses on software event processing for the expected ESS detector suite. This will deliver generic neutron event information required for scientific experiments. Deliverable 5.2, which presents the results of our investigations in this task, shows that we are in a good position to cope with the processing needs of the different detector types once their configuration is final. For the future of the BrightnESS task, we see no unusual or high impact risks. For the majority of cases, specifications of upcoming detectors and their raw output format are not yet in a state that allows software prototyping. However, during the course of the project thus far, we have developed a good working relationship with the detector group and their partner institutes across Europe. That resulted in a good understanding of the domain and, not least, to two working prototypes of the event formation system for NMX and the Multi-Grid detector ahead of schedule. These two detector systems are a good template for future customized implementations. Most systems are quite similar to the Multi-Grid detector, and with NMX we are close to covering the most complex computational needs. To drive these working prototypes forward, we have put in place a common and modular framework. It hosts the detector-type specific processing algorithms whereby future tasks are divided into manageable modular chunks. With the tools developed, we are confident that we can adapt our processing algorithms and parameters in sync with any new hardware prototypes that become available, any updates to prototype detectors and production versions. We will be able to review quality indicators for individual events, statistics within and across datasets and interactively examine the effect of different filters or code changes. The software will also enable the specialist from ESS’ Data Management and Software Centre (DMSC) or the ESS detector group to fine-tune the event processing pipeline, change detector architecture and varying user needs, and will serve as commissioning and calibration tools.'
    url = 'https://brightness.esss.se/about/deliverables/52-report-processing-choices-detector-types'
    bright.request_post(doi, title, abstract, url)
