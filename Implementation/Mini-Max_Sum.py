#!/bin/python
# Mini-Max Sum: https://www.hackerrank.com/challenges/mini-max-sum
# 여러 정수를 받아서 그 중 하나를 뺀 나머지의 합들 중에서 최소 최대값 찾기
# 전체 합에서 가장 큰 수와 가장 작은 수를 빼면 된다. 
import sys

lst = [(int)(x) for x in input().strip().split(' ')]
x = sum(lst)
print (x- max(lst), x-min(lst))
