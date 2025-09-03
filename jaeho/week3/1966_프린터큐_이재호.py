"""
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

예를 들어 Queue에 4개의 문서(A B C D)가 있고, 
중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
"""
"""
4 2
# 4장이 있고 그중에 인덱스 2번 문서가 몇번째로 인쇄되는지
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3 = 4 출력
1 2 3
2 3 1
3 1 2 = 3 출력
1 2
2 1 = 2 출력
1 = 1 출력

6 0
# 6장이 있고 그중에 0번 문서가 몇번째로 인쇄되는지
1 1 9 1 1 1
1 2 3 4 5 6 

9 1 1 1 1 1 = 9 출력
6 1 2 3 4 5

1 1 1 1 1 = 1 출력
"""

from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    q = deque()
    # 큐 설정
    for i in range(len(arr)):
        tu = (arr[i], i)
        # 값과 인덱스를 튜플로 묶어서 큐에 추가 
        q.append(tu)

    print_count = 0

    while q:
        # 큐에 값이 남아있을때 까지 반복          
        current_doc = q.popleft()
        # 큐에서 값을 하나 꺼내서
        current_value = current_doc[0]
        # 튜플 인덱스 0은 값
        current_index = current_doc[1]
        # 튜플 인덱스 1은 인덱스

        for tu in q:
            # 튜플을 반복 돌면서
            if current_value < tu[0]:
                # 제일 앞에 있는 문서보다 밸류가 높은 문서가 있는지 확인
                value = True
                # 있으면 밸류를 참으로 바꾸고 멈춤
                break


        if value:
            q.append(current_doc)
            # 밸류가 참이면(제일 앞에 있는 문서보다 밸류가 높은 문서가 있으면)
            # 제일 앞에 문서를 제일 뒤로 보냄
        else:
            print_count += 1
            # 그게 아니면(뒤에 밸류가 높은 문서가 없으면)
            # 프린트 카운트 하나 올리고
            if current_index == M:
                # 만약에 찾고있는 문서가 출력될 차례면
                print(print_count)
                # 정답출력
                break