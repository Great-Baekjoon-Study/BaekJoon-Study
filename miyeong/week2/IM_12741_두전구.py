# 두 개의 전구 X와 Y가 있음. 0초에서부터 시작하여 100초간 두 전구가 언제 켜지는지 관찰
# 전구 X는 A초에서부터 B초까지에만 켜져 있음.
# 전구 Y는 C초에서부터 D초까지에만 켜져 있음.
# 100초 중 두 전구가 동시에 켜져 있던 시간은 몇 초?

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    A, B, C, D = map(int, input().split())

    bulb = [0] * (max(A,B,C,D) + 1) # 전구 리스트

    # 전구가 켜져 있으면 +1
    # 두 개가 동시에 켜져 있으면 2일 거임.

    # 전구 X가 켜져 있는 거 표시
    for i in range(A, B+1):
        bulb[i] += 1

    # 전구 Y가 켜져 있는 거 표시
    for i in range(C, D+1):
        bulb[i] += 1

    # 두 전구가 동시에 켜져 있는 초를 담은 리스트
    on = []

    # 전구 다 돌아보면서 2인 초를 on에 추가
    for i in range(len(bulb)):
        if bulb[i] == 2:
            on.append(i)

    # on이 비어있지 않으면 최대값 - 최소값이 두 전구가 동시에 켜져 있던 시간
    # 비어있으면 동시에 켜져 있는 시간이 없는 거
    if on:
        print(f'#{test_case} {max(on) - min(on)}')
    else:
        print(f'#{test_case} 0')

