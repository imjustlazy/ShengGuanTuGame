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

def who_winner(*players):
    locations = {player.name: player.location for player in players}
    winner = [name for name, location in locations.items() 
            if location == '红楼梦太虚幻境图']
    return winner[0]

def exist_winner(*players):
    winner = [p.name for p in players if p.location == '红楼梦太虚幻境图']
    assert len(winner) <= 1
    if len(winner) == 0:
        return None
    else:
        return winner[0]

def main():
    dices = Dices()
    game_map = GameMap()
    # NO! 同时赋值会触发 类的继承 中的隐藏bug! 应该分别赋值
    # baoyu, baochai, daiyu = BaoYu(), BaoChai(), DaiYu()
    # fengjie, miaoyu, xiangling = FengJie(), MiaoYu(), XiangLing()
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
        if is_game_end(baoyu, baochai, daiyu, fengjie, miaoyu, xiangling):
            break
        baochai.go(dices, game_map)
        if is_game_end(baoyu, baochai, daiyu, fengjie, miaoyu, xiangling):
            break
        daiyu.go(dices, game_map)
        if is_game_end(baoyu, baochai, daiyu, fengjie, miaoyu, xiangling):
            break
        fengjie.go(dices, game_map)
        if is_game_end(baoyu, baochai, daiyu, fengjie, miaoyu, xiangling):
            break
        miaoyu.go(dices, game_map)
        if is_game_end(baoyu, baochai, daiyu, fengjie, miaoyu, xiangling):
            break
        xiangling.go(dices, game_map)
        if is_game_end(baoyu, baochai, daiyu, fengjie, miaoyu, xiangling):
            break
        print('第', huihe, '回合结束\n')
    print('游戏结束，赢家是', 
        who_winner(baoyu, baochai, daiyu, fengjie, miaoyu, xiangling), '\n')

    baoyu.show_status()
    baochai.show_status()
    daiyu.show_status()
    fengjie.show_status()
    miaoyu.show_status()
    xiangling.show_status()

    pdb.set_trace()

if __name__ == '__main__':
    main()
