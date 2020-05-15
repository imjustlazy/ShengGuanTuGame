# coding: utf-8

class Place(object):
    name = ''
    description = ''
    pre = ''
    sub = ''

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def add_effect(self):
        pass
