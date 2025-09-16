def dfs(balloon):
    # 풍선이 하나 남았으면 자기 자신 점수
    # 종료 조건
    if len(balloon) == 1:
        return balloon[0]

    best = 0  # 현재 상태에서 얻을 수 있는 최대 점수를 저장할 변수
    for i in range(len(balloon)):
        # 현재 단계에서 i번째 풍선을 터뜨리는 경우를 시도
        
        # 1. 점수 계산
        if i == 0:  # 맨 왼쪽 풍선을 터뜨릴 때
            score = balloon[i+1] # 오른쪽 풍선의 점수만 얻음
        elif i == len(balloon) - 1:  # 맨 오른쪽 풍선을 터뜨릴 때
            score = balloon[i-1] # 왼쪽 풍선의 점수만 얻음
        else:  # 중간에 있는 풍선을 터뜨릴 때
            score = balloon[i-1] * balloon[i+1] # 양옆 풍선 점수의 곱을 얻음

        # 2. 풍선 하나 제거 (다음 상태 생성)
        # i번째 풍선을 제외한 새로운 리스트를 만듦
        new_balloons = balloon[:i] + balloon[i+1:]

        # 3. 재귀 호출 및 최대값 갱신
        # "이번에 얻은 점수" + "남은 풍선들로 얻을 수 있는 최대 점수"
        # 위 값을 기존의 best 값과 비교하여 더 큰 값으로 갱신
        best = max(best, score + dfs(new_balloons))

    return best # 모든 경우를 시도해본 후 찾은 최대 점수를 반환