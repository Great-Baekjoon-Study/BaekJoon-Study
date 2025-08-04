# def bubble_sort(a, N):
#     for i in range(N-1, 0, -1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]


# def bubble_sort2(N, K, a):
#     sort_cnt = 0
#     for i in range(N-1, 0, -1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 sort_cnt += 1
#                 if sort_cnt == K:
#                     return a[j+1], a[j]
#                 else:
#                     a[j], a[j+1] = a[j+1], a[j]
#     else:
#         return -1
    
# print(bubble_sort2(6, 10, [4, 6, 5, 1, 3, 2]))
# print(bubble_sort2(6, 12, [4, 6, 5, 1, 3, 2]))

N, K = map(int, input().split())
A = list(map(int, input().split()))

sort_cnt = 0
for i in range(N-1, 0, -1):
    for j in range(i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            sort_cnt += 1
            if sort_cnt == K:
                print(f'{A[j]} {A[j+1]}')
                exit()

if sort_cnt < K:
    print(-1)