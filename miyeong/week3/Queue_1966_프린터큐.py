# 현재 Queue의 가장 앞에 있는 문서의 '중요도' 확인
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 함.
# 그렇지 않다면 바로 인쇄
# Queue에 4개의 문서(A, B, C, D)가 있고, 중요도가 2 1 4 3 라면 C -> D -> A -> B
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내기
# 중요도가 같은 문서가 여러 개 있을 수 있음.

from collections import deque

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    # N : 문서의 개수, M : 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지
    N, M = map(int, input().split())
    importants = list(map(int, input().split())) # N개 문서의 중요도

    q = deque() # 현재 Queue에서 몇 번째에 놓여있는지와 중요도를 함꼐 담은 큐

    for idx, important in enumerate(importants):
        q.append((idx, important)) # 현재 위치, 중요도

    cnt = 0 # 인쇄 횟수

    while q:
        idx, important = q.popleft() # 맨 앞에 원소 꺼내기

        # 현재 문서에서 가장 높은 중요도
        max_important = 0
        for i in range(len(q)):
            if q[i][1] > max_important:
                max_important = q[i][1]

        # 현재 문서의 중요도가 최대값보다 작은 경우 -> 뒤로 보내기
        if important < max_important:
            q.append((idx, important))
        else: # 인쇄
            cnt += 1
            if idx == M: # 내가 궁금한 문서랑 꺼내는 원소가 같을 경우
                print(cnt)
                break