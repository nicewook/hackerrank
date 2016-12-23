#!/bin/python
# Kangaroo: https://www.hackerrank.com/challenges/kangaroo
# 캥거루 두 마리가 x1, x2에서 한번에 v1, v2만큼 점프하는데 만날 수 있나?
# x1 < x2 이다.
# 따라서 무조건 v1 > v2이어야 하고 x1, x2의 초기 거리차가 v1, v2 차이의 배수여야 한다.

import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v1 > v2 and (x2-x1)%(v1-v2) == 0:
    print("YES")
else:
    print("NO")
