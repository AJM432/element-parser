import json


with open('data.json', 'r') as f:
    data = json.load(f)


class Element:

    def __init__(self, name, key):
        self.name = name
        self.key = key
        
        self.symbol = self.get_item('symbol')
        self.full_name = self.get_item('name')
        self.valenceE = self.get_item('shells')[-1]  # valence electron

    def get_item(self, required):  # input attribute of element, outputs value
        for element in data:
            if self.key in element:
                if element[self.key] == self.name:
                    return element[required]


class Metal(Element):
    def __init__(self, name, key):
        super().__init__(name, key)  # refrences super class
        self.charge = self.valenceE


class Nonmetal(Element):

    def __init__(self, name, key):
        
        super().__init__(name, key)  # refrences super class
        self.compound = self.get_item('suffix')
        self.charge = self.valenceE - 8
        




