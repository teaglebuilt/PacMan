import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests import Session
from zeep import Client
from zeep.transports import Transport
import operator
import requests
import json
from itertools import chain
from pprint import pprint


class WebService:

    def __init__(self):
        session = Session()
        session.verify = False
        self.transport = Transport(session=session)
        self.service = dict()
        self.endpoints = list()
        self.methods = list()

    def parseElements(self, elements):
        all_elements = {}
        for name, element in elements:
            all_elements[name] = {}
            all_elements[name]['optional'] = element.is_optional
            if hasattr(element.type, 'elements'):
                all_elements[name]['type'] = self.parseElements(
                    element.type.elements)
            else:
                all_elements[name]['type'] = str(element.type)
        return all_elements

    def soap_methods(self, uri):
        interface = {}
        self.client = Client(wsdl=uri, transport=self.transport)
        for service in self.client.wsdl.services.values():
            interface[service.name] = {}
            for port in service.ports.values():
                interface[service.name][port.name] = {}
                operations = {}
                for operation in port.binding._operations.values():
                    operations[operation.name] = {}
                    operations[operation.name]['input'] = {}
                    elements = operation.input.body.type.elements
                    operations[operation.name]['input'] = self.parseElements(elements)
                interface[service.name][port.name]['operations'] = operations
        return interface

    def rest_methods(self, uri):
        data = requests.get(uri).json()
        print(data)
        return data["paths"]

    def __call__(self, uri):
        print(uri)
        if uri.endswith("wsdl"):
            return self.soap_methods(uri)
        elif uri.endswith("swagger.json"):
            return self.rest_methods(uri)