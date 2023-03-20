# 📌조건문
# 사용자로부터 입력을 받을 때는 input() 함수를 사용
# x = int(input())
# y = int(input())

# # 조건문 내부에 대하여 띄어쓰기를 4번 사용, 어떠한 값이 다른 값과 동일한지 구할 때는 "==" 사용
# if y == 0:
#     print('0으로 나눌 수 없음')
# else:
#     print(x / y)

# if elif -> elif나 else는 옵션
score = 90
if score >= 94:
    print('1등급')
elif score >= 87:
    print('2등급')
elif score >= 81:
    print('3등급')
else:
    print('3등급 미만')
    
# 📌반복문
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(x)

# for문은 어떠한 시퀀스의 원소에 차례대로 접근한다는 점에서 range() 함수와 함께 사용됨 -> range(start, end)
result = 0
for i in range(1, 51): # 1부터 50까지 방문
    result += i
    
print(result) # 1275

# 1~50까지의 수 중 10의 배수만 더하기
result = 0
for i in range(1, 51):
    if i % 10 == 0:
      result += i

print(result) # 150

# 📌enumerate() 함수를 사용하면 인덱스와 함께 반복 가능
name_list = ['원뭉치', '두뭉치', '세뭉치']
for i, ele in enumerate(name_list):
    print(i, ele)
    # 0 원뭉치
    # 1 두뭉치
    # 2 세뭉치

# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i * j)
        
# 1부터 N까지의 수 중에서 소수 찾기 -> 소수가 아닌 경우, 어떤 수의 배수인지 출력한 뒤에 해당 수에 대한 반복문을 탈출
n = 10
for x in range(2, n + 1):
    prime_number = True
    for y in range(2, x):
        if x % y == 0:
            print(x, '=', y, '*', x // y)
            prime_number = False
            break # 반복문 탈출
    if prime_number:
        print(x, '은(는) 소수입니다.')
        # 2 은(는) 소수입니다.
        # 3 은(는) 소수입니다.
        # 4 = 2 * 2
        # 5 은(는) 소수입니다.
        # 6 = 2 * 3
        # 7 은(는) 소수입니다.
        # 8 = 2 * 4
        # 9 = 3 * 3
        # 10 = 2 * 5
        
# 📌함수
# 함수는 def 구문을 이용하여 작성
def add(a, b, c):
    result = a + b + c
    return result

print(add(1, 3, 5)) # 9
print(add(3, 5, 7)) # 15

# 리스트 내 원소 중에서 가장 큰 값의 인덱스(위치)를 찾아서 반환
def find_max_index(arr):
    max_index = 0
    for i in range(len(arr)):
        if arr[max_index] < arr[i]:
            max_index = i
    return max_index

data = [7, 1, 5, 9, 3, 2, 4]
max_index = find_max_index(data)
print(max_index) # 3

# 특정한 값을 가지는 원소의 인덱스를 찾는 함수
def find_certain_value(arr, value):
    for i, x in enumerate(arr):
        if x == value:
            return i
    return -1 # 찾지 못한 경우 -1을 반환

print(find_certain_value([3, 5, 7, 9], 2)) # -1
print(find_certain_value([3, 5, 7, 9], 7)) # 2