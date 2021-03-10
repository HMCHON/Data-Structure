'''
Problem 3 H-Index

채점 결과
정확성: 12.5
합계: 12.5 / 100.0
'''

from collections import Counter, defaultdict


def solution(cit):
    cit.sort(reverse = True) #[0,1,3,5,6]
    lst = defaultdict(lambda:[])
    for k, v in list(enumerate(cit)):
        lst[k].append(v) 
    for k in lst:
        if k > lst[k][0]:
            answer = lst[k-1][0]
            return answer
          
'''
채점 결과
정확성: 12.5
합계: 12.5 / 100.0
'''     

