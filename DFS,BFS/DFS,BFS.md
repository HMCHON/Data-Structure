# 깊이/너비 우선 탐색 (DFS/BFS)

>_✨M코딩테스트에서 2차원 배열의 탐사 문제를 만난다면 그래프 형태로 바꿔 접근✨_



![image](https://user-images.githubusercontent.com/49745654/110678131-4ea28880-8219-11eb-963b-00435a4d8fae.png)

- 스택 : 박스쌓기, 박스는 아래에서 위로 쌓을 수 있음, 아래있는 박스는 위 박스를 치운 후 획득 가능
        (선입후출 First in, Last out) or (후입선출 Last in, First out)
- 큐   : 대기줄, 선입설출(First in, First out)
- DFS : Depth-First Search 깊이 우선 탐색 알고리즘, 그래프를 탐색, 멀리있는 노드를 우선으로 탐색 (스택이용)
- BFS : 너비우선탐색, 가까운 노드부터 탐색 (큐 이용하면 효과적으로 구현) 
------------------------------
## Stack 스택
```sh
stack = []

# IN(5) - IN(2) - IN(3) - IN(7) - DEL() - IN(1) - IN(4) - DEL()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop

print(stack) # 최하단 원소부터 출력 # [5, 2, 3, 1]
print(stack[::-1]) # 최상단 원소부터 출력 #[1, 3, 2, 5]
```

------------------------------
## Queue 큐
```sh
from collections import deque
queue = deque()

#IN(5) - IN(2) - IN(3) - IN(7) - DEL() - IN(1) - IN(4) - DEL()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.append()

print(queue) # 먼저 들어온 순서대로 출력 # deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 순서대로 출력 # deque([4, 1, 7, 3])
```
------------------------------
### DFS (Depth-First Search)
1. 인접 리스트 방식 예제
    - 장점 : 메모리 효율적으로 사용
    - 단점 : 두 노드가 연결되어 있는지 정보를 얻는 속도가 느림
    = 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 리스트 방식 사용
```sh
graph = [[]for_in range(3)] #[[],[],[]]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph) # [[(1,7),(2,5)], [(0,7)], [(0,5)]]
```
2. DFS 스택 자료구조 동작 과정
  1) 탐색 시작 노드를 스택에 삽입하고 방문 처리
  2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리
      방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3) 2)번의 과정을 더이상 수행할 수 없을 때까지 반복
```sh
def dfs(graph, v, visited):
  visited[v] = True # 현재 노드를 방문처리
  print(v, end='')
  for i in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 (숫자 작은 순서)
    if not visited[i]:
      dfs(graph, i, visited)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]]
    
viited = [False] * 9 # 각 노드가 방문된 정보를 리스트 자료형으로 표현
dfs(graph, 1, visited)
```
------------------------------
### BFS (Breadth-First Search)
2. BFS 큐 자료구조 동작 과정
  1) 탐색 시작 노드를 스택에 삽입하고 방문 처리
  2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 후 방문처리
  3) 2)번의 과정을 더이상 수행할 수 없을 때까지 반복
```sh
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end='')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5], 
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]]

visited = [False] * 9
bfs(graph, 1, visited) # 1 2 3 6 7 4 5 6
```

### list 다루기
```sh
list1 = [[1, 10], [2, 22], [3, 19]]
list2 = [[4, 2], [5, 9], [6, 3]]

list3 = list(map(list.__add__, list1, list2))
print(list3) # [[1, 10, 4, 2], [2, 22, 5, 9], [3, 19, 6, 3]]
```

```sh
import itertools

list1 = [[1, 10], [2, 22], [3, 19]]
list2 = [[4, 2], [5, 9], [6, 3]]

list3 = list(map(list.__add__, list1, list2))
list4 = list(itertools.chain(*list3))
print(list4) # [1, 10, 4, 2, 2, 22, 5, 9, 3, 19, 6, 3]
```

```sh
list1 = [[1, 10], [2, 22], [3, 19]]
list2 = [[4, 2], [5, 9], [6, 3]]

list3 = list(zip(list1, list2))
print(list3) # [([1, 10], [4, 2]), ([2, 22], [5, 9]), ([3, 19], [6, 3])]
```
```sh
array = list(product([+1,-1], repeat=(n-1)))
print(array) # [(1, 1, 1, 1), (1, 1, 1, -1), (1, 1, -1, 1), ... (1, 1, -1, -1)]
```





















