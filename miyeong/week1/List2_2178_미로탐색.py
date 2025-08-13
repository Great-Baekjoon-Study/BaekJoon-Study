n, m = map(int, input().split()) # 미로의 세로 크기, 가로 크기
maze = [list(map(int, input().strip())) for _ in range(n)] # 미로 정보를 2차원 리스트로 저장

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
        
        # 범위 안이고, 아직 방문하지 않았고 길(1)인 경우
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1  # 거리 갱신 = 이전 칸 거리 + 1
            queue.append((nx, ny))         # 다음에 탐색할 위치 저장

# 결과 출력
# 도착점(맨 오른쪽 아래)의 값 출력
print(maze[n-1][m-1])
