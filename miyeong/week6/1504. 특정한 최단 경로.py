# 방향성이 없는 그래프
# 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하고자 함.
# 임의로 주어진 두 정점은 반드시 통과해야 함.
# 한번 이동했던 정점과 간선 모두 다시 이동할 수 있음.
# 주어진 두 정점을 반드시 거치면서 최단 경로로 이동

# 다익스트라
# 1. 구해야 하는 경로
#   - 1 -> v1 -> v2 -> N
#   - 1 -> v2 -> v1 -> N
#   - 두 가지 경우 모두 계산 후 최솟값 선택
# 2. 최소한 다음 구간들의 최단 거리를 알아야 함.
#   - 1 -> v1, 1 -> v2
#   - v1 -> v2
#   - v1 -> N, v2 -> N
# 3. 다익스트라를 총 3번 돌려야 함.
#   - 시작점 1에서의 최단 거리
#   - 시작점 v1에서의 최단 거리
#   - 시작점 v2에서의 최단 거리

import heapq

INF = int(1e9) # 무한대를 나타내는 값

def dijkstra(start):
    dist = [INF] * (N + 1)              # 거리 배열 초기화
    dist[start] = 0                     # 시작점은 자기 자신까지 거리 0
    pq = []                             # 우선순위 큐
    heapq.heappush(pq, (0, start))      # (거리, 정점) 형태로 넣기

    while pq:
        cur_dist, now = heapq.heappop(pq) # 현재 거리, 현재 정점 꺼내기
        
        # 이미 처리된 거리보다 크면 무시
        if dist[now] < cur_dist:
            continue
        
        # 현재 정점과 연결된 모든 인접 노드 확인
        for next, cost in graph[now]:
            new_dist = cur_dist + cost      # 현재까지 거리 + 간선 비용
            if new_dist < dist[next]:       # 더 짧은 경로 발견 시 갱신
                dist[next] = new_dist
                heapq.heappush(pq, (new_dist, next))
    return dist

# N : 정점의 개수
# E : 간선의 개수
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split()) # 반드시 거쳐야 하는 두 개의 정점 번호

# 다익스트라 3번 실행
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 1 -> v1 -> v2 -> N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]

# 1 -> v2 -> v1 -> N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

answer = min(path1, path2)

if answer < INF:
    print(answer)
else:
    print(-1)