#!/usr/bin/env python3
import requests


class Brightness(object):
    """XML metadata"""
    deliverables = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 5.1, 5.2,
                    5.3, 5.4, 6.1, 6.2]

    deliverable_dict = {
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

    def f(self):
        for key,value in self.deliverable_dict.items():
            print(key, value)
        return (0)

    def request_post(self):
        xml = """my xml"""
        headers = {'Content-Type': 'application/xml'}
        requests.post('http://www.my-website.net/xml', data=xml, headers=headers)


if __name__ == '__main__':
    bright = Brightness()
    bright.f()
