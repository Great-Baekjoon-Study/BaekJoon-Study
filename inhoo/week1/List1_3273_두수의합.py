# a+b =x 만족하는 (a, b) 쌍 구하기

n = int(input())
p = list(map(int, input().split()))
x = int(input())

#x-p[i] 한 게 p 안에 있으면 한쌍

p_set = set(p)
ans_cnt = 0 #쌍 개수

for num in p_set:
    if x-num in p_set:
        ans_cnt +=1
        
print(int(ans_cnt/2)) #쌍 중복으로 2개 나올 거니까
#'/2' 말고 조건문으로 걸러낼 수 있는 방법은 없을까?

#리스트에서보다 집합에서 탐색시간이 더 줄어듦.
# 백준 실버 = 알고리즘 기본기를 시험하는 구간.
# 보통 O(n²) → 시간 초과, O(n log n) 또는 O(n)으로 줄여야 통과.
# 파이썬에서는 특히 in list 반복은 주의.

# **리스트(list)**에서 if something in p: → O(n) 시간
# → 리스트 전체를 순회해서 비교해야 함.
# **집합(set)**에서 if something in p_set: → O(1) 평균 시간

##원래코드
# i=0
# ans_cnt = 0 #쌍 개수

# for i in range(n):
#     if x-p[i] in p:
#         ans_cnt +=1
        
# print(int(ans_cnt/2))
        