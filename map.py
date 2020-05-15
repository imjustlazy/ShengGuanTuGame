# coding: utf-8

from place import Place

# class Place(object):
#     name = ''
#     description = ''

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

class Map(object):
    places = dict()

    def __init__(self):
        self.load_map_description()

    def load_map_description(self):
        f = open('./map_description.txt', 'r', encoding='utf-8')
        descriptions = [line.rstrip('\n').split(', ') for line in f.readlines()]
        f.close()
        assert all([len(item) == 2 for item in descriptions])
        
        count_guizu = 0
        for name, des in descriptions:
            if name == '鬼卒':
                count_guizu += 1
                name += str(count_guizu)
            places[name] = Place(name, des)