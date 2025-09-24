# 상근이는 결혼식에 자신의 친구와 친구의 친구 초대함.
# 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지
# 상근이의 학번은 1
# 결혼식에 초대할 사람의 수 구하기

from collections import deque

n = int(input()) # 상근이의 동기의 수
m = int(input()) # 리스트의 길이

friend = [[] for _ in range(n + 1)] # 친구 관계를 담은 리스트
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

visited = [0] * (n + 1)
q = deque()
q.append((1, 0)) # (현재 노드, 깊이)
visited[1] = 1

count = 0 # 결혼식에 초대할 사람의 수

while q:
    node, depth = q.popleft()

    # 친구의 친구까지만 허용 (depth 2 이하)
    if 0 < depth <= 2:
        count += 1

    if depth == 2:
        continue # 더 깊이 들어가면 안 됨

    for next_node in friend[node]:
        if visited[next_node] == 0:
            visited[next_node] = 1
            q.append((next_node, depth + 1))

print(count)


