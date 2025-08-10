#카운팅 정렬 구하기

N = int(input())
arr = [int(input()) for _ in range(N)] #리스트 만들어짐

for _ in range(N):
    x = int(input())

#가장 큰 수 찾기
max_v = 0
for i in arr:
    if i > max_v:
        max_v = i

#counts[] 배열 만들기
counts = [0] * (max_v +1)
#그리고 숫자들 개수 세기
for num in arr:
    counts[num] +=1

# 값들 쌓아놓기, 인덱스 쌓기
for num in range(max_v+1): # 0~ 최댓값
    for _ in range(counts[num]): #counts배열에 있는 num의 숫자 개수만큼 뽑아내기
        print(num)



#<이전 코드>
#수업에서 배운 카운팅 정렬 그대로 씀, 메모리 초과됨
#'정렬된 결과'를 굳이 새 리스트에 작성하지 말고 바로 출력
# 인덱스 누적합도 없앰
#그러면 메모리 줄여짐
# temp = [0] * N
# for p in range(N-1, -1, -1): # N-1 ~0
#     x = arr[p]
#     counts[x] -=1 # 다음숫자 인덱스이므로
#     temp[counts[x]] = x

# for q in temp:
#     print(q)


