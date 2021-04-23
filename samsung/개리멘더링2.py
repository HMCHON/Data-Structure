import sys
sys.stdin = open('input.txt', 'r')

def solve(x,y,d1,d2):
    ch = [list([0]*(n+1)) for _ in range(n+1)]
    ch[x][y] = 5
    for i in range(1,d1+1):
        ch[x+i][y-i] = 5 
        ch[x+d2+i][y+d2-i] = 5
    for i in range(1,d2+1):
        ch[x+i][y+i] = 5
        ch[x+d1+i][y-d1+i] = 5
    
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0

    for r in range(1,x+d1): # 1번 선거구
        for c in range(1,y+1):
            if ch[r][c] == 5:
                break
            a1 += board[r][c]

    for r in range(1,x+d2+1): # 2번 선거구
        for c in range(n,y,-1):
            if ch[r][c] == 5:
                break
            a2 += board[r][c]

    for r in range(x+d1,n+1): # 3번 선거구
        for c in range(1,y-d1+d2):
            if ch[r][c] == 5:
                break
            a3 += board[r][c]

    for r in range(x+d2+1,n+1): # 4번 선거구
        for c in range(n,y-d1+d2-1,-1):
            if ch[r][c] == 5:
                break
            a4 += board[r][c]

    a5 = total_sum-a1-a2-a3-a4
    return max(a1,a2,a3,a4,a5)-min(a1,a2,a3,a4,a5)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    board[i].insert(0,0)
board.insert(0,[0]*(n+1))

total_sum=0
for i in range(n+1):
    for j in range(n+1):
        total_sum += board[i][j]

cnt = 10e9
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if not x+d1+d2 <= n:
                    break
                if not 1<=y-d1:
                    break
                if not y+d2 <= n:
                    break
                cnt = min(cnt, solve(x,y,d1,d2))

print(cnt)
