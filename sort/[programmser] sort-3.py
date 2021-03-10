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
정확성: 100.0
합계: 100.0 / 100.0
'''     

def solution(cit):
    cit.sort() #[0,1,3,5,6]
    h, k, answer = 0,0,0
    if cit[0] >= len(cit):
        return len(cit)
        
    for i in range(0,cit[-1]+1):
       
        h = sum(j>=i for j in cit) # i번 이상 인용 된 논문 수 구하기 2
        k = sum(j<=i for j in cit) # i번 이하 인용 된 논문 수 구하기 2
        if h>=i and k<=i: # 조건만족확인1
            answer = i
    return answer
