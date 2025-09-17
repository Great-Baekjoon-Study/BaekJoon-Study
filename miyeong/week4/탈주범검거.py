# 터널끼리 연결되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수
# 탈주범은 시간당 1의 거리를 움직일 수 있음.

# import sys
# sys.stdin = open('sample_input (19).txt', 'r')

# 1. BFS로 접근
#   - 이동 방향 : 상하좌우
#   - 이동이 불가능한 케이스
#       - [델타 배열 기본] 범위 밖으로 나가면 못 감
#       - [방문 기록 기본] 이미 방문한 곳은 못 감
#       - [0이면 못 간다]
#       - [문제 조건]
#           - 현재 내 위치에서 뚫려 있는 곳만 이동 가능
#           - 다음 위치의 입구가 뚫려있는 곳으로만 가능
#             -> 이런 케이스들은 델타배열과 동일한 순서 (상하좌우)
#               이동 가능 여부를 기록해두면 좋다.

# 2. 방문 기록을 해야한다

# 델타배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널들의 종류에 따라, 이동 가능 여부를 기록
types = {
    # 상하좌우 순서로 기록
    1 : [1, 1, 1, 1],
    2 : [1, 1, 0, 0],
    3 : [0, 0, 1, 1],
    4 : [1, 0, 0, 1],
    5 : [0, 1, 0, 1],
    6 : [0, 1, 1, 0],
    7 : [1, 0, 1, 0]
}

def bfs(R, C):
    q = [(R, C)] # 후보군
    visited[R][C] = 1 # 출발점 초기화

    while q: # 후보군이 없을 때까지(더 이상 방문할 수 있는 곳이 없으면 종료)
        now_y, now_x = q.pop(0)
        dirs = types[graph[now_y][now_x]]

        for dir in range(4): # 상하좌우 확인
            # 출구가 없으면 다음 방향 확인 (continue)
            if dirs[dir] == 0:
                continue

            # 다음 좌표
            new_y = now_y + dy[dir]
            new_x = now_x + dx[dir]

            # 범위 밖이면 pass
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            # 못 가는 곳이면 pass
            if graph[new_y][new_x] == 0:
                continue

            # 이미 방문했으면 pass
            if visited[new_y][new_x]:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[graph[new_y][new_x]]

            # 현재 상좌 -> next_dirs가 하우 가 안 뚫렸으면 못 간다
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue

            # 현재 하우 -> next_dirs의 상좌 가 안 뚫렸으면 못 간다
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            # L 시간 이후는 볼 필요 없다
            if visited[now_y][now_x] + 1 > L:
                continue

            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[now_y][now_x] + 1
            q.append((new_y, new_x))



T = int(input())
for test_case in range(1, T+1):
    # N : 세로 크기
    # M : 가로 크기
    # R : 맨홀 뚜껑이 위치한 장소의 세로 위치
    # C : 맨홀 뚜껑이 위치한 장소의 가로 위치
    # L : 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())

    # 지하 터널 지도 정보
    # 숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미하며 숫자 0은 터널이 없는 장소를 의미
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 특정 좌표까지 몇 시간이 걸렸는 지 기록
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)
    cnt = 0

    # L 시간 이하로 방문한 모든 곳을 count
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{test_case} {cnt}')