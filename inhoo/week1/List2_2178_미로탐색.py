# DFS 사용, 런타임 에러 발생
# 갈림길의 좌표, 최소 칸의 수



n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
# 1 2 0
# 0 0 0
# 0 0 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

def dfs(x,y): #x,y는 시작점 # 좌표
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
    
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
            if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                #한 번도 안 가본 길이거나 더 짧은 거리라면 거리값을 갱신
                visited[nx][ny] = visited[x][y] + 1
                if nx == n-1 and ny ==m-1:
                    return
                dfs(nx,ny)
    return

dfs(0,0)
print(visited[n-1][m-1])

