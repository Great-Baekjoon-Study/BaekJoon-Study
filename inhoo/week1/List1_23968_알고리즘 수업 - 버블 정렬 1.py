count = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    for j in range(0,i):   
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            count+=1

            if count == K:

                if A[j]< A[j+1]:
                    print(A[j],A[j+1])
                    exit()
                                         
if count < K:
    print(-1)