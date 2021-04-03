# 자물쇠와 열쇠 (프로그래머스)
'''
1. 행렬을 90도로 회전
2. 행렬에 풀링
3. 행렬 특정 영역 모든 요소 1인지 확인
4. M<=N일때 M이 N의 모든 요소에 대입되어 계산
'''




def rotate_90(key):
    key1 = [[0]*len(key) for _ in range(len(key))]    
    for i in range(len(key)):
        for j in range(len(key)):
            key1[j][len(key)-i-1] = key[i][j]
            
    return key1
    

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	

def sum_all(array):
    a = 0
    length = len(array)//3
    for i in range(length,length*2):
        for j in range(length,length*2):
            if array[i][j] != 1:
                return False
    return True

def solution(key, lock):
    array = [[0]*len(lock)*3 for _ in range(len(lock)*3)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            array[i+len(lock)][j+len(lock)] = lock[i][j]
    for rot in range(4):
        key = rotate_90(key)
        for x in range(len(lock)*2):
            for y in range(len(lock)*2):
                for i in range(len(key)):
                    for j in range(len(key)):
                        array[i+x][j+y] += key[i][j]
                if sum_all(array) == True:
                    return True
                for i in range(len(key)):
                    for j in range(len(key)):
                        array[i+x][j+y] -= key[i][j]
    return False
    
print(solution(key, lock))
