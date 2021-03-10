'''
Problem 2 가장 큰 수
채점 결과
정확성: 27.3
합계: 27.3 / 100.0
'''

from collections import defaultdict, Counter
from operator import itemgetter

def solution(numbers):
    
    zfil_num = []
    for i in numbers:
        zfil_num.append(str(i).ljust(len("".join([str(_) for _ in numbers])), '0'))
    
    
    e = list(range(len(numbers))) # [0, 1, 2]
    a = defaultdict(lambda:[])
    for k, v in zip(e,zfil_num):
        a[k].append(v) # {0: ['6000'], 1: ['1000'], 2: ['2000']})
    
    rank = [num1 for num1, num2 in sorted(a.items(), key = itemgetter(1), reverse = True)] #[0, 2, 1]
    
    answer = []
    for i in rank:
        answer.append(str(numbers[i]))
    answer = (''.join(answer))

    return answer
  
  
  
