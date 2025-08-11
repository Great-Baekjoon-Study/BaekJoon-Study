document = input()
word = input()

d = len(document) # document 길이
w = len(word) # word 길이
i = 0 # 인덱스
cnt = 0 # 단어가 최대 몇 번 중복되지 않게 등장하는지 세기

while i < d:
    if document[i:i+w] == word:
        cnt += 1
        i += w
    else:
        i += 1

print(cnt)
