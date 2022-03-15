import json
from datetime import datetime
from html.parser import HTMLParser
from io import StringIO

import requests


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def get_hvc_data(postalcode, streetnumber):
    baseUrl = 'https://inzamelkalender.hvcgroep.nl'

    bagidPage = \
        requests.get(baseUrl + '/adressen/' + postalcode + ':' + streetnumber)
    bagidJson = json.loads(bagidPage.text)
    bagid = bagidJson[0]['bagid']

    afvalstromenPage = \
        requests.get(baseUrl + '/rest/adressen/' + bagid + '/afvalstromen')
    afvalstromenJson = json.loads(afvalstromenPage.text)

    ophaaldataPage = \
        requests.get(baseUrl + '/rest/adressen/' + bagid + '/ophaaldata')
    ophaaldataJson = json.loads(ophaaldataPage.text)

    ophaaldata = []
    for entry in ophaaldataJson:
        afvalstroom = entry['afvalstroom_id']
        afvalstroomLink = \
            'https://www.hvcgroep.nl/afvalstroom/' + str(afvalstroom)
        ophaaldatumStr = entry['ophaaldatum']
        ophaaldatum = datetime.strptime(ophaaldatumStr, "%Y-%m-%d")
        for stroom in afvalstromenJson:
            if stroom['id'] == afvalstroom:
                title = stroom['title']
                content = strip_tags(stroom['content'])
        ophaaldata.append({
            'ophaaldatum': ophaaldatum,
            'title': title,
            'content': content,
            'link': afvalstroomLink
            })
    return(ophaaldata)
