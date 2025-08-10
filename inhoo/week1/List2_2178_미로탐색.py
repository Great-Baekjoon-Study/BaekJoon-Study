#미로탐색

# 뒤 :뒤에서 온 길은 다시는 가지 말기(다른 길 실패했을 경우에는 다시 돌아가기)
# 왼,앞,오
# 범위 밖으로 벗어나는지 확인
# 3갈래 길이 발생했을 때, 3개 다 가보고 판단
#가서 갈 곳이 없을 때, 다시 조건문으로 돌아가기


N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]


distance = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


start_point = [(0, 0)]  # 시작점 넣기
front = 0         # 맨 앞에서부터 차례대로 꺼내 쓰기 위한 번호(인덱스)

# 시작칸도 "칸 수"에 포함되니까 1로 시작
distance[0][0] = 1

# 6 이제 반복 시작
while front < len(start_point):
    # 앞에서 하나 꺼내오기
    i, j = start_point[front]
    front += 1

    #도착지에 도착
    if i == N - 1 and j == M - 1:
        print(distance[i][j])
        break

    # 현재칸에서 다음 행
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]

        #판 안에서만 돌리기
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[i][j] + 1

                start_point.append((nx, ny))
