# -*- coding: utf-8 -*-
'''
P 31 Coin sums
    In England the currency is made up of pound, £, and pence, p, and there are 
    eight coins in general circulation:
        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:
        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
'''
def answer():
    '''
    Start with the largest coin. Add as many of that as you can to the total. If the
    total shoots above 2, subtract the last term and move to the next smaller coin 
    and repeat. Once the total becomes equal to 2, stop and add one to num_ways.
    The begin again with the next biggest coin after the smallest coin in the previous
    permutation. 
    '''
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    #coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
    starting_coin = coins[0]
    list = []
    num_ways = 0
    while True:
        num_ways = 0
        total = starting_coin
        print "starting coin: ", starting_coin
        list.append(starting_coin)
        print "list: ", list
        for coin in coins:
            while total + coin <= 2:
                print "adding coin", coin
                total += coin
                list.append(coin)
            if total == 2:
                print "found way: ", list
                num_ways += 1
                try:
                    starting_coin = coins[coins.index(coin) + 1]
                    total -= coin
                    list.pop()
                except IndexError:
                    print "next starting coin"
                    starting_coin = coins[coins.index(starting_coin) + 1]
                    total = 0
                    list = []
                    break
                #break
    return num_ways

def answerr():
    coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    #coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
    starting_coin = coins[0]
    list = []
    num_ways = 0
    while True:
        combo = {2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
        total = 0
        for coin in coins:
            while total + coin <= 2:
                print "appending coin", coin
                total += coin
                combo[coin] += 1
                list.append(coin)
            if total == 2:
                print "found way: ", list
                num_ways += 1
                combo[coin] -= 1
                total -= 2
                list = []
                for c in coins:
                    for freq in range(combo[c]):
                        list.append(c)
                print "new list:", list
                return
            
                    
if __name__ == "__main__":
    print answerr() # 

    