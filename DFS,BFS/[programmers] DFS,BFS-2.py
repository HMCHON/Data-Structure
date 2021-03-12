'''
problem 2 네트워크

채점 결과
정확성: 15.4
합계: 15.4 / 100.0

-> 크기가 1인 노드도 count하는 문제 발생
    = 네트워크를 탐색하는 알고리즘으로 수정 필요
'''

def dfs(graph, x, y,n):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2
        dfs(graph, x-1, y,n)
        dfs(graph, x, y-1,n)
        dfs(graph, x+1, y, n)
        dfs(graph, x, y+1, n)        
        return True        
    return False
    

def solution(n, computers):
    result = 0
    for i in range(n):
        for j in range(n):
            if dfs(computers, i, j,n) == True:
                result += 1
    return result
  
  
  '''
  
  '''
from collections import deque

# BFS 메서드 정의
def bfs(graph,start, visited):
	queue = deque([start])
	visited[start] = True # 방문한 노드에 체크
	while queue: #큐가 빌 때까지 반복
		v = queue.pop() #큐에서 하나의 원소 뽑아 출력
		#해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
		for i in graph[v]: 
			if not visited[i]:
				queue.append(i)
				visited[i] = True
	return True

def solution(n, computer):
	result = 0
	visited = [False]*n
	for i in computer:
		if bfs(computer, i, visited) == True:
			result += 1
	return result
    
  
  
