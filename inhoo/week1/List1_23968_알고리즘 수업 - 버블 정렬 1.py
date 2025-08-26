N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0

def bubble_sort():
    global count
    for i in range(N-1, 0, -1):
        for j in range(0,i):   
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                count+=1

                if count == K:
                    return f'{A[j]} {A[j+1]}'
                    
                                         
    if count < K:
        return -1


print(bubble_sort())

#함수 안에서 변수를 읽기만 할 때는 global 안 써도 됨
#다만 변수에 값을 대입할 때는 그 변수를 local 취급함.
#return print() 하면 print()의 반환값 None이 반환된다.