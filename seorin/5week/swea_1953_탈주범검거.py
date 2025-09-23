from collections import deque
'''
터널이 연결되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수 계산 
탈주범은 시간당 1의 거리를 움직일 수 있음
지하 터널은 총 7 종류의 터널 구조물로 구성

1 = 상하좌우
2 = 상하 
3 = 좌우
4 - 상우
5 = 하우
6 = 하좌
7 = 상좌

* 왼쪽이 세로, 오른쪽이 가로
 ( 2, 1 ) 으로 주어질 경우, 이는 세로 위치 2, 가로 위치 1을 의미

기존 위치에 있는게 1시간 소요 되고 시작 
1시간마다 움직일 수도 있고 안 움직일 수도 있음

탈주범이 있을 수 있는 위치 개수 구하기

bfs로 문제 해결
'''
# 퍼아프별 갈 수 있는 위치 저장
moves = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}

def bfs(x, y, L):
    dq = deque([(x, y, 1)])
    visited[x][y] = True
    cnt = 1

    while dq:
        x, y, t = dq.popleft()

        if t == L : 
            continue
        
        # 얼만큼 움직일거냐? 
        # 그래프 값이 moves 안에 있는 값만큼
        for di, dj in moves.get(tunnel[x][y], []):
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < M : 
                if not visited[nx][ny] and tunnel[nx][ny] != 0 :
                    # -di -dj가 있다는 건 서로 열린 방향이 반대가 있다는 거 => 움직일 수 있음 
                    if (-di, -dj) in moves[tunnel[nx][ny]] :
                        dq.append((nx, ny, t+1))
                        visited[nx][ny] = True
                        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    # N = 세로 크기
    # M = 가로 크기
    # R = 맨홀 뚜껑이 위치한 장소의 세로 위치
    # C = 가로 위치
    # L = 탈출 후 소요된 시간 
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * (M) for _ in range(N)]
    # 맨홀 뚜껑이 시작한 위치가 시작 위치 이때 시간 1 소요 


    result = bfs(R, C, L)

    print(f"#{tc} {result}")