#!/bin/python
# Designer PDF Viewer: https://www.hackerrank.com/challenges/designer-pdf-viewer
# 한 단어를 형광펜칠 할때에 그 면적 계산하기
# 알파벳 소문자 각각의 높이가 입력값으로 제시되며 가로는 1이라 한다.
# 입력되는 단어별 높이를 리스트로 받아둔 다음, 그 리스트의 최대값(=최대 높이)와 길이를 곱해주면 면적이다

import sys

size = [(int)(x) for x in input().strip().split()]
word = [size[ord(c)-ord('a')] for c in input().strip()]
print(max(word) * len(word))
