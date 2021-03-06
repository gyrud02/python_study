# 숫자형 데이터는 어떻게 만들고 사용할까?

# 1. 정수형(Integer)
# - 양수, 음수, 0
# ex) a라는 이름의 변수 메모리 공간에 123 양의 정수를 저장할 수 있다.
a = 123
print(a)

# ex) a라는 이름의 변수 메모리 공간에 -178 음의 정수를 저장할 수 있다.
a = -178
print(a)

a = 0
print(a)

# 2. 실수형(floating point)
# - 소수점이 포함된 숫자를 말한다.
# ex) a 변수에 1.2라는 실수를 저장할 수 있다.
a = 1.2
print(a)

a = -3.45
print(a)

# 3. 컴퓨터 지수 값
# ex) a라는 이름의 변수 메모리 공간에 컴퓨터 지수표현 방식으로 4.24E10 또는 4.24e10 실수를 저장할 수 있다.
a = 4.24E10 # 4.24E10은 4.24 * 10의 10승의 값을 의미한다.
print(a)

a = 4.24e-10 # 4.24e-10은 4.24 * 10의 -10승의 값을 의미한다.
print(a)

# ex) 8진수와 16진수
# - 8진수는 숫자0 + 알파벳소문자o 또는 대문자O로 시작하는 숫자값이다.
a = 0o177
print(a) # 출력값 127

a = 0O177
print(a) # 출력값 127

# - 16진수를 만들기 위해서는 0x로 시작한다.
a = 0x8ff
print(a) # 출력값 2303

# ---------- 참고 : 8진수나 16진수는 파이썬에서 사용되지 않는 형태의 숫자 자료형이기 때문에 눈에 익히고 넘어가도 된다.