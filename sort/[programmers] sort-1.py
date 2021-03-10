'''
Problem 1 K번째수

채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

def solution(array, commands):
    
    answer = []
    for i in commands:
        start = i[0] # 2  -----> # start, end, k = i
        end = i[1] # 5
        k = i[2] # 3
        first_array = array[start-1:end]   # ------> answer.append(list(sorted(array[i-1:j]))[k-1]
        second_array = sorted(first_array, reverse = False) # ------┐-----------------------------
        answer.append(second_array[k-1]) # -------------------------┘
    return answer
  
  
'''
다른 풀이 [1]
[풀이 요점]
1. lambda 사용을 유연하게 하기
'''

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
