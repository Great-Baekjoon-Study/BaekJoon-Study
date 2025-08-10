N, M = map(int, input().split())  # 4 6
miro = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N * M):
    for i in range(N):
        for j in range(M):
            # 방문 가능한 칸(0은 벽)
            if miro[i][j] > 0:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if miro[ni][nj] == 1:
                            miro[ni][nj] = miro[i][j] + 1

print(miro[N-1][M-1])
