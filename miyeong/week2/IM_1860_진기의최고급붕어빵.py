# N명의 사람이 자격을 얻음.
# 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있음.
# 0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별
# 제공 가능하면 "Possible", 아니면 "Impossible" 출력

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # N명의 사람에게 M초의 시간을 들여 K개의 붕어빵 만들기
    customer = list(map(int, input().split())) # 손님들이 언제 도착하는지 주어짐.

    customer.sort() # 오는 순서 정렬

    possible = True
    for i in range(N):
        # i번째 손님이 도착한 시간
        time = customer[i]

        # time초까지 만든 붕어빵 개수
        bread = (time // M) * K

        # 지금까지 온 손님 수 (i+1명)
        # 지금까지 온 손님 수보다 만들어진 붕어빵 개수가 작으면 제공 불가능
        if bread < i+1:
            possible = False
            break
    
    if possible:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')


