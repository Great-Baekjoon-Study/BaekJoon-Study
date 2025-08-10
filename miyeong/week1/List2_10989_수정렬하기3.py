N = int(input()) # 수의 개수
num_lst = []
for i in range(N):
    num = int(input()) # N개의 줄에 수가 주어짐.
    num_lst.append(num)

count = [0] * (max(num_lst)+1)

for n in num_lst:
    count[n] += 1

for i in range(1, len(count)):
    count[i] = count[i-1] + count[i]

temp = [0] * len(num_lst)
for i in range(len(num_lst)-1, -1, -1):
    count[num_lst[i]] -= 1
    temp[count[num_lst[i]]] += num_lst[i]

print(temp)