from collections import deque

T = int(input())  
for _ in range(T):
    n, m = map(int, input().split())   # 문서 개수 n, 찾고 싶은 문서 위치 m
    arr = list(map(int, input().split()))


    q = deque()
    for i in range(n):
        q.append((i, arr[i])) # (문서번호, 중요도) 큐에 넣기

    cnt = 0  # 출력 순서 카운트

    while True:
        now = q.popleft()   # 맨 앞 문서 꺼내기
        
        # 현재 문서보다 더 큰 중요도가 있는지 확인
        check = False
        for x in q:
            if x[1] > now[1]:
                check = True
                break


        if check:   # 더 큰 게 있으면 뒤로 보내기
            q.append(now)
        else:       # 더 큰 게 없으면
            cnt += 1
            if now[0] == m:  # 찾던 문서라면 끝내기
                print(cnt)
                break
