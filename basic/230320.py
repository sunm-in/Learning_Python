# 📌변수, 상수
a = 12
b = 5
print(a + b) # 17
a = 19
print(a + b) # 24
# print(c) NameError: name 'c' is not defined

# 📌사칙연산
num1 = 31
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

# 📌문자열
str1 = 'hello'
str2 = 'python'
print(str1 + ', ' + str2) # hello, python
print("\"안녕\"하세요. \"반갑\"습니다.") # "안녕"하세요. "반갑"습니다.

# 📌문자열 인덱싱(indexing)
a = "Hello"
print(a[0]) # H
print(a[3]) # l

# 📌문자열 슬라이싱(slicing): 부분 문자열(substring)을 얻기 위해 사용 -> 변수명[시작 인덱스:끝 인덱스] 형태
a = "Hello World"
prefix = a[:4] # 인덱스 3까지의 접두사
print(prefix) # Hell
suffix = a[2:] # 인덱스 2부터의 접미사
print(suffix) # llo World
print(a[7:10]) # orl
print(a[2:50]) # llo World -> 문자열 인덱싱을 할 때 범위를 벗어나는 경우 오류 발생 -> 슬라이싱의 경우 부드럽게 처리됨

# 📌파이썬에서 문자열은 값을 변경할 수 없기 때문에, 불변(immutable) 객체라고도 한다.
# a[3] = 'b' # TypeError: 'str' object does not support item assignment

# 📌리스트
odds = [1, 3, 5, 7, 9]
data = ["Hello", 7, 0.5]
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(evens[3]) # 8
print(evens[0:5]) # [2, 4, 6, 8, 10]

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a + b) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
]
print(arr) # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print(arr[0][1]) # 2
print(arr[2][2]) # 13

# 📌문자열은 불변(immutable) 객체, 리스트는 가변(mutable) 객체
a = [5, 6, 7, 8, 9]
a[4] = 5
print(a) # [5, 6, 7, 8, 5]
a[0] = 1
print(a) # [1, 6, 7, 8, 5]
a[1:4] = [2, 3, 4] # 특정 구간을 한꺼번에 바꾸기
print(a) # [1, 2, 3, 4, 5]

# 📌파이썬에서 2차원 이상의 리스트를 초기화할 때는 리스트 컴프리헨션(list comprehension)을 사용
# 원소를 8개 포함하는 1차원 리스트 초기화
arr = [5] * 8 # [5, 5, 5, 5, 5, 5, 5, 5]

# 4 X 5 크기를 갖는 2차원 리스트 초기화
arr = [[0] * 5 for _ in range(4)] 
print(arr) # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

arr = [[i] * 5 for i in range(4)]
print(arr) # [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]

arr = [[(i * 5) + j for j in range(5)] for i in range(4)]
print(arr) # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]

# 📌사전(Dictionary) 자료형
# 데이터를 키(key)와 값(value) 쌍의 형태로 저장할 때 사용, 모든 키(key)를 하나씩 확인할 때는 keys() 메서드 사용
data = {}
data['apple'] = '사과'
data['banana'] = '바나나'
for key in data.keys():
  print('key:', key, ", value:", data[key])
  # key: apple , value: 사과
  # key: banana , value: 바나나

# 사전 자료형은 특정한 데이터의 등장 횟수를 셀 때 효과적으로 사용 가능
data = [1, 3, 3, 5, 4, 3, 1, 4]
counter = {}
for x in data:
  if x not in counter:
    counter[x] = 1
  else:
    counter[x] += 1
print(counter) # {1: 2, 3: 3, 5: 1, 4: 2}

# 📌집합(Set) 자료형
# 데이터의 중복을 허용하지 않고, 순서가 상관없을 때 사용하는 자료형
# 특정한 데이터가 등장한 적 있는지 체크할 때 효과적으로 사용됨
data = [1, 3, 3, 5, 4, 3, 1, 4]
visited = set()
for x in data:
  if x not in visited:
    visited.add(x)
  else:
    print('중복 원소 발견:', x)
    # 중복 원소 발견: 3
    # 중복 원소 발견: 3
    # 중복 원소 발견: 1
    # 중복 원소 발견: 4
    
print('고유한 원소들:', visited) # 고유한 원소들: {1, 3, 4, 5}