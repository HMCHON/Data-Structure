'''
Problem 1 완주하지 못한 선수

[문제 요점]
1. 동명이인의 처리
2. 효율성
'''

def solution(p, c):

# a - A - b - B - ... - Z 순으로 정렬
p.sort()
c.sort()

# zip 이용해 합치기
for participant, completion in zip(p, c):  
    if participant != completion: 
        return participant  # p = ['a', 'b', 'b', 'c']  / c = ['a', 'b', 'c'] -> zip -> [('a','a'), ('b','b'), ('b','c')]
return participant[-1]  # p= ['a', 'b'] / c = ['a'] -> zip -> [('a','a')]



'''
다른 풀이 [1]

[풀이 요점]
1. collections의 Counter 객체는 서로 빼기가 가능하다
2. answer.keys() => dict_keys(['leo']
   list(answer.keys())[0] => leo
'''

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
  
  
  
  
  
