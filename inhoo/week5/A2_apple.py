# 방향: 0=오른쪽(right), 1=아래, 2=왼쪽, 3=위
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def turn_count(start_dir, dx, dy):
    """
    시작 방향에서 목표까지 갈 때
    오른쪽 회전 몇 번 필요한지 단순 계산
    """
    count = 0 #회전 세는 변수
    cur_dir = start_dir # 지금 바라보는 방향, 오른쪽으로 시작

    # 먼저 가야 하는 방향 리스트(예: 오른쪽 → 아래)
    moves = []
    if dy > 0: moves.append(0)   # 오른쪽으로 가야하면 '오른쪽(회전수0)' 추가
    if dx > 0: moves.append(1)   # 아래
    if dy < 0: moves.append(2)   # 왼쪽
    if dx < 0: moves.append(3)   # 위쪽

    # 필요한 각 방향으로 가려면 몇 번 돌려야 하는지
    for d in moves:
        while cur_dir != d:      # 현재 방향이 목표 방향 될 때까지
            cur_dir = (cur_dir + 1) % 4 #0,1,2,3으로 순환
            count += 1           # 회전 1번
        # 방향 맞추면 그냥 직진 → 회전 아니므로 count 증가없음.

    return count, cur_dir        # 총 회전 수, 마지막 방향 리턴

def solve(grid):   # 격자 지도 전체
    N = len(grid)
    
    # 사과 위치 모으기
    apples = [(0,0)]
    for num in range(1, N*N+1):
        for i in range(N):
            for j in range(N):
                if grid[i][j] == num:
                    apples.append((i,j)) #출발 ~ 1번사과, 2번,,순서 저장
    
    
    # (0,0)부터 순서대로 이동
    total_turns = 0
    cur_dir = 0  # 시작 방향: 동쪽
    for k in range(len(apples)-1):
        x1,y1 = apples[k]
        x2,y2 = apples[k+1]
        dx, dy = x2-x1, y2-y1
        turns, cur_dir = turn_count(cur_dir, dx, dy)
        total_turns += turns
    return total_turns
