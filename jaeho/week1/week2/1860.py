"""

그는 무조건 예약제로만 손님을 받으며, 

그래서 오늘은 N명의 사람이 자격을 얻었다.

진기는 0초부터 붕어빵을 만들기 시작하며, 

M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.

서빙은 진기가 하는 것이 아니기 때문에, 붕어빵이 완성되면 어떤 시간 지연도 없이 다음 붕어빵 만들기를 시작할 수 있다.

0초 이후에 손님들이 언제 도착하는지 주어지면, 

모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 세 자연수 N, M, K(1 ≤ N, M, K ≤ 100)가 공백으로 구분되어 주어진다.

두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며,

각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타낸다. 각 수는 0이상 11,111이하이다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면 “Possible”을, 아니라면 “Impossible”을 출력한다.

"""

import sys

sys.stdin = open("input (6).txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # N = 손님 수
    # M = 붕어빵 만드는 시간
    # K = 만들어지는 붕어빵 수
    son_time = list(map(int, input().split()))
    # 첫 손이 오는 시간보다 붕어빵 만드는 시간이 짧으면 불가
    
    # 첫 손님이 언제오는지, 마지막손님이 언제오는지 확인을 위한 정렬
    son_time.sort()

    # 마지막 손
    last_son = son_time[-1]

    # 마지막 손님 올때까지 몇번 붕어빵을 뺄수 있는가?
    boong_count = last_son // M
    if boong_count < 1:
        boong_count = 1

    boong_stack = 0

    pass_and_fail = True

    # 붕어빵 1회 돌릴때 마다 K개 쌓인다
    for t in range(1,boong_count+1) :
        boong_stack += K
        for p in son_time:
            if M > p :
                pass_and_fail = False
                break
                # 만약에 첫 손 오는 시간보다 첫 붕어빵 나오는 시간이 늦으면 실패
            elif M * t <= p < M * (t+1) and boong_stack >=1:
                boong_stack -= 1
                # 첫 손 오는 시간에 맞춰 붕어빵이 나왓을때 손님 한명 빠질때 마다 -1
            elif M * t <= p < M * (t+1) and boong_stack < 1:
                pass_and_fail = False
                break
            elif M * (t+1) < p :
                break
                # 두번째, 세번째 붕어빵 나오기 전까지 손님이 붕어빵을 다 사가면 fail
            else:
                pass
        
    if pass_and_fail:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
        


    

