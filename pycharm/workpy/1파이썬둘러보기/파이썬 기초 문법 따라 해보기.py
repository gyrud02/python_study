# 실행 : ctrl + shift + F10

print(1+2)
print(3/2.4)
print(3*9)

a = 1
b = 2
print(a)
print(b)
print(a + b)

a = "Python"
print(a)


# 조건문
#if 조건:
a = 3
if a > 1:
    print("a is greater than 1")

# 반복문 for
#for 변수명 in [리스트(배열)]:
for a in [1,2,3]:
    print(a)

# 반복문 while
#while 변수명 < 조건:
i = 0
while i < 3:
    i = i + 1
    print(i)

# 사용자 정의 함수 만들기 (자바스크립트 function(){}과 같다)
#def add(매개변수, 매개변수, ...)
#   return 매개변수
def add(c,d):
    return c + d

#   add()함수는 띄워쓰기에 따라 사용 용도가 달라진다.

print(add(10,100))