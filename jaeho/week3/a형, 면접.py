# 어차피 최솟값을 얻기 위해서는 최대한 앞에서 몰아서 점수를 얻고
# 두배카운터를 초반에 가져가는것이 중요함
"""
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N = 문제 개수, M = 맞힌 개수, K = 보너스 달성 카운트
    count = 0
    # 보너스 카운트
    i = 0
    # 문제진행상황
    score = 0
    # 스코어
    fail_count = N - M
    # 틀린 개수
    if K >= 1 and fail_count * (K-1) >= M :
        score = M
    else:
        while i < N:
            count += 1
            # 한문제 맞춤
            score += 1
            # 1점 오름
            i += 1
            # 문제진행상황 최신화
            remain = N - i
            # 남는문제 최신화
            if count == K:
            # 만약에 연속으로 맞춘 카운터가 K가 되면
                count = 0
                # 카운트를 0으로 초기화하고
                score = score * 2
                # 점수를 두배로 올린다
            elif remain <= K * fail_count:
                # 만약에 남은 문제수보다 틀린 개수 * 보너스 충족을 위한 연속정답수가 크거나 같으면
                # 한번도 보너스 점수를 얻지 못함 
                score += (K-1) * (remain//K) + (remain % K)
                # (K-1) << 보너스를 받기전까지 연속 맞춘다는 가정하에 K-1개 맞으면 틀린다
                # 남은 문제수 / K를 하면 몇번이나 사이클이 돌 수 있는지 파악가능 하기에 1 사이클 마다 K-1점 추가
                break
    print (f'#{tc} {score}')
"""

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N = 문제 개수, M = 맞힌 개수, K = 보너스 달성 카운트
    count = 0
    # 보너스 카운트
    i = 0
    # 문제진행상황
    score = 0
    # 스코어
    fail_count = N - M
    # 틀린 개수
    if K >= 1 and fail_count * (K-1) >= M :
        score = M
    else:
    # --- 여기부터 else 블록의 올바른 로직 ---
    # 1. 오답으로 보호받는 '안전 점수'
        safe_score = fail_count * (K - 1)
        
        # 2. 보호받지 못하고 보너스를 계산해야 하는 정답 개수
        remaining_answers = M - safe_score
        
        # 3. 나머지 정답들을 연속으로 맞힐 때의 '보너스 점수' 계산
        bonus_score = 0
        count = 0
        for _ in range(remaining_answers):
            bonus_score += 1
            count += 1
            if count == K:
                bonus_score *= 2
                count = 0
                
        # 4. 최종 점수는 두 점수의 합
        score = safe_score + bonus_score
    
print(f'#{tc} {score}')




    
