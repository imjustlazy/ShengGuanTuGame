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

    def get_place_from_name(self, place_name: str):
        return self.places[place_name]

    def load_map_description(self):
        f = open('./place_description.txt', 'r', encoding='utf-8')
        descriptions = [line.rstrip('\n').split(', ') for line in f.readlines()]
        f.close()
        assert all([len(item) == 2 for item in descriptions])
        
        count_guizu = 0
        for name, des in descriptions:
            if name == '鬼卒':
                count_guizu += 1
                name += str(count_guizu)
            self.places[name] = Place(name, des)
        
        f = open('./structure_description.txt', 'r', encoding='utf-8')
        descriptions = f.readlines()
        f.close()
        assert descriptions.count('\n') == 2
        cut_a = descriptions.index('\n')
        description_a, descriptions = descriptions[:cut_a], descriptions[cut_a+1:]
        cut_b = descriptions.index('\n')
        description_b, description_c= descriptions[:cut_b], descriptions[cut_b+1:]
        assert len(description_a) == 127 and len(description_b) == 14 and len(description_c) == 17

        def build_structure_from_place_list(place_names: list):
            connections = [(place_names[i], place_names[i+1]) for i in range(len(place_names)-1)]
            for pre_name, sub_name in connections:
                # pre = self.get_place_from_name(pre_name)
                pre = self.places[pre_name]
                sub = self.places[sub_name]
                # 
                pre.sub = sub_name
                sub.pre = pre_name
