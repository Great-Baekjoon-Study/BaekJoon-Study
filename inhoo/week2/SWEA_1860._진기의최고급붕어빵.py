#이런 붕어빵 나도 먹어보고 싶당
#N명의 사람이 자격을 얻음
#0초~ 붕어빵 만들기 시작
#M초 에 K개의 붕어빵
#0초 이후에 손님들이 언제 도착하는지 알고,
#모든 손님들에게 기다리는 시간없이 붕어빵 제공가능한지 판별!!하기
#한 손님이라도 못 받으면 Impossible 출력
#도착하는 시간 - M*K = 붕어빵 만들기 시작    _이러면 되지 않을까?
T = int(input())


def baking():
#1손님당 1개
    N, M, K = map(int, input().split()) #N명의 사람
    arrive_time_list = list(map(int, input().split())) #N개의 정수, 초단위, 0~11,111
    arrive_time_list.sort()

    for i in range(N):
        num_baking =arrive_time_list[i] // M #손님당 M초에 K개를 만드는 동작 1번, 누적
        if num_baking > 0: #무조건 동작한다.
            if num_baking *K < i+1: #붕어빵 총 개수가 i+1(총사람수)보다 작으면
                ###i+1은 사람 수가 아니다. arrive list가 정렬되어 있지 않으므로
                
                return 'Impossible' #N,M,K가 1보다 크기 때문에 num_baking <=0일 수가 없음. 무조건 크다.
        else:
            return 'Impossible'


    return 'Possible' #for문을 돌려 전체 리스트의 요소를 확인하기

for tc in range(1, T+1):
    print(f'#{tc} {baking()}')
