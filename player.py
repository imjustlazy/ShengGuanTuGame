# coding: utf-8

import random
from dice import Dices
import place_common_effect

legal_names = ['宝玉', '宝钗', '黛玉', '凤姐', '妙玉', '香菱']

class Player(object):
    name = ''
    qingan_count = 0
    wenhao_count = 0
    shouhe_count = 0
    juhe_count = 0
    fa_count = 0
    nianxiang_count = 0
    losemoney_count = 0
    is_stop = False
    location = ''
    location_last = ''
    dice_kind = None
    dices = (0, 0, 0)

    stop_places = list()
    goback_places = list()
    qingan_places = list()
    wenhao_places = list()
    shouhe_places = list()
    juhe_places = list()
    fa_places = list()
    nianxiang_places = list()
    losemoney_places = list()
    calldice_places = list()

    def __init__(self, name):
        self.name = name
        self.location = '荣国府'
        self.location_last = '荣国府'
        self.stop_places = place_common_effect.stop_places
        self.goback_places = place_common_effect.goback_places
        self.qingan_places = place_common_effect.qingan_places
        self.wenhao_places = place_common_effect.wenhao_places
        self.shouhe_places = list()
        self.juhe_places   = place_common_effect.juhe_places
        self.fa_places     = list()
        self.nianxiang_places = place_common_effect.nianxiang_places
        self.losemoney_places = place_common_effect.losemoney_places
        self.calldice_places  = place_common_effect.calldice_places

    def go(self, dices: Dices):
        '''一轮行动'''
        if self.is_stop:
            self.is_stop = False
            return
        self.get_dices(dices)
        # TODO: add the process of go forward
        self.place_interact()

    def go_back(self):
        '''罚回本位'''
        self.location_last, self.location = self.location, self.location_last

    def go_forward(self, new_place: str):
        self.location_last = self.location
        self.location = new_place

    def stop(self):
        '''停一轮'''
        self.is_stop = True
    
    def get_dices(self, dices: Dices):
        self.dice_kind, self.dices = dices.get()

    def call_dices(self, dices: Dices):
        '''随意呼点应者方行不应者罚'''
        call_num = random.randint(1, 6)
        print(self.name, 'call', call_num)
        self.get_dices(dices)
        self.judge_dices(call_num)

    def judge_dices(self, num_target):
        '''遇某方行不遇者罚'''
        if num_target in self.dices:
            # TODO: 遇某方行
            pass
        else:
            self.fa()

    def qingan(self):
        self.qingan_count += 1

    def wenhao(self):
        self.wenhao_count += 1

    def shouhe(self):
        self.shouhe_count += 1

    def juhe(self):
        self.juhe_count += 1

    def fa(self, bei: int = 1):
        self.fa_count += bei
    
    def nianxiang(self):
        self.nianxiang_count += 1

    def losemoney(self):
        self.losemoney_count += 1

    def place_interact(self):
        '''
        六人相同的处置
        '''
        print(self.name, '正走到', self.location)
        # location = self.location


class BaoYu(Player):
    yeshi_count = 0
    yeshi_places = ['贾氏家塾', '茫茫大士', '渺渺真人']
    _stop_places = ['薛姨妈', '袭人', '晴雯']
    _goback_places = ['玉钏', '鸳鸯']
    _not_goback_places = ['贾氏家塾', '松鹤童子', '冯渊']
    _not_wenhao_places = ['贾环']
    _shouhe_places = ['女仙', '怡红院']
    _fa_places = [('金钏', 3), ('赵姨娘', 3), '贾环', '彩云', ('秦可卿', 2)]
    _calldice_places = [('怡红院', 1)]

    # stop_places: list
    # goback_places: list
    # qingan_places: list
    # wenhao_places: list
    # shouhe_places: list
    # juhe_places: list
    # fa_places: list
    # nianxiang_places: list
    # losemoney_places: list
    # calldice_places: list

    def __init__(self, name = '宝玉'):
        super().__init__(name)
        assert self.name == '宝玉'
        self.stop_places += self._stop_places
        self.goback_places = [p for p in self.goback_places + self._goback_places
                                if p not in self._not_goback_places]
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places += self._fa_places
        self.calldice_places += self._calldice_places

    def place_interact(self):
        super().place_interact()
        # location = super().location


class BaoChai(Player):
    _not_wenhao_places = ['莺儿']
    _shouhe_places = ['蘅芜苑']
    _fa_places = ['茫茫大士', '渺渺真人']
    _calldice_places = [('薛姨妈', 2), ('蘅芜苑', 2)]
    
    def __init__(self, name = '宝钗'):
        super().__init__(name)
        assert self.name == '宝钗'
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places += self._fa_places
        self.calldice_places += self._calldice_places
    
    def place_interact(self):
        super().place_interact()


class DaiYu(Player):
    _stop_places = ['贾夫人']
    _not_wenhao_places = ['宝蟾', '紫鹃', '雪雁']
    _shouhe_places = ['林如海', '潇湘馆']
    _calldice_places = ['林如海', ('潇湘馆', 3)]
    
    def __init__(self, name = '黛玉'):
        super().__init__(name)
        assert self.name == '黛玉'
        self.stop_places += self._stop_places
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places += self._fa_places
        self.calldice_places += self._calldice_places
    
    def place_interact(self):
        super().place_interact()


class FengJie(Player):
    _stop_places = ['鸳鸯', '巧姐', '秦可卿']
    _wenhao_places = ['內监']
    _not_wenhao_places = ['贾环', '鸳鸯', '平姑娘', '尤二姐', '巧姐', '小红']
    _shouhe_places = ['巧姐', '']
    _fa_places = [('赵姨娘', 3), '贾环', '贾琏', ('秦可卿', 2), ('鲍二家', 2), ('醋缸', 2)]
    _calldice_places = [('怡红院', 1), ('贾琏', 4), ('尤二姐', 3), '醋缸']

    def __init__(self, name = '凤姐'):
        super().__init__(name)
        assert self.name == '凤姐'
        self.stop_places += self._stop_places
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places += self._fa_places
        self.calldice_places += self._calldice_places

    def place_interact(self):
        super().place_interact()


class MiaoYu(Player):
    _stop_places = ['女仙', '惜春']
    _not_stop_places = ['贾赦']
    _not_qingan_places = ['贾珠']
    _not_wenhao_places = ['薛蟠', '宝蟾', '薛蝌']
    _shouhe_places = ['栊翠庵']
    _fa_places = ['刘姥姥']
    _not_losemoney_places = ['女尼']
    _calldice_places = [('栊翠庵', 5)]
    
    def __init__(self, name = '妙玉'):
        super().__init__(name)
        assert self.name == '妙玉'
        self.stop_places = [p for p in self.stop_places + self._stop_places
                            if p not in self._not_stop_places]
        self.qingan_places = [p for p in self.qingan_places if p not in self._not_qingan_places]
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places += self._fa_places
        self.calldice_places += self._calldice_places
    
    def place_interact(self):
        super().place_interact()


class XiangLing(Player):
    _stop_places = ['薛姨妈']
    _not_stop_places = ['贾赦']
    _not_goback_places = ['冯渊']
    _qingan_places = ['夏金桂', '甄士隐']
    _not_qingan_places = ['贾珠']
    _shouhe_places = ['薛蟠']
    _fa_places = [('宝蟾', 3), ('冯渊', 2)]
    _calldice_places = [('薛蟠', 6), '夏金桂', '甄士隐']
    
    def __init__(self, name = '香菱'):
        super().__init__(name)
        assert self.name == '香菱'
        self.stop_places = [p for p in self.stop_places + self._stop_places
                            if p not in self._not_stop_places]
        self.goback_places = [p for p in self.goback_places if p not in self._not_goback_places]
        self.qingan_places = [p for p in self.qingan_places + self._qingan_places
                            if p not in self._not_qingan_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places += self._fa_places
        self.calldice_places += self._calldice_places
    
    def place_interact(self):
        super().place_interact()