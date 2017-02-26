from __future__ import absolute_import, division, print_function

from lxml import etree
from lxml import objectify
import json


class BaseCluster():

    def __init__(self, isJson, data, block_string):
        self.json = isJson
        self.block_string = block_string
        self.data = block_string
        if isJson:
            self.json_init(data)
            self.raw_obj = data[list(data.keys())[0]]
        else:
            self.xml_init(data)
            self.raw_obj = data

    def json_init(self, json_obj):
        for rootkey in json_obj:
            for key in json_obj[rootkey]:
                setattr(self, key, json_obj[rootkey][key])

    def xml_init(self, xml):
        for element in xml.iterchildren():
            setattr(self, element.tag, element.text)

    def __repr__(self):
        return self.data
