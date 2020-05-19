# coding: utf-8

import random

from dice import Dices
from game_map import GameMap
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

    # stop_places: list
    # goback_places: list
    # qingan_places: list
    # wenhao_places: list
    # shouhe_places: list
    # juhe_places: list
    # fa_places: dict
    # nianxiang_places: list
    # losemoney_places: list
    # calldice_places: dict

    def __init__(self, name):
        self.name = name
        self.location = '荣国府'
        self.stop_places = place_common_effect.stop_places.copy()
        self.goback_places = place_common_effect.goback_places.copy()
        self.qingan_places = place_common_effect.qingan_places.copy()
        self.wenhao_places = place_common_effect.wenhao_places.copy()
        self.shouhe_places = list()
        self.juhe_places   = place_common_effect.juhe_places.copy()
        self.fa_places     = dict()
        self.nianxiang_places = place_common_effect.nianxiang_places.copy()
        self.losemoney_places = place_common_effect.losemoney_places.copy()
        self.calldice_places  = place_common_effect.calldice_places.copy()

    def show_status(self):
        summary = self.name + ' 的状态:\n'
        summary += self.name + '正在 ' + self.location + '\n'
        if self.is_stop:
            summary += '即将停一轮\n'
        summary += '请安了 ' + str(self.qingan_count) + ' 次\n'
        summary += '问好了 ' + str(self.wenhao_count) + ' 次\n'
        summary += '受贺了 ' + str(self.shouhe_count) + ' 次\n'
        summary += '举贺了 ' + str(self.juhe_count) + ' 次\n'
        summary += '被罚了 ' + str(self.fa_count) + ' 次\n'
        summary += '拈香了 ' + str(self.nianxiang_count) + ' 次\n'
        summary += '捐资了 ' + str(self.losemoney_count) + ' 次\n'
        print(summary)

    def show_features(self):
        summary = self.name + ' 的特点:\n'
        summary += self.name + '停一轮 的地点有 ' + ', '.join(self.stop_places) + '\n'
        summary += self.name + '回本位 的地点有 ' + ', '.join(self.goback_places) + '\n'
        summary += self.name + '请安 的地点有 ' + ', '.join(self.qingan_places) + '\n'
        summary += self.name + '问好 的地点有 ' + ', '.join(self.wenhao_places) + '\n'
        summary += self.name + '受贺 的地点有 ' + ', '.join(self.shouhe_places) + '\n'
        summary += self.name + '举贺 的地点有 ' + ', '.join(self.juhe_places) + '\n'
        summary += self.name + '受罚 的地点有 ' + ', '.join(self.fa_places) + '\n'
        summary += self.name + '拈香 的地点有 ' + ', '.join(self.nianxiang_places) + '\n'
        summary += self.name + '捐资 的地点有 ' + ', '.join(self.losemoney_places) + '\n'
        summary += self.name + '掷骰 的地点有 ' + ', '.join(self.calldice_places) + '\n'
        print(summary)

    def go(self, dices: Dices, game_map: GameMap):
        '''一轮行动'''
        print(self.name, '正在', self.location, '开始一轮行动')
        if self.is_stop:
            print(self.name, '这一轮 停')
            self.is_stop = False
            return
        self.get_dices(dices)
        print(self.name, '掷骰子。结果是', self.dices)
        self.go_forward(game_map)
        self.place_interact()

    def get_dices(self, dices: Dices):
        self.dice_kind, self.dices = dices.get()

    def go_forward(self, game_map: GameMap):
        step = sum(self.dices)
        new_place = game_map.go_forward(self.location, step)
        self.location_last = self.location
        self.location = new_place
        print(self.name, '往前走', step, '步，到达', new_place)

    def place_interact(self):
        '''
        人物与地点的交互
        '''
        if self.location in self.stop_places:
            self.stop()
        if self.location in self.goback_places:
            self.goback()
        if self.location in self.qingan_places:
            self.qingan()
        if self.location in self.wenhao_places:
            self.wenhao()
        if self.location in self.shouhe_places:
            self.shouhe()
        if self.location in self.juhe_places:
            self.juhe()
        if self.location in self.fa_places:
            self.fa()
        if self.location in self.nianxiang_places:
            self.losemoney()
        if self.location in self.calldice_places:
            # self.call_dices()
            pass
        print(self.name, '走到了', self.location, '\n')


    def stop(self):
        '''停一轮'''
        print(self.name, '将要停一轮')
        self.is_stop = True

    def goback(self):
        '''罚回本位'''
        print(self.name, '被罚回本位')
        self.location_last, self.location = self.location, self.location_last
        print(self.name, '从', self.location_last, '回到了', self.location)

    def qingan(self):
        '''请安'''
        print(self.name, '向', self.location, '请安')
        self.qingan_count += 1

    def wenhao(self):
        '''问好'''
        print(self.name, '向', self.location, '问好')
        self.wenhao_count += 1

    def shouhe(self):
        '''受贺'''
        print(self.name, '因', self.location, '受贺')
        self.shouhe_count += 1

    def juhe(self):
        '''举贺'''
        print(self.name, '在', self.location, '举贺')
        self.juhe_count += 1

    def fa(self):
        '''受罚'''
        bei = self.fa_places[self.location]
        if bei == 1:
            fa_str = '受罚'
        elif bei == 2:
            fa_str = '加倍受罚'
        elif bei == 3:
            fa_str = '三倍受罚'
        print(self.name, '因', self.location, fa_str)
        self.fa_count += bei
    
    def nianxiang(self):
        '''拈香'''
        print(self.name, '在', self.location, '拈香')
        self.nianxiang_count += 1

    def losemoney(self):
        '''糖钱 赏赐 捐资 布施'''
        print(self.name, '给', self.location, '捐资')
        self.losemoney_count += 1

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


class BaoYu(Player):
    yeshi_count = 0
    yeshi_places = ['贾氏家塾', '茫茫大士', '渺渺真人']
    _stop_places = ['薛姨妈', '袭人', '晴雯']
    _goback_places = ['玉钏', '鸳鸯']
    _not_goback_places = ['贾氏家塾', '松鹤童子', '冯渊']
    _not_wenhao_places = ['贾环']
    _shouhe_places = ['女仙', '怡红院']
    _fa_places = {'金钏': 3, '赵姨娘': 3, '贾环': 1, '彩云': 1, '秦可卿': 2}
    _calldice_places = {'怡红院': 1}

    def __init__(self):
        super().__init__('宝玉')
        # print('after super().__init__()')
        # self.show_features()
        self.stop_places += self._stop_places
        self.goback_places = [p for p in self.goback_places + self._goback_places
                                if p not in self._not_goback_places]
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places.update(self._fa_places)
        self.calldice_places.update(self._calldice_places)
        # print('after changes')
        # self.show_features()

    def place_interact(self):
        super().place_interact()


class BaoChai(Player):
    _not_wenhao_places = ['莺儿']
    _shouhe_places = ['蘅芜苑']
    _fa_places = {'茫茫大士': 1, '渺渺真人': 1}
    _calldice_places = {'薛姨妈': 2, '蘅芜苑': 2}
    
    def __init__(self):
        super().__init__('宝钗')
        # print('after super().__init__()')
        # self.show_features()
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places.update(self._fa_places)
        self.calldice_places.update(self._calldice_places)
        # print('after changes')
        # self.show_features()
    
    def place_interact(self):
        super().place_interact()


class DaiYu(Player):
    _stop_places = ['贾夫人']
    _not_wenhao_places = ['宝蟾', '紫鹃', '雪雁']
    _shouhe_places = ['林如海', '潇湘馆']
    _calldice_places = {'林如海': None, '潇湘馆': 3}
    
    def __init__(self):
        super().__init__('黛玉')
        # print('after super().__init__()')
        # self.show_features()
        self.stop_places += self._stop_places
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.calldice_places.update(self._calldice_places)
        # print('after changes')
        # self.show_features()
    
    def place_interact(self):
        super().place_interact()


class FengJie(Player):
    _stop_places = ['鸳鸯', '巧姐', '秦可卿']
    _wenhao_places = ['內监']
    _not_wenhao_places = ['贾环', '鸳鸯', '平姑娘', '尤二姐', '巧姐', '小红']
    _shouhe_places = ['巧姐', '']
    _fa_places = {'赵姨娘': 3, '贾环': 1, '贾琏': 1, '尤二姐': 3, '鲍二家': 2, '醋缸': 2}
    _calldice_places = {'贾琏': 4, '醋缸': None}

    def __init__(self):
        super().__init__('凤姐')
        # print('after super().__init__()')
        # self.show_features()
        self.stop_places += self._stop_places
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places.update(self._fa_places)
        self.calldice_places.update(self._calldice_places)
        # print('after changes')
        # self.show_features()

    def place_interact(self):
        super().place_interact()


class MiaoYu(Player):
    _stop_places = ['女仙', '惜春']
    _not_stop_places = ['贾赦']
    _not_qingan_places = ['贾珠']
    _not_wenhao_places = ['薛蟠', '宝蟾', '薛蝌']
    _shouhe_places = ['栊翠庵']
    _fa_places = {'刘姥姥': 1}
    _not_losemoney_places = ['女尼']
    _calldice_places = {'栊翠庵': 5}
    
    def __init__(self):
        super().__init__('妙玉')
        # print('after super().__init__()')
        # self.show_features()
        self.stop_places = [p for p in self.stop_places + self._stop_places
                            if p not in self._not_stop_places]
        self.qingan_places = [p for p in self.qingan_places if p not in self._not_qingan_places]
        self.wenhao_places = [p for p in self.wenhao_places if p not in self._not_wenhao_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places.update(self._fa_places)
        self.losemoney_places = [p for p in self.losemoney_places if p not in self._not_losemoney_places]
        self.calldice_places.update(self._calldice_places)
        # print('after changes')
        # self.show_features()
    
    def place_interact(self):
        super().place_interact()


class XiangLing(Player):
    _stop_places = ['薛姨妈']
    _not_stop_places = ['贾赦']
    _not_goback_places = ['冯渊']
    _qingan_places = ['夏金桂', '甄士隐']
    _not_qingan_places = ['贾珠']
    _shouhe_places = ['薛蟠']
    _fa_places = {'宝蟾': 3, '冯渊': 2}
    _calldice_places = {'薛蟠': 6, '夏金桂': None, '甄士隐': None}
    
    def __init__(self):
        super().__init__('香菱')
        # print('after super().__init__()')
        # self.show_features()
        self.stop_places = [p for p in self.stop_places + self._stop_places
                            if p not in self._not_stop_places]
        self.goback_places = [p for p in self.goback_places if p not in self._not_goback_places]
        self.qingan_places = [p for p in self.qingan_places + self._qingan_places
                            if p not in self._not_qingan_places]
        self.shouhe_places += self._shouhe_places
        self.fa_places.update(self._fa_places)
        self.calldice_places.update(self._calldice_places)
        # print('after changes')
        # self.show_features()
    
    def place_interact(self):
        super().place_interact()
