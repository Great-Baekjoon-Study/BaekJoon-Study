# N, M = map(int, input().split())  # 4 6
# miro = [list(map(int, input().strip())) for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for _ in range(N * M):
#     for i in range(N):
#         for j in range(M):
#             # 방문 가능한 칸(0은 벽)
#             if miro[i][j] > 0:
#                 for k in range(4):
#                     ni = i + dx[k]
#                     nj = j + dy[k]
#                     if 0 <= ni < N and 0 <= nj < M:
#                         if miro[ni][nj] == 1:
#                             miro[ni][nj] = miro[i][j] + 1

# print(miro[N-1][M-1])


n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 델타 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 위치
x, y = 0, 0

# 이동할 좌표들을 저장하는 리스트 (큐 역할)
queue = [(x, y)]

# while문으로 이동 가능한 곳을 탐색
while queue:
    x, y = queue.pop(0)  # 리스트에서 맨 앞 원소 꺼내기
    
    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 안이고, 길(1)인 경우
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1  # 거리 갱신
            queue.append((nx, ny))         # 다음에 탐색할 위치 저장

# 결과 출력
print(maze[n-1][m-1])
