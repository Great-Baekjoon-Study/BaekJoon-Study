# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수 구하기

n = int(input()) # 수열의 크기
a = list(map(int, input().split())) # n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
x = int(input()) # ai + aj = x 
cnt = 0 # 주어진 조건을 만족하는 쌍의 수 초기 설정값
for i in range(len(a)): # 수열 a 반복
    for j in range(i + 1, len(a)): # i번째 다음 수부터 끝까지 반복
        if a[i] + a[j] == x: # i번째 원소와 j번째 원소의 합이 x일 경우
            cnt += 1 # 주어진 조건을 만족하기 때문에 쌍의 수 1 증가

print(cnt)

# 이중 반복문 돌려서 시간 복잡도 O(n^2) 돼서 시간 초과
# ----------------------------------------------------------------------------------------------

n = int(input()) # 수열의 크기
a = list(map(int, input().split())) # n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
x = int(input()) # ai + aj = x 
cnt = 0 # 주어진 조건을 만족하는 쌍의 수 초기 설정값
for num in a: # 수열 a 반복
    if (x - num) in a: # x-num이 a에 있을 경우
        cnt += 1 # 주어진 조건을 만족하는 거기 때문에 cnt 1 증가
print(cnt // 2) # 예를 들어 (1, 9), (9, 1) 이런 식으로 두 번 세기 때문에 2 나누기

# for문 한 번만 써서 시간 복잡도 O(n)이라고 생각했는데
# in 연산자로 a 리스트에서 값을 찾는 건 O(n)이기 때문에
# 결국 얘도 시간 복잡도 O(n^2)
# ----------------------------------------------------------------------------------------------

n = int(input()) # 수열의 크기
a = list(map(int, input().split())) # n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
x = int(input()) # ai + aj = x 
checked = set() # 지금까지 등장한 숫자를 저장할 집합
cnt = 0 # 주어진 조건을 만족하는 쌍의 수 초기 설정값
for num in a:
    if (x - num) in checked: # 이전에 등장한 수 중에 x-num이 있다면
        cnt += 1 # (x-num, num) 쌍이 존재하므로 cnt 증가
    checked.add(num) # 현재 숫자를 집합에 추가
print(cnt) #(ai, aj)와 (aj, ai)를 한 번만 세는 방식이라서 cnt // 2 할 필요 없음

# set은 in 연산이 평균 O(1)이라서 빠르게 동작함.
# for문 한 번만 쓰고, set의 in 연산 사용했기 때문에 시간 복잡도 O(n)

