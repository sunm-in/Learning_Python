# 📌코딩 테스트에서 자주 사용되는 라이브러리
data = [7, 2, 5, 4, 1]

print(sum(data)) # 19
print(min(data)) # 1
print(max(data)) # 7
print(sorted(data)) # [1, 2, 4, 5, 7]

# 📌itertools 모듈에서는 다양한 경우의 수 관련 함수를 제공
from itertools import permutations, combinations, product, combinations_with_replacement

# 순열
arr = ['A', 'B', 'C']
result = list(permutations(arr, 2))
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 조합
result = list(combinations(arr, 2))
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열
result = list(product(arr, repeat=2))
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 중복 조합
result = list(combinations_with_replacement(arr, 2))
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# 📌우선순위 큐(priority queue)의 목적으로 힙(heap)을 사용할 수 있다.
# 파이썬에서는 heapq 라이브러리 제공, 최소 힙(min heap)을 따른다.
# 힙에 원소를 삽입 또는 삭제할 때 O(logN)의 시간 복잡도를 요구한다.
# 단순히 힙에 모든 원소를 넣었다가 빼는 것만으로도 O(NlogN)의 시간 복잡도를 보장하며 오름차순 정렬을 수행할 수 있다.
import heapq

arr = [5, 2, 9, 8, 7, 3, 4, 1, 6]
heap = []
result = []

for x in arr:
    heapq.heappush(heap, x)
    
for i in range(len(heap)):
    x = heapq.heappop(heap)
    result.append(x)
    
print(result) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 📌코딩 테스트에서의 입출력
# 첫째 줄에는 학생의 수가 100 이하의 자연수
# 둘째 줄에는 각 학생의 점수가 100 이하의 양의 정수로 공백을 기준으로 구분되어 주어짐
# 5
# 35 92 89 54 22
n = int(input())
arr = list(map(int, input().split()))
print(n) # 5
print(arr) # [35, 92, 89, 54, 22]

# 📌sys
# 입력 문자열이 다수의 라인으로 구성되는 경우 -> 입력이 너무 많아서, 입력 과정에서 시간 초과 발생할 수 있음
# sys 모듈에 포함된 readline을 input 대신에 사용하여 빠르게 입력받을 수 있다.
# 이때, readline은 개행문자 "\n"까지 읽어 들이므로, rstrip() 함수를 이용해 개행 문자를 제거할 수 있다.
import sys
input = sys.stdin.readline

data = input().rstrip()
print(data)

# 📌f-string을 사용하면 원하는 형태에 맞게 간단히 문자열을 출력할 수 있다.
score = 70
print(f"학생의 점수는 {score}점 입니다.")