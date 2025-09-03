T = int(input())  # 테스트 케이스 수 입력
for test_case in range(1, T + 1):
    N = int(input())  # 나무의 개수 입력

    tree = list(map(int, input().split()))  # 각 나무의 초기 높이를 리스트로 입력

    max_h = max(tree)  # 현재 가장 큰 나무 높이 계산
    diff = [max_h - h for h in tree]  # 각 나무가 최대 높이까지 자라야 하는 차이 계산

    odd = []   # 홀수 차이를 가진 나무 리스트
    even = []  # 짝수 차이를 가진 나무 리스트

    for d in diff:  # 각 나무의 차이를 확인
        if d == 0:  # 이미 최대 높이면 건너뜀
            continue
        elif d % 2 == 1:  # 차이가 홀수면
            odd.append(d)
        else:  # 차이가 짝수면
            even.append(d)

    odd_day = len(odd)  # 홀수 차이를 가진 나무가 남은 횟수 = 홀수 날 필요한 수

    even_day = 0  # 짝수 날 필요한 수 초기화

    for o in odd:  # 홀수 차이도 2씩 쪼개어 짝수 날로 처리 가능
        even_day += o // 2

    for e in even:  # 짝수 차이 나무도 2씩 증가하므로 짝수 날 필요 횟수 계산
        even_day += e // 2

    cnt = 0  # 총 날짜 카운트
    while odd_day or even_day:  # 홀수 날 또는 짝수 날이 남아있으면 반복
        cnt += 1  # 날짜 증가
        if cnt % 2 == 1:  # 홀수 날
            if odd_day != 0:  # 홀수 날 필요 횟수가 있으면
                odd_day -= 1  # 1씩 줄임
            if odd_day == 0 and even_day > 2:  # 홀수 날인데 홀수 날 필요 없고, 짝수 날이 2 이상 남으면
                odd_day += 2  # 짝수 날 2를 쪼개서 홀수 날에 처리
                even_day -= 1  # 짝수 날에서 1 감소
        else:  # 짝수 날
            if even_day != 0:  # 짝수 날 필요 횟수가 남아있으면
                even_day -= 1  # 1씩 줄임

    print(f"#{test_case} {cnt}")  # 각 테스트 케이스 결과 출력


'''
1 자라고, 2 자라는 거 더하면 이틀 동안 3 자람. 그러니까 +3씩 시키고 남은 거 1 더하든 2 더하든
어차피 하루에 한 나무만 물을 줄 수 있으니까 각자 따로 구한 다음에 다 더하면 안 되나?
근데 첫번째 나무 물 안 주는 날에 두 번째 나무에 물 줄 수도 있으니까 따로 구하면 최소 날짜 수가 안 나옴.
=> 잘못된 방법
'''