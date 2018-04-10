# -*- coding: utf-8 -*-
from random import choice

'''
def card_build():
    huase = ['梅花','红桃','方块','黑桃']
    shuzi = range(2,11) + ['J','Q','K','A']
    num = 0

    print '[',
    for i in huase:
        for j in shuzi:
            print "'" + str(i) + str(j) + "',",
            num = num + 1
    print ']'

    print 'num = ',num

def card_build2():
    #无：梅花2 红桃2 方块2 黑桃A
    cards = [ '梅花3', '梅花4', '梅花5', '梅花6', '梅花7', '梅花8', '梅花9', '梅花10', '梅花J', '梅花Q', '梅花K', '梅花A',
              '红桃3', '红桃4', '红桃5', '红桃6', '红桃7', '红桃8', '红桃9', '红桃10', '红桃J', '红桃Q', '红桃K', '红桃A',
              '方块3', '方块4', '方块5', '方块6', '方块7', '方块8', '方块9', '方块10', '方块J', '方块Q', '方块K', '方块A',
              '黑桃2', '黑桃3', '黑桃4', '黑桃5', '黑桃6', '黑桃7', '黑桃8', '黑桃9', '黑桃10', '黑桃J', '黑桃Q', '黑桃K' ]

    for one in cards:
        print one
'''

def display_card(i):
    huase = ('♣','♥','♦','♠')#('♣梅花','♥红桃','♦方块','♠黑桃')
    shuzi = ('3','4','5','6','7','8','9','10','J','Q','K','A','2')   # 0..11(A),12(2)
    tmp = shuzi[i % 12]
    if i == 47:
        tmp = shuzi[12]
    s_tmp = huase[i/12] + tmp
    return s_tmp.decode('utf8')

    
def distribute_cards(tmp_cards,tmp_orders):
    i = 0
    tmp_players = [[],[],[]]
    while(len(tmp_cards) > 0):
        index = tmp_orders[i]
        i = (i + 1)%3
        x = choice(tmp_cards)
        tmp_cards.remove(x)
        tmp_players[index].append(x)
    return tmp_players

def sort_card(tmp_cards):
    tmp_len = len(tmp_cards)
    for i in range(0,tmp_len-1):
        for j in range(i+1,tmp_len):
            if (tmp_cards[i]%12 > tmp_cards[j]%12) or (tmp_cards[i] == 47):
                tmp = tmp_cards[i]
                tmp_cards[i] = tmp_cards[j]
                tmp_cards[j] = tmp
    return tmp_cards
    
cards = range(0,48)
for i in cards:
    pass
    #print display_card(i),
    #print i,i%12   # card_bigs


orders = [0,1,2]  #上中下游
    
players = distribute_cards(cards,orders)

for i in orders:
    print 'Player',i,'= ',
    players[i] = sort_card(players[i])
    for j in players[i]:
        print display_card(j),
    print '\n'
