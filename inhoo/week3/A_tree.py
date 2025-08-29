'''
2<=N<=100 , 초기 높이: 1~120
물을 주는 짝수날이 많아야 한다.
그래야 최소날짜 됨.
'''

def water_day(arr):
    differ_h = []
    even_day = 0  # 무조건 짝수날에 물을 줘야하는 날은 없다. 홀수로 분리 가능
    odd_day = 0  # 무조건 홀수날에 물을 줘야하는 날
    total_day = 0
    water_0 = 0

    max_h = max(arr) #높이들의 최댓값 구함

    for tree in arr:
        water_0 += max_h-tree
        differ_h.append(max_h-tree) # 최댓값 높이와 차이 구함, 물 줘야하는 양 구하기

    if water_0 == 0: #물 줘야할 날 없으면 0 리턴
        return 0

    for i in differ_h: #i는 높이 차 하나
        if i % 2 ==1:
            odd_day += 1

        even_day += (i // 2)  #최대한 짝수날에 물 주도록 하기

    if odd_day > even_day: #무조건 홀수에 물 주는 날이 많다면
        #짝수날까지 홀수,짝수날 모두 주고 + 나머지 홀수날 구하기
        total_day = even_day*2 + (odd_day-even_day-1)*2 +1
        return total_day

    else: #even=odd이면 even_day*2,이고
        #짝수날이 더 많으면 홀수 날에 들어갈 수 있음.
        total_day += odd_day * 2 #홀수,짝수날 모두 주고
        #남은 짝수날들 계산
        a = (even_day - odd_day) *2 #남은 짝수날의 총 물 줘야하는 횟수
        total_day += 2 * (a//3) # (홀수날,짝수날) 묶으면 2일에 키 3 자라게 함.

        if a % 3 == 1:
            total_day += 1
        elif a % 3 == 2:
            total_day += 2
        return total_day

T = int(input())


for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))  # 나무들의 높이
    result = water_day(arr)
    print(f'#{tc} {result}')













#처음 시험 때 풀었던 바보같은 코드
'''
#N개의 나무가 있다.
# 하루에 한 나무만 물 주기
# 첫 날은 물을 준 나무의 키가 1 자라고,
#홀수 날은 나무의 키+1
#짝수 날은 나무의 키 +2

#모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 *최소 날짜 수


#**어떤 날에는 물을 주는 것을 하지 않을 수도 있따.

#최대한 짝수날에 물을 주고, 홀수날에 배정하기, 마지막날에 일 안하는 날 몰아넣기


T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 나무의 개수
    arr = list(map(int, input().split()))   #나무의 높이


    max_h = max(arr)
    total_h = 0
    cnt_date = 0
    for i in arr:  #높이차 합구하기
        total_h += max_h -i

    if total_h == 0:
        cnt_date = 0

    else:
        num_3 = total_h //3
        cnt_date += 2* num_3

        if total_h % 3 == 1:
            cnt_date += 1
        elif total_h % 3 == 2:
            cnt_date += 2

    print(f'#{tc} {cnt_date}')
'''




