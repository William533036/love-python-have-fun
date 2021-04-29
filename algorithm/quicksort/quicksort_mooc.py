# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  黄英杰
@Version        :  1.0.0
------------------------------------
@File           :  quicksort_mooc.py
@Description    :  
@CreateTime     :  2021/4/29 0029 下午 12:22
@微信号          :  HelperRobot
------------------------------------
@ModifyTime     :  
"""

def quicksort(alist, first=None, last=None):


    first = 0 if not first else first
    last = len(alist)-1 if not last else last
    quicksortHelper(alist, first, last)

def quicksortHelper(alist, first, last):
    if first<last:
        splitpoint = partition(alist, first, last)
        quicksortHelper(alist, first, splitpoint - 1)
        quicksortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    value = alist[first]

    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and alist[left] <= value:
            left = left + 1

        while  right >= left and alist[right] >= value:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = alist[left]
            alist[left] = alist[right]
            alist[right] = temp

    temp = alist[first]
    alist[first] = alist[right]
    alist[right] = temp
    return right



if __name__ == '__main__':
    import random
    list1 = [random.randint(0,99) for _ in range(10)]
    print(list1)
    quicksort(list1)
    print(list1)


