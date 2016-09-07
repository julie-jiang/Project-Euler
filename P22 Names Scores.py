# -*- coding: utf-8 -*-
'''
P22 Names Scores
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
    containing over five-thousand first names, begin by sorting it into 
    alphabetical order. Then working out the alphabetical value for each name, 
    multiply this value by its alphabetical position in the list to obtain a 
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which 
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, 
    COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
'''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def answer():
    names = read_file()
    names = quick_sort(names, 0, len(names) - 1)
    score = 0
    for index in range(len(names)):
        score += (index + 1) * abc_value(names[index])
    return score
    
def quick_sort(list_, lo, hi):
    '''
    Quick sort algorithm
    '''
    if lo < hi:
        p = partition(list_, lo, hi)
        quick_sort(list_, lo, p - 1)
        quick_sort(list_, p + 1, hi)
    return list_

def partition(list_, lo, hi):
    '''
    Partition the list so that everything that comes before the pivot (here I
    arbitrarily chose the last item in the list) is less than the pivot, and 
    everything that comes after the pivot is greater than the pivot.
    Returns the final index of the pivot.
    '''
    pivot = list_[hi]
    i = lo
    for j in range(lo, hi):
        if list_[j] <= pivot:
            temp = list_[j]
            list_[j], list_[i] = list_[i], temp
            i += 1
    temp = list_[i]
    list_[i], list_[hi] = pivot, temp
    return i
    
def abc_value(name):
    '''
    Calculates the alphabetical value of the name
    '''
    score = 0
    for letter in name:
        score += alphabet.index(letter) + 1
    return score          
            
def read_file():
    filename = \
    open("/Users/Jiang/Desktop/Project Euler/Supporting Files/P22 Names.txt")
    filename = filename.read()
    filename = filename.split('","')
    filename[0] = filename[0].lstrip('"')
    filename[-1] = filename[-1].rstrip('"')
    return filename

if __name__ == "__main__":
    print answer() # 871198282