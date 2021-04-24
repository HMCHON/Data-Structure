import sys
#sys.stdin = open('input.txt','r')

N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)] #비료 밭
B = [[5]*N for _ in range(N)] #처음 밭
T = [[[] for _ in range(N)] for _ in range(N)] #나무

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

for _ in range(M):
    x,y,a = map(int,input().split())
    T[x-1][y-1].append(a)

for year in range(K):
    
    # 봄 + 여름
    for i in range(N):
        for j in range(N):
            if T[i][j]:
                T[i][j].sort() # 나이 낮은 순으로 정렬
                grow_tree = []
                dead_tree = 0
                for age in T[i][j]:
                    if age <= B[i][j]:
                        B[i][j] -= age
                        age += 1
                        grow_tree.append(age)
                    else:
                        dead_tree += age //2
                B[i][j] += dead_tree # 죽은 나무 비료로 뿌리기
                T[i][j] = []
                T[i][j].extend(grow_tree) # 자란 나무 정보 기입
    
    # 가을
    for i in range(N):
        for j in range(N):
            if T[i][j]:
                for age in T[i][j]:
                    if age % 5 == 0: # 나이가 5의 배수이면
                        for k in range(8):
                            new_x = i + dx[k]
                            new_y = j + dy[k]
                            if 0<=new_x<N and 0<=new_y<N:
                                T[new_x][new_y].append(1)
    
    #겨울
    for i in range(N):
        for j in range(N):
            B[i][j] += A[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(T[i][j])
print(cnt)
    
    
    
