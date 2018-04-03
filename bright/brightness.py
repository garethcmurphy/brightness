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


class Brightness(object):
    """XML metadata"""

    def __init__(self):
        self.deliverables = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10,
                             5.1, 5.2, 5.3, 5.4, 6.1, 6.2]

        self.deliv_tags = [11, 12, 13, 14, 21, 22, 23, 24, 41, 42, 43, 44, 45, 46, 47,  49, 410, 54, 61, 62]

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

        self.deliverable_title = {'11': '1.1: Agenda and minutes of the General Assembly / Kick-off meeting ',
                                  '12': '1.2: Data Management Plan ',
                                  '13': '1.3: 1st Agenda and minutes of yearly General Assembly ',
                                  '14': '1.4: 2nd Agenda and minutes of yearly General Assembly ',
                                  '21': '2.1: Risk assessment and mitigation plan ',
                                  '22': '2.2: Launch of IKC Best practice online platform  ',
                                  '23': '2.3: Deployment of Management Information System ',
                                  '24': '2.4: 1st Annual IKC Progress Assessment ',
                                  '41': '4.1: Integration plan for detector readout ',
                                  '410': '4.10: Test for technology demonstrator ',
                                  '42': '4.2: Counting rate capability ',
                                  '43': '4.3: Natural and enriched Gadolinium convertors design ',
                                  '44': '4.4: Report on the engineering design of BRR low dimensional moderator ',
                                  '45': '4.5: Simulation and Generic multi-grid design ',
                                  '46': '4.6: Detector characterisation ',
                                  '47': '4.7: Report on the conception design of the ESS and the BRR test beamline ',
                                  '49': '4.9: Detector electronics chain ',
                                  '51': '5.1: Design report data aggregator software ',
                                  '52': '5.2: Report processing choices for detector types ',
                                  '53': '5.3: Beta-version data aggregator software ',
                                  '54': '5.4: Report filed data acquisition ',
                                  '61': 'Deliverables ',
                                  '62': '6.2: Results of target group online survey '}

        self.deliverable_abstracts = {
            '11': 'The kick-off meeting held on September 25 2015 in Lund, Sweden successfully brought together representatives from all the 18 institutions that form the BrightnESS Consortium. It was an opportunity for all partners to align on the main objectives of the project, to present their prospective contribution to the project and get more information on the project management formalities. \n The aim of the meeting was to ensure that everyone has a common understanding of the project and their roles in it. All 18 research and academic institutions were represented at the meeting, which gathered a total of 68 participants. All guests were invited to an informal networking dinner on the evening of September 24. \n The schedule continued next day with the kick-off meeting during the first part of the day, and individual work package specific sessions in the afternoon. \n',
            '12': 'The purpose of this deliverable is to support the data management life cycle for all data that will be collected, processed or generated by the project. It provides a description of the data types the project will generate and how the data will be collected and stored and made available for validation, exploitation and re-\xaduse by others. The information in this Data Management Plan will be updated during the course of the project. \n',
            '13': 'The first BrightnESS General Assembly (GA) meeting was held on 7th October 2016 in Lund, Sweden. As the Assembly is responsible for monitoring the project implementation and determining the strategy anddirection of the project, the meeting represented an important opportunity for taking stock of the technical progress made during the first year of BrightnESS, discussing risks and problems encountered, checking progress versus cost expenditure and aligning on the activities for the next 12 months. \n In total, 16 partner institutes were represented at the meeting. The day before the official GA-meeting, the Representatives were invited to visit the ESS construction site visit outside Lund, followed by an informal networking dinner. At the GA meeting the participants were welcomed by Allen Weeks, the ESS Head of Communications, External Relations and IKC Management, who started the meeting with an overview of the ESS construction status. In the following session, Roy Pennings and Raquel Costa, the Project Coordinator and the Project Manager respectively, provided an overall update of the technical and financial project status of BrightnESS (WP1) as well as information on the upcoming reporting process to the European Commission. \n Presentations: \n Introduction to the GA \n Cost Monitoring \n Work Package 2 \n Work Package 3 \n Work Package 4 \n Work Package\xa0 5 \n Work Package 6 \n Work Package 6 (Task 6.4) \n',
            '14': 'The second BrightnESS General Assembly (GA) meeting was held at the ESS construction site outside Lund on the 5th September 2017. As the Assembly is responsible for monitoring the project implementation and determining the strategy and direction of the project, the meeting represented an important opportunity for taking stock of the technical progress made during the second year of BrightnESS, discussing risks and problems encountered, checking progress versus cost expenditure and aligning on the activities for the remaining 12 months. \n',
            '21': 'The construction of ESS is as unique as the ESS itself; this new next generation spallation source is being built on a greenfield site, physically located in Sweden and Denmark. For both countries, the experience of building research infrastructures of this scale is new. To build ESS, most of the necessary skills for its development need to be imported through In-kind Contributions (hereafter IKC) from participating institutes and companies in the member states. The IKC approach is intended to foster collaborations between national academia and industry, representing the entire supply chain. \n The mission for the ESS is the construction of the world’s leading neutron source for material research. In order to achieve this mission it is necessary to build an ESS Organisation with the necessary skills to oversee the project and support its Partners with the capability to manage and integrate IKC into a one highly integrated machine. This heavy reliance on IKC from many partners, poses significant challenges in terms of the management of the technologies, interoperability, integration, quality and timeliness of delivery/construction/operation for a complex and technologically advanced project like ESS. \n The ESS has fully recognised the risks associated with IKC and has taken necessary steps to handle and minimise them. To meet these needs, the ESS has developed a Risk Management Policy, which is based on three documents, including the ESS Risk Management Policy [1], the ESS Risk \nManagement Process [2] and the ESS Risk Management Plan [3] as well as the risk register for the entire facility, which are described in further detail below. \n The risks associated with IKC are analysed on different levels: High-level ESS risks associated with IKC for ESS Management, IK Risks to be held by the Individual Projects Accelerator, Target, NSS, as well as for the risks for IKC Partners across Europe and the successful implementation of IKCs. \n',
            '22': 'As part of Work Package 2 (WP2) “Strengthening the in-kind contribution coordination”, one of the main outcomes of the project is to maximize the common knowledge on how to best execute In-kind contribution (IKC) activities among all Partners in the European Spallation Source (ESS) Project. \n Task 2.3 concerns the setting-up and maintenance of an online IKC Best Practice Platform (hereafter: BPP) for the BrightnESS project which will allow partners and other stakeholders not only to find and exchange information, but also to benefit from sharing key documents that facilitate both the preparation and the implementation of an in-kind model in European Big Science Projects. \n The online Best Practices Platform will be accessible from March 9th via the website of the BrightnESS project. By integrating the BPP into the BrightnESS website, the BrightnESS network will leverage synergies in a more efficient manner in addition to generating further incremental user traffic. \n The BPP will evolve and further develop during the project’s lifecycle and extensions will be added based on user feedback. All content is available in English. \n',
            '23': 'This report concerns Deliverable D2.3 of the BrightnESS project and describes the "Deployment of an In-Kind Data Management Information System". The system consists of a centralised software platform called XRM+, that will provide support to the In-kind Management Coordination Office, ESS partners and management and for the governance of the ESS Project. The software code is strategically important for the management of In-Kind Contributions (IKCs) considering the total number of partners, the variety and complexity of the contributions, the number of partners per technical work-package and their interactions. \n',
            '24': 'This document is Deliverable 2.4. It is a comparative overview of the In Kind Contributions (IKC) being developed by (combinations of) institutes from the ESS Partner Countries1 between September 2015 (start of BrightnESS) and December 2016. Specifically, the deliverable highlights the important supporting role of the Work Package 2 ‘Field Coordinators’ from the BrightnESS IKC-Hubs in aligning activities across institutes and across borders and identifying potential technical risks that would prevent ESS from maintaining synchronicity between construction activities in Lund and the delivery schedule of the technical IKC Work Packages. \n',
            '41': 'Neutron detectors are the “eyes of ESS”, “seeing” the neutrons scattered within the instruments. As such, they act as cameras for neutrons converting neutrons into electronic signals for the Data Management and Scientific Computing Centre to process and analyse into scientific results. \n \nThe neutron detectors themselves are, at the core, electronic items. They are commonly categorized as consisting of a sensor, often termed just “the detector” and electronics performing digitization, triggering, identification, compression, collection, analysis tasks, termed the “readout electronics”. What is written in this report applies equally to the neutron detectors as parts of instruments and to the neutron beam monitors that monitor neutron flux and characteristics alone the neutron beamlines. \n At the European Spallation Source (ESS), due to the step change in the capability and complexity of the neutron instruments that will make up the facility, the electronics will be at least 1-2 orders of magnitude more complicated than for previous neutron facilities. This implies a subsequent step change in the approach to the integration of electronics. \n Deliverable 4.1 describes the integration plan for the detector readout and details of the breakdown and strategy for its implementation. A functional decomposition based approach has been adopted for the electronics integration. This treats the detector readout as a modular system. By clearly defining interfaces, and points of integration, it allows a generic readout to support the variety of detector designs that will be needed for the ESS instruments at minimum cost, whilst allowing for a long-term maintainable detector system, with minimal support levels. The implementation of the integration plan is now well underway both in terms of hardware candidates existing for all stages of this readout, as well as the software and firmware implementation. The interfaces to other groups within ESS have been identified and work on their definition is also progressing well. The most important interface is with BrightnESS WP5.1, where work is proceeding in close collaboration. \n',
            '410': 'The organization of BrightnESS Work Package 4 task 4.3 relies on the interaction between the European Spallation Source ERIC (ESS) and the Institut Lauve-Langevin (ILL) detector teams to make the best Multi-Grid technology [1-8] available for the ESS instruments at the first day of operation. Two approaches are considered in this task: on one side, ESS is focusing on the simulation, design, construction and characterization of a demonstrator detector containing detection elements, called grids, similar to the IN5 Grid developed previously in the CRISP project. This baseline, described in the BrightnESS D4.5 deliverable, ensures production feasibility and predictable operation of the detectors for the ESS instruments at Day-1. On the other side, the development carried out at ILL is mainly focused on the study of a new grid, called RAMSES Grid, with the aim of: \n1. reducing the dead zones of the detector, and \n2. improving the intrinsic detection efficiency. \nILL and ESS developed a 3 m long 8-columns prototype, called the IN5_Prototype, before the BrightnESS project. The walls used to reinforce the structure of the vessel limited its global efficiency. The weight of one module, 700 kg, a factor of around 2 higher than IN5, also represents a severe drawback for the integration into an instrument. Most of the Time-of-Flight (TOF) instruments of ESS are planned to operate in vacuum. The new approach studied in the BrightnESS project, is to reduce significantly the requirements on the mechanical strength on the detector vessel in order to reduce the need of reinforcement walls, by operating the detector at low gas pressure. \n',
            '42': 'This deliverable, “Counting rate capability”, is part of the task 4.2 “The Intensity Frontier”. It aims to report the rate capability of the technology used for the Multi-Blade detector. \n The Multi-Blade is a 10 B -based detector conceived to face the challenge of the counting rate capability arising from the neutron reflectometry at the European Spallation Source (ESS). The current detector technology, based on 3 He -based detector, is reaching fundamental limits in counting rate capability and position resolution. [Cam+11] The problem with count rates is a general one, and the ESS solution could potentially be applied to existing instruments at other neutron sources. [PHW14] \n The work on the Multi-Blade began in 2011 at the Institut Laue-Langevin (ILL) where two technology prototypes were built and tested showing promising results. [Pis14] The European Union is now sponsoring the Multi-Blade detector through the BrightnESS project [ESS] that aims to realise detectors optimised for these high rates. \n The Multi-Blade design has been improved since the beginning of BrightnESS as part of task 4.2. A new demonstrator has been built and tested within the collaboration of ESS, Lund University (LU) and the Wigner Research Centre for Physics, Hungary. It has been shown that aside from the improvement in counting rate capability, the Multi-Blade design also decreases the spatial resolution by about a factor three over state-of-the-art 3He-based reflectometer detectors. These and other results including the path ahead for this project will be presented. The Multi-Blade design is the one favoured as a development path to be pursued for reflectometry at ESS. \n At present, a data rate of 40 kHz/mm2 is achieved. This result is already very close to the desiderata target of 100 kHz/mm2 and it is a factor 100 above the state of art of the available technology (300Hz/mm2). Calculations indicates that this design is capable of reaching the given goal. \n',
            '43': 'This deliverable, D4.3: Natural and enriched Gadolinium converters design, is about determining a viable approved design for Gadolinium convertors for detectors. It establishes a design and engineering technique baseline for the detectors. There are three main aspects to this deliverable: \n 1. The requirements for the converters layers by understanding the desired properties. \n 2. Established a mechanical technique, by which relatively large areas (up to 60x60 cm2) of thin Gadolinium foils can be produced. \n 3. Present isoptope-enriched Gadolinium as a possible future upgrade for the detectors, by determining that there is a limited, but realistic strategic availability of the material. \n',
            '44': 'The construction of the European Spallation Source ERIC (ESS) is one of Europe’s largest recent research infrastructure investments and the most important advancement in the activity of the neutron scattering community. One of the crucial components and a most innovative development in enhancing the neutron source brightness is the compact cryogenic moderator. Its principle was recently invented by the ESS target team during the design phase of ESS. It has the potential to deliver a revolutionary difference versus an incremental difference in the performance of ESS. \n Before being able to be implemented, this very new idea and its technical solutions need complex simulation and experimental verification at various conditions. Without experimental verification at an appropriate existing neutron source, the compact cryogenic moderator represents a significant risk to the ESS project. Given the central nature of the moderator to the neutron source, it is difficult to find opportunities to experimentally verify novel designs. \n',
            '45': 'This deliverable, “Simulation and Generic multi-grid design”, is a part of the task 4.3 “Large Area Detectors”. Its aim is to report the generic design of the Multi-Grid detector via simulation, as well as design and construction of a demonstrator detector. Results from the testing of the demonstrator are also presented. \n The concept of the Multi-Grid detector addresses the requirements of direct geometry spectrometers, where up till now, 3He tubes have been used, providing an alternative to this rare gas [1, 2, 3] The Multi-Grid (MG) provides a much more affordable alternative to the traditional technology, as well as offering several technical advantages. These include the possibility to tailor the detector to the exact need of the instrument and a a higher rate capability. \n',
            '46': 'Within neutron scattering science the trend is toward increasing instrument power to expand neutron scattering techniques to faster kinetics as well as smaller and more complex structures. Neutron reflectometers are the most challenging instruments in terms of detector rate requirements. At current facilities, the time resolution for kinetic studies is limited by the available flux. Moreover, detector performance is already a challenge on reflectometers at existing sources. The peak brightness at the European Spallation Source (ESS) will be without precedent and the requirements for reflectometers at ESS go beyond present-day requirements and existing technologies. Current detectors for reflectometry are at their technical limit and already inhibit instrument performance to some extent. To ensure that the first reflectometry instrument at ESS can be considered as a ‘day-1 instrument’, a new performant and reliable detector system is needed by 2019. BrightnESS WP4 contributes toward meeting ESS requirements. Deliverable 4.6 concerns the completion of a detailed characterization of the Multi-Blade detector used in neutron reflectometry. The results confirm that the ambitious requirements expressed in the conceptual ESS instrument proposals can be met. In that sense, the achievement of Deliverable 4.6 significantly contributes to the reduction of the technical risk in building world-leading neutron reflectometers as part of the ESS instrument suite. Moreover, from the research carried out, the expectation is that the new technology will not only work for ESS, but can also be applied to existing instruments at other neutron sources. The technical details concerning the results of the Multi-Blade detector characterization are shown in the annexed publication which was recently published in JINST. The annex should therefore be considered an integral part of Deliverable 4.6. \n',
            '47': 'At the European Spallation Source (ESS), beams of neutrons will be generated by accelerating protons and directing them at a target made of tungsten. The high-energy neutrons resulting from the collisions are slowed down by the moderators, then extracted through the beam lines and guided to the instruments. One of the crucial components and a most innovative development in enhancing the neutron source brightness is the compact cryogenic moderator (CCM; also called: Low Dimension Moderator or LDM). Its principle was recently invented by the ESS target team during the design phase of ESS. This very new idea and its technical solutions need complex simulation and experimental verification at various conditions. The Wigner Research Centre, as a partner in BrightnESS Work Package 4, provides valuable contributions to task 4.5 through the experience gained in the construction and operation of a similarly innovative cold neutron source at the Budapest Neutron Centre (BNC). BNC operates a cold neutron research facility which includes a liquid hydrogen moderator inserted horizontally into the reactor core, a supermirror neutron guide system and a suit of 8 experimental stations placed in a neutron guide hall. \n',
            '49': 'This deliverable report D4.9 – Detector electronics chain describes the completion of a readout electronics chain for the NMX prototype detector, currently developed jointly by ESS and CERN within Work Package 4 Task 4.1. It contains information about the already available hardware used as a starting point for dedicated developments and the reasons why these components were selected. The components are in particular the VMM front-end ASIC developed within the ATLAS New Small Wheel upgrade project and the Scalable Readout System of the RD51 Collaboration1. \n The VMM ASIC features high readout rates, low electronic noise, excellent configuration possibilities and easy availability. The Scalable Readout System (SRS) is also freely available and allows for the implementation of new front-end ASICs within the timescale of this project. Moreover, as the name suggests, this readout system can be scaled from small detectors used during the development phase to the final prototype (to be delivered at the end of the project), or even several and larger detectors like foreseen at the NMX instrument. \n Several new hardware components and FPGA firmware have been developed in order to implement the VMM Application Specific Integrated Circuit (ASIC) into the Scalable Readout System. The system shows reliable operation in laboratory tests as well as in a first test beam at the R2D2 beamline at IFE, Norway. \nTowards the end of the BrightnESS project, improvements to the system will be implemented to increase the readout rate and provide a user-friendly system with online data monitoring. It should be noted that there is close collaborative work between BrightnESS WP4 and WP5 on this online data monitoring. \n',
            '51': 'The data aggregator software task in work package 5 is progressing as planned. We decided to use Apache Kafka as the underlying technology for aggregation and streaming, and Google FlatBuffers as the serialisation library. Development work is going on with an agile approach focussed on early software tests and delivery, addressing the requirements in iterations. Collaboration tools are being used to track the progress of the project, discuss issues and maintain documentation, with virtual meetings held every two weeks. \n Software modules to generate simulated data streams for integration and performance evaluations are ready to be put into our testing and deployment infrastructure. This infrastructure consists of a build server and with virtual machines for deploying and running integration tests as well as a physical lab space with three servers to be installed at the ESSIIP laboratory in Lund, where software from the Data Management group can be tested and integrated with real hardware and software from other ESS groups. \n In the coming development cycles we are going to validate the technology choices and system design and architecture in both settings, addressing problems that might be discovered in the tests. The use of Kafka in projects handling large volumes of data is an indication that it can satisfy our requirements. Results from the tests and future project steps will be documented in JIRA, Confluence and Bitbucket. \n \xa0 \n \xa0 \n DOI:\xa0 http://dx.doi.org/10.17199/BRIGHTNESS.D5.1 \xa0 \n',
            '52': 'Task 5.1 “Creating a standard neutron event data stream for different detector types” focuses on software event processing for the expected ESS detector suite. This will deliver generic neutron event information required for scientific experiments. Deliverable 5.2, which presents the results of our investigations in this task, shows that we are in a good position to cope with the processing needs of the different detector types once their configuration is final. For the future of the BrightnESS task, we see no unusual or high impact risks. \n For the majority of cases, specifications of upcoming detectors and their raw output format are not yet in a state that allows software prototyping. However, during the course of the project thus far, we have developed a good working relationship with the detector group and their partner institutes across Europe. That resulted in a good understanding of the domain and, not least, to two working prototypes of the event formation system for NMX and the Multi-Grid detector ahead of schedule. These two detector systems are a good template for future customized implementations. Most systems are quite similar to the Multi-Grid detector, and with NMX we are close to covering the most complex computational needs. To drive these working prototypes forward, we have put in place a common and modular framework. It hosts the detector-type specific processing algorithms whereby future tasks are divided into manageable modular chunks. \n With the tools developed, we are confident that we can adapt our processing algorithms and parameters in sync with any new hardware prototypes that become available, any updates to prototype detectors and production versions. We will be able to review quality indicators for individual events, statistics within and across datasets and interactively examine the effect of different filters or code changes. The software will also enable the specialist from ESS’ Data Management and Software Centre (DMSC) or the ESS detector group to fine-tune the event processing pipeline, change detector architecture and varying user needs, and will serve as commissioning and calibration tools. \n \xa0 \n DOI:\xa0 10.17199/BRIGHTNESS.D5.2 \n',
            '53': 'This document concerns BrightnESS Deliverable 5.3: “Beta-version data aggregator software”. It marks the delivery of a working software prototype of the main component of the data streaming infrastructure, that is needed to determine the roadmap to the full completion of the task (D5.5 due July 2018). The development of the data aggregation software system is progressing ahead of the WP schedule. With the choice of the open source third party project Apache Kafka as the central component for aggregation and streaming, the WP5 participants could focus on the domain specific software components to retrieve and aggregate the data, and to write them to file. This maximises the impact of work package 5 for ESS and other neutron facilities as it provides better functionality, flexibility and fault tolerance of the data acquisition chain. In current integration tests, neutron event data - together with simulated instrument metadata - automatically traverse the readout pipeline from event formation to file writing through Kafka. \n',
            '54': 'To enable cutting edge materials research at the European Spallation Source (ESS), information about the sample and its environment conditions, like temperature, strain, or electric and magnetic field are as important as the collection of neutron event data. This BrightnESS task 5.2 deals with the collection of sample environment information at a higher rate than is routinely done at existing neutron scattering facilities, in order to be prepared for the demands of the high flux source that ESS will provide. This first deliverable of the task lays out the work that has been done so far to gather requirements, identify potential hard- and software solutions, as well as prepare for integrating the sample environment data stream into the general data acquisition chain. It concludes with a roadmap to get to a working demonstrator system by the end of the project. The main challenges are the accurate absolute timestamping of the sampled data, which makes full use of the advanced ESS timing system, as well as the need to support continuous data sampling at high rates, which is a rare operations mode for fast ADCs. The work has been carried out in close collaboration with the other tasks in WP5, the ESS Detector Group (largely in WP4), and the ESS Integrated Control Systems division (ICS). \n',
            '61': ' ',
            '62': 'In its INFRADEV-3-2015 call, the European Commission recognised the challenges and difficulties faced by new pan-European infrastructures such as ESS in the process of becoming fully operational, when technologies, services and procedures need to be finalised and users’ trust and awareness must be built. As a response to the appeal of the European Commission on research infrastructures to give specific attention to interactions with end-users, one of the strategic goals of  BrightnESS  is to gain the trust of future users of ESS from science and industry, and to understand the role of key actors in the innovation ecosystem that ESS will foster. To this end, the  BrightnESS  team, within the framework of Work Package 6 entitled  Collaboration, Communication, and Dissemination,  and Work Package 3 entitled  Organisational Innovation  designed and carried out activities with the aim of acquiring a profound understanding of target groups relevant for ESS and its partners. In 2016,  BrightnESS  launched three parallel initiatives aiming at identifying the needs and expectations of: \n Scientific and academic users \n Industrial users \n Actors in innovation ecosystems \n The ultimate goal of the set of activities was not only to gain a deeper insight on each of the groups, but also to use the findings to develop tailored outreach and engagement strategies, and to shape ESS policies for access and innovation. Each group was assessed through a custom-made approach, which best conformed to the group specifics. \n'
        }

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
        doi = '10.17199/BRIGHTNESS.D' + tag2
        return doi


if __name__ == '__main__':

    print(sys.version)
    bright = Brightness()
    bright.get_password()
    bright.f()
    deliv = bright.deliv_tags

    for tag1 in deliv:
        tag = str(tag1)
        print(tag)
        doi = bright.make_doi(tag)
        title = bright.deliverable_title[tag]
        abstract = bright.deliverable_abstracts[tag]
        url = "https://brightness.esss.se/about/deliverables/" + tag + "-" + bright.deliverable_dict[tag]
        print(doi, title, abstract, url)
        bright.request_post(doi, title, abstract, url)
