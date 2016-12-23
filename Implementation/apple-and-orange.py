#!/bin/python
# Apple and Orange  https://www.hackerrank.com/challenges/apple-and-orange
# 사과나무 - 집 - 오렌지나무가 있다.
# 나무로부터 떨어진 과일의 거리와 집의 범위를 통해, 집에 떨어진 과일의 개수를 각각 계산한다
# 나무로부터 떨어진 과일의 거리와 나무위치를 더한 값과 집 범위를 비교해 참인 경우에만 1을 리스트에 추가하고 합을 구한다

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

print(sum([1 for x in apple if a+x >=s and a+x <=t]))
print(sum([1 for x in orange if b+x >=s and b+x <=t]))
