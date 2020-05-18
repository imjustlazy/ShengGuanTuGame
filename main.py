# coding: utf-8

import pdb

from game_map import GameMap
from dice import Dices
from player import BaoYu, BaoChai, DaiYu, FengJie, MiaoYu, XiangLing

# TODO: put gamemap, 6 players all in this class, and game status
# class GameStatus(object):
#     is_end = False

#     def __init__(self):
#         # 

def is_game_end(*players):
    locations = [player.location for player in players]
    return any([location == '红楼梦太虚幻境图' for location in locations])

def main():
    dices = Dices()
    game_map = GameMap()
    baoyu, baochai, daiyu = BaoYu(), BaoChai(), DaiYu()
    fengjie, miaoyu, xiangling = FengJie(), MiaoYu(), XiangLing()
    
    baoyu = BaoYu()
    baochai = BaoChai()
    daiyu = DaiYu()
    fengjie = FengJie()
    miaoyu = MiaoYu()
    xiangling = XiangLing()

    huihe = 0
    while True:
        huihe += 1
        print('开始第', huihe, '回合\n')
        baoyu.go(dices, game_map)
        if is_game_end(baoyu, baochai, fengjie):
            print('游戏结束，赢家是', '宝玉')
            break
        baochai.go(dices, game_map)
        if is_game_end(baoyu, baochai, fengjie):
            print('游戏结束，赢家是', '宝钗')
            break
        fengjie.go(dices, game_map)
        if is_game_end(baoyu, baochai, fengjie):
            print('游戏结束，赢家是', '凤姐')
            break
        print('第', huihe, '回合结束\n')
    baoyu.show_status()
    baochai.show_status()
    fengjie.show_status()
    pdb.set_trace()

if __name__ == '__main__':
    main()
