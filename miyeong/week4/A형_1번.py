# 나삼성씨가 새로 나온 게임을 구입
# 이 게임은 아래와 같이 가로, 세로 N x N 크기의 지도에 주어진 사과를 순서대로 먹는 게임
# 사과는 번호 순서에 따라 차례대로 지도에 나타남.
# 예를 들어, 1번 사과를 먹으면 2번 사과가 나타나고, 2번 사과를 먹으면 3번 사과가 나타남.
# 2번 사과를 1번 사과보다 먼저 먹는 것은 불가능
# 플레이어의 시작 위치는 좌측 상단으로 고정되어있음.
# 게임을 시작하면 자동으로 화살표 방향으로 전진하고, 회전을 하는데 오른쪽으로 90도씩으로만 회전 가능
# 사과를 먹음과 동시에 회전하는 것도 가능
# 지도 상에 모든 사과를 먹으면 게임 종료
# 회전 횟수를 최소화하여 순서대로 모든 사과를 먹으려면, 최소 몇 번의 회전이 필요한지 구하기
# 새로운 사과가 나타날 때 바로 직전 사과와 동일한 열/행에 나타나지 않음.
# 지도의 가장자리 영역에는 사과가 나타나지 않음.

# 1 7
# 2 9
# 3 10
# 4 14
# 5 23

import sys
sys.stdin = open('input (17).txt', 'r')

from collections import deque

# 방향 정의 : 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# N : 보드 크기
# start : (x, y, d) -> 시작 좌표와 방향
# target : (x, y) -> 목표 사과 좌표
def bfs(N, start, target):
    sx, sy, sd = start # 시작 위치 (x, y)와 방향 d
    tx, ty = target    # 목표 위치 (사과의 위치)

    INF = float('inf')
    # dist[x][y][d] = (x, y)에 방향 d로 도달했을 때 최소 회전 횟수
    dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    dist[sx][sy][sd] = 0 # 시작점 초기화 => 이미 거기에 도착해 있는 상태이기 때문에 필요한 회전 횟수는 0번

    q = deque()
    q.append((sx, sy, sd)) # 시작 상태 큐에 삽입

    while q:
        x, y, d = q.popleft()

        # 목표 사과 좌표에 도달하면 회전 횟수 반환
        if (x, y) == (tx, ty):
            return dist[x][y][d], d

        # --- 이동 방법 2가지 ---

        # 1. 직진 (회전 없음, 비용 0)
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N: # 보드 안쪽일 경우만
            # dist[nx][ny][d] : 새 위치 (nx, ny)에서 방향 d로 도달했을 때의 최소 회전 횟수
            # dist[x][y][d] : 현재 위치 (x, y)에서 방향 d로 도달한 최소 회전 횟수
            # 직진 이동은 회전이 없으므로 비용 0
            # 만약 기존 값보다 작으면 더 작은 회전 횟수로 도달 가능 -> 갱신
            if dist[nx][ny][d] > dist[x][y][d]:
                dist[nx][ny][d] = dist[x][y][d]
                q.appendleft((nx, ny, d)) # 비용 0 -> 덱 앞에 넣음

        # 2. 오른쪽 회전 후 직진 (회전 비용 1)
        nd = (d + 1) % 4 # 방향을 오른쪽으로 90도 회전
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < N and 0 <= ny < N:
            if dist[nx][ny][nd] > dist[x][y][d] + 1:
                dist[nx][ny][nd] = dist[x][y][d] + 1
                q.append((nx, ny, nd)) # 비용 1 -> 덱 뒤에 넣음

        # 직진은 덱 앞에 넣고, 회전은 덱 뒤에 넣는 이유
        # - 지금은 최소한의 회전 횟수를 구하기 때문에 비용 0은 지금 거리와 같으니가 큐의 앞쪽에 넣어서 즉시 탐색
        # - 비용 1은 한 칸 더 큰 거리니까 큐의 뒤쪽에 넣어서 나중에 탐색

    # 목표 사과 위치에 도달하지 못했을 경우
    # INF : dist 배열에서 초기화 값 INF와 동일
    # sd : 시작 방향 그대로 반환
    return INF, sd

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 지도의 한 변의 크기
    grid = [list(map(int, input().split())) for _ in range(N)] # 지도 정보

    apples = [] # 사과 좌표들 (순서대로 먹어야 함)

    idx = 1 # 1번 사과 좌표부터 찾을 거임.
    while idx <= 10: # 사과들의 개수는 2 이상 10 이하이므로, 사과 번호는 최대 10번까지임.
        for i in range(N):
            for j in range(N):
                if grid[i][j] == idx:
                    apples.append((i, j))

        idx += 1

    total_turns = 0 # 최소 몇 번의 회전

    # 시작점 :(0, 0)에서 오른쪽(0) 바라보고 시작
    start = (0, 0, 0)

    for apple in apples:
        turns, new_dir = bfs(N, start, apple) # 최소 회전 횟수와 도착 방향
        total_turns += turns

        # 다음 시작점은 현재 사과 위치 + 도착 방향
        start = (apple[0], apple[1], new_dir)

    print(f'#{test_case} {total_turns}')



