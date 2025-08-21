# N = int(input())
# # 숫자 개수

# arr = [int(input()) for _ in range(N)]
# # 정렬할 숫자 받아오기

# max_val = 0
# for num in arr:
#     if num > max_val:
#         max_val = num
# # 최댓값 구하기

# matrix = [0] * (max_val + 1) 
# # 최댓값 만큼의 배열 생성. 0 ~ 최댓값까지

# for n in arr:
#     matrix[n] += 1
# # 배열에 숫자의 값을 인덱스로 하여 카운트

# sort_lst=[]
# # 정렬할 빈 배열 생성

# for i in range(max_val+1):
#     # 최댓값 +1 만큼 반복
#     for _ in range(matrix[i]):
#         # 카운트 된 횟수 = 정렬할 숫자 n의 개수 
#         sort_lst.append(i)
#         # ex) max_val = 7이면
#         # 0, 1, 2, 3, 4, 5, 6, 7 반복
#         # matrix[0] = 0이 있는 숫자만큼  반복
#         # 0을 0이 있는 숫자만큼 반복해서 빈 배열에 추가

# for num in sort_lst:
#     print(num)

# # 위 코드는 아무리해도 메모리 초과가 뜬다.
# # ai한테 물어봣더니 배열을 받아와서 리스트로 만들면 메모리 초과랜다
# # input이 아니라 import sys.stadin.readline() 으로 받아와서 풀어야 한다.
# ##-----------------------------------------------------
import sys

N = int(sys.stdin.readline())
# 숫자 개수

matrix = [0] * (10001) 
# 최댓값 만큼의 배열 생성. 0 ~ 10001 문제에서 정한 최댓값까지
for _ in range(N):
    num = int(sys.stdin.readline())
    matrix[num] += 1
# 바로 받아와서 매트릭스에서 카운트

for i in range(1, 10001):
    if matrix[i] != 0:
        for _ in range(matrix[i]):
            print(i)
# 정렬해야하는 숫자가 0이 아닐때마다 작동하여 시간을 줄임

