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