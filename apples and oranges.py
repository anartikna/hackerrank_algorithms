'''Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where  is the start point, and  is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .

When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right.

Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?

For example, Sam's house is between  and . The apple tree is located at  and the orange at . There are  apples and  oranges. Apples are thrown  units distance from , and  units distance. Adding each apple distance to the position of the tree, they land at . Oranges land at . One apple and two oranges land in the inclusive range  so we print.
Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
Input Format

The first line contains two space-separated integers denoting the respective values of  and .
The second line contains two space-separated integers denoting the respective values of  and .
The third line contains two space-separated integers denoting the respective values of  and .
The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point .
The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point .
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_loc = [z+a for z in apples]
    oranges_loc = [y+b for y in oranges]
    in_range_apple = 0
    in_range_orange = 0
    '''
    ALTERNATIVELY
    from operator import add
    test_list1 = [4, 5, 6, 2, 10]
    test_list2 = [1] * len(test_list1)

    res_list = list(map(add, test_list1, test_list2))

    print(test_list1)
    print(test_list2)
    print(res_list)

                #### Output ####
    [4, 5, 6, 2, 10]
    [1, 1, 1, 1, 1]
    [5, 6, 7, 3, 11]
    '''
    #num_Apples = len(apples_loc)
    #num_Oranges = len(oranges_loc)

    for item in apples_loc:
        if item in range(s,t+1):
            in_range_apple+=1
    
    #print('\n')
    
    for item in oranges_loc:
        if item in range(s,t+1):
            in_range_orange+=1
    print(in_range_apple)
    print(in_range_orange)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
