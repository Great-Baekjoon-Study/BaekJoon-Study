# 깃허브 왜케어려워요
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    wbr_map = [[0] * 3 for _ in range(N)]

    for c in range(N):
        w = 0
        b = 0
        r = 0
        for d in range(M):
            if arr[c][d] == 'W':
                w += 1
            elif arr[c][d] == 'B':
                b += 1
            elif arr[c][d] == 'R':
                r += 1
        wbr_map[c][0] = M - w
        wbr_map[c][1] = M - b
        wbr_map[c][2] = M - r
        # M - w,b,r 각 줄을 특정색으로 페인트칠 하는 비용

    min_paint = N*M
    # 나올 수 있는 가장 큰 값으로 초기화

    for i in range(N - 2):
        # 흰색은 최소 첫번째 줄을 포함해야하고 이어질 파란/빨간색 위해 N-2, N-1 남겨둠
        for j in range(i + 1, N - 1):
        # 파란색은 i 다음부터, 빨간색 위해 N-1 남겨둠

            paint = 0

            for w_row in range(i + 1):
                paint += wbr_map[w_row][0]

            # 파란색 영역 비용
            for b_row in range(i + 1, j + 1):
                paint += wbr_map[b_row][1]

            # 빨간색 영역 비용
            for r_row in range(j + 1, N):
                paint += wbr_map[r_row][2]

            # 4. 최솟값 갱신
            if paint < min_paint:
                min_paint = paint

    print(f'#{tc} {min_paint}')
    