'''
Problem 3 위장


[문제 요점]
1. 경우의 수 고려할 때 안 입는 경우 +1 씩 한 후, 둘다 안 입는 경우 제외해서 -1 해주기.

[1차 시도 결과]
정확성 100.0
합계 100.0 / 100.0
'''

def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans


def solution(clothes):
    c = {}
    for i in clothes:
        c[i[0]] = i[1] # {'yellowhat': 'headgear', 'bluesunglasses': 'eyewear', 'green_turban': 'headgear'}

        v = list(set(c.values())) # ['eyewear', 'headgear']
     
    array = []
    for search_kind in v:
        count = 0
        
        for name, search in c.items():
            if search_kind == search:
                count += 1
        array.append(count+1)
    
    answer = multiply(array) -1 # reduce(lambda x, y: x*y, array) -1 하면 간단하게 가능
    return answer   
  
 
  
'''
다른 풀이 [1]
'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer


'''
다른 풀이 [2]
'''
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1



