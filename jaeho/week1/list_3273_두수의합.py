"""
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고,
1000000보다 작거나 같은 자연수이다.
자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

"""
"""
------1차시도------
N = int(input())
arr = list(map(int, input().split()))
x = int(input())
# N = 수열의 크기
# arr = 수열
# x = 합계가 만족해야하는 값

def solve() :
    i = 0
    #인덱스 반복 돌리기위한 i값 0
    counts = 0
    # 1쌍 찾을때 마다 카운트 +1
    while i < N :
        for num in arr :
            # 수열 arr을 num으로 반복돌림
            if num == arr[i]:
                pass
            # num == arr[i]이면 같은 값끼리 더하는 상황임 (n개의 서로 다른 양의정수로 이루어진 수열이므로) 따라서 pass
            elif arr[i] + num == x:
                counts += 1
        i += 1
    return counts//2
    # 중복값 제거를 위한 / 2
--- 시간복잡도 ㅁ랃ㅈ고ㅓㅎㄷㄱㅈ ---
"""

N = int(input())
arr = list(map(int, input().split()))
x = int(input())

def solve(N, arr, x):
    arr.sort()
    # 받아온 수열을 오름차순으로 정렬

    count = 0
    # 합 x 나올때마다 카운트 +1
    left = 0
    right = N - 1
    # 왼쪽과 오른쪽 설정하여 한개씩 땡겨오면서 반복할거라 왼쪽을 0, 오른쪽을 n-1로 설정

    while left < right:
        # 왼쪽 오른쪽 조건에 미달할때마다 한쪽씩 땡겨가면서 반복할거고 결국은 중앙에서 만남. 만나면 조건문 끝

        current_sum = arr[left] + arr[right]
        # 왼쪽 오른쪽 더한 값

        if current_sum == x:
            count += 1
            left += 1
            right -= 1
            # 왼쪽, 오른쪽 양 끝값을 더한 값이 x면 카운트 1을 올리고 양쪽 인덱스를 땡긴다.
        elif current_sum < x:
            left += 1
            # 왼쪽, 오른쪽 양 끝값을 더한 값이 x보다 작으면 왼쪽을 땡겨서 더 큰 값을 만든다
        else:  # current_sum > x
            right -= 1
            # 왼쪽, 오른쪽 양 끝값을 더한 값이 x보다 크으면 오른쪽을 땡겨서 작은 값을 만든다

    return count

result = solve(N, arr, x)
        # 안넣으면 런타임에러뜸
print(result)




