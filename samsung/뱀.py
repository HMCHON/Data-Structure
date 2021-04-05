'''
1. 뱀이 차지하고 있는 범위를 알기 위한 map 생성
2. 뱀이 이동하는 좌표를 map에 갱신하기 위한 dx, dy 요소 활용
3. queue를 이용해서 뱀이 사과먹을 때 길이 늘어나서 꼬리를 삭제하지 않는 함수 구현
4. index를 사용해 time이 방향 전환 시간과 일치할 때 방향 전환하는 함수 구현
''' 
n = int(input()) # 맵의 크기
m = [[0]*(n+1) for _ in range(n+1)] # 맵의 크기만한 0행렬

apple = int(input()) # 반복을 위한 사과 갯수 입력 받기
for _ in range(apple):
    a,b = map(int, input().split()) # 사과 위치 받기
    m[a][b] = 1 # 맵에 사과 위치를 1로 표시

D = int(input()) # 방향 전환 횟수 입력 받기
info = []
for _ in range(D): 
    info.append(input().split()) # info 리스트에 (방향전환시간, 방향전환방향) 입력

# 방향 전환을 위한 dx,dy
dx = [0, 1, 0, -1] # 동-남-서-북
dy = [1, 0, -1, 0] # 동-남-서-북

def turn(direction, c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction

def solve():
    time = 0
    index = 0
    direction = 0
    x, y = 1,1
    q = [(x,y)] # 뱀 머리가 있는 곳 queue
    
    m[x][y] = 2 # 뱀 머리가 있는 곳을 2로 표시
    
    while True:
        # 처음에는 direction = 0 이므로 동쪽으로 이동
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 맵 범위 안에 있으며 벽이나 몸통을 만나지 않으면
        if 1<=nx and nx<=n and 1<=ny and ny<=n and m[nx][ny]!=2:
            
            # 사과가 없으면
            if m[nx][ny] == 0:
                m[nx][ny] = 2 # 뱀 머리 이동
                q.append((nx,ny))
                qx, qy = q.pop(0)
                m[qx][qy] = 0 # queue에서 가장 첫번째 요소 꺼내서 0으로 변환
            
            # 사과가 있으면
            if m[nx][ny] == 1:
                m[nx][ny] = 2 # 뱀 머리 이동
                q.append((nx, ny))
            
        else:
            time += 1
            break
        
        x = nx
        y = ny
        time += 1
        
        if index < D and time == int(info[index][0]): # 방향 전환 해야하는 순간
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(solve())
