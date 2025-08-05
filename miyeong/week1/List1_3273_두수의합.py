# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
# 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수 구하기

n = int(input()) # 수열의 크기
a = list(map(int, input().split())) # n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
x = int(input()) # ai + aj = x 

# cnt = 0 # 주어진 조건을 만족하는 쌍의 수 초기 설정값
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] + a[j] == x:
#             cnt += 1

# print(cnt)

cnt = 0
for num in a:
    if (x - num) in a:
        cnt += 1
print(cnt // 2)
