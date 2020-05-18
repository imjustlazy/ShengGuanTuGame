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

    def __repr__(self):
        return self.name + '\t前一位置: ' + self.pre + '\t后一位置: ' + self.sub
    
    def __str__(self):
        return self.name + '\t前一位置: ' + self.pre + '\t后一位置: ' + self.sub
