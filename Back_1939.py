# 1939
from collections import deque
n, m = map(int, input().split())

graph = dict()
start = 1000000000
end = 1

def dfs(c):
  need_visit = deque([start_node])
  visited = [False] *(n+1)
  visited[start_node] = True
  while need_visit:
    reference = need_visit.popleft()
    for y, weight in graph[reference].items():
      if not visited[y] and weight >= c:
        visited[y] = True
        need_visit.append(y)
  return visited[end_node]
for _ in range(m):
    a, b, weight = map(int, input().split())
    if a not in graph.keys():
        graph[a] = dict()
    if b not in graph.keys():
        graph[b] = dict()
    graph[a][b] = weight
    graph[b][a] = weight
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while(start <= end):
  mid = (start+end)//2
  if dfs(mid):
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)
# 4 4
# 1 3 6
# 1 2 5
# 4 2 4
# 3 4 7
# 1 4    오류 남