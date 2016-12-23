#!/bin/python
# Mini-Max Sum: https://www.hackerrank.com/challenges/mini-max-sum

import sys

lst = [(int)(x) for x in input().strip().split(' ')]
x = sum(lst)
print (x- max(lst), x-min(lst))
