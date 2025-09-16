# 방향을 0:RIGHT, 1:DOWN, 2:LEFT, 3:UP (시계방향 순서)로 표현
RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3

def left(facing):
    """현재 방향 facing에서 '왼쪽(LEFT)'을 바라보려면 시계방향으로 몇 번 회전?"""
    return (LEFT - facing) % 4

def right(facing):
    """현재 방향 facing에서 '오른쪽(RIGHT)'을 바라보려면 시계방향으로 몇 번 회전?"""
    return (RIGHT - facing) % 4

def top(facing):
    """현재 방향 facing에서 '위(UP)'를 바라보려면 시계방향으로 몇 번 회전?"""
    return (UP - facing) % 4

def bottom(facing):
    """현재 방향 facing에서 '아래(DOWN)'를 바라보려면 시계방향으로 몇 번 회전?"""
    return (DOWN - facing) % 4


# 입력
N = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(N)]

# 사과 위치 수집 (라벨 1..K)
pos = {}
K = 0
for r in range(N):
    for c in range(N):
        v = grid[r][c]
        if v > 0:
            pos[v] = (r, c)
            if v > K:
                K = v

# 방문 순서: 시작 (0,0) -> 1 -> 2 -> ... -> K
route = [(0, 0)] + [pos[i] for i in range(1, K + 1)]

# 시작 방향: 오른쪽
facing = RIGHT
total_rot = 0

for i in range(len(route) - 1):
    (r1, c1) = route[i]
    (r2, c2) = route[i + 1]
    dr = r2 - r1  # +면 아래(DOWN), -면 위(UP)
    dc = c2 - c1  # +면 오른쪽(RIGHT), -면 왼쪽(LEFT)

    # 각 축으로 '바라봐야 할' 방향이 있다면, 현재 바라보는 방향에서 그 방향까지 필요한 회전 수 계산
    rot_x = 0
    dir_x = None
    if dc > 0:
        rot_x = right(facing)
        dir_x = RIGHT
    elif dc < 0:
        rot_x = left(facing)
        dir_x = LEFT

    rot_y = 0
    dir_y = None
    if dr > 0:
        rot_y = bottom(facing)
        dir_y = DOWN
    elif dr < 0:
        rot_y = top(facing)
        dir_y = UP

    # 구간 회전 수 = x, y 중 더 큰 회전 수
    seg_rot = rot_x if rot_x >= rot_y else rot_y
    total_rot += seg_rot

    # 다음 구간을 위해 '실제로 마지막에 바라보게 되는' 방향을 갱신
    # - 큰 회전 수 쪽 방향으로 바라보는 것으로 업데이트
    # - 동률이면, x축 방향이 있었다면 그쪽을, 아니면 y축 방향으로
    if rot_x > rot_y and dir_x is not None:
        facing = dir_x
    elif rot_y > rot_x and dir_y is not None:
        facing = dir_y
    else:
        # rot_x == rot_y 인 경우
        if dir_x is not None:
            facing = dir_x
        elif dir_y is not None:
            facing = dir_y
        # 둘 다 None이면(제자리) facing 유지

print(total_rot)
