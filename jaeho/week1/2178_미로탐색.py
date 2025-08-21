# 1차 시도
"""
N, M = map(int, input().split())
# N이 가로길이 M이 세로길이
arr = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(M):
i = 0
j = 0
# # [0, 0]에서부터 시작 
# # 왼쪽 오른쪽 끝까지 이동
count = 0
# 결국 좌표 [N][M] 으로 가야하는데
while i == N and j == M:
    if arr[i][j+1] == 1:
        j += 1
        count += 1
        continue
    elif arr[i+1][j] == 1:
        i += 1
        count += 1
        continue
    else :
        i -= 1
    
"""
# gpt 피드백 
"""
작성하신 코드는 '단순한 규칙'에 기반한 탐욕(Greedy) 알고리즘과 유사합니다. 
"일단 오른쪽으로 갈 수 있으면 가고, 안되면 아래로 가자" 와 같은 방식이죠.
 이런 방식은 미로 문제 해결에 다음과 같은 치명적인 약점들을 가지고 있습니다.

1. 최단 경로를 보장하지 않음
이것이 가장 근본적인 문제입니다. 미로 탐색은 '지금 당장 좋아 보이는 길'이 아니라
 '전체적으로 가장 짧은 길'을 찾아야 합니다.

 
2. 2. 막다른 길이나 무한 루프에 빠질 수 있음
"""
# N(행), M(열) 크기를 입력받습니다.
N, M = map(int, input().split())

# 미로 정보를 2차원 리스트로 입력받습니다.
# 입력이 '10111'처럼 공백 없이 주어지므로, 문자열을 한 글자씩 숫자로 변환합니다.
maze = []
for _ in range(N):
    maze.append([int(char) for char in input()])

# 방문 여부 및 거리 계산을 위한 2차원 리스트를 0으로 초기화합니다.
distance = [[0] * M for _ in range(N)]

# BFS를 위한 큐를 생성합니다.
q = deque()

# 시작점 (0, 0)을 큐에 추가하고 거리를 1로 설정합니다.
q.append((0, 0))
distance[0][0] = 1

# 상, 하, 좌, 우 방향을 나타내는 dr, dc 리스트
dr = [-1, 1, 0, 0]  # 행(row) 변화량
dc = [0, 0, -1, 1]  # 열(column) 변화량

# 큐가 빌 때까지 탐색을 계속합니다.
while q:
    # 큐의 맨 앞에서 현재 위치를 꺼냅니다.
    r, c = q.popleft()

    # 현재 위치에서 네 방향을 탐색합니다.
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 다음에 이동할 위치가 미로 범위 안에 있는지 확인합니다.
        if 0 <= nr < N and 0 <= nc < M:
            # 이동할 수 있는 길이고, 아직 방문하지 않았다면
            if maze[nr][nc] == 1 and distance[nr][nc] == 0:
                # 이전 위치의 거리 + 1로 거리를 기록합니다.
                distance[nr][nc] = distance[r][c] + 1
                # 다음 탐색을 위해 큐에 추가합니다.
                q.append((nr, nc))

# 도착점(N-1, M-1)에 기록된 최종 거리를 출력합니다.
print(distance[N-1][M-1]) 




