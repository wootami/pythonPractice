# 0.파이썬 명명규칙
# 기본적으로 스네이크 케이스(snake_case)를 사용.
# 클래스 이름은 카멜 케이스(CamelCase)를 사용.

# 0.주석 처리
'''여러 문장 주석 처리
print("이것은 실행되지 않습니다.") '''

# 1.파이썬 자료형
# 숫자 자료형
a = 10
b = 3.14

# 문자열 자료형
name = "Alice"
greeting = 'Hello, World!'

# 불린 자료형
is_active = True

# 리스트 자료형
fruits = ["apple", "banana", "cherry"]

# 튜플 자료형
coordinates = (10.0, 20.0)

# 딕셔너리 자료형
person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}

print("숫자:", a, b)
print("문자열:", name + greeting)
print("불린:",is_active,"테스트") 
print("리스트:", fruits) 
print("튜플:", coordinates)
print("딕셔너리 :", person)
print("우리집" + name + "는 " , a , "살 입니다.") 

station = ["사당", "신도림", "인천공항"]
print(station, "행 열차가 들어오고 있습니다.")
print("------------------------------------------")
# -------------------------------------------------------
# 2.연산자
# 산술 연산자
x = 15
y = 4
print("산술 연산자:")
print("덧셈:", x + y)
print("뺄셈:", x - y)
print("곱셈:", x * y)
print("나눗셈:", x / y)
print("몫:", x // y)
print("나머지:", x % y)
print("거듭제곱:", x ** y)
# 비교 연산자
print("\n비교 연산자:")
print("같음:", x == y)
print("같지 않음:", x != y)
print("크다:", x > y)
print("작다:", x < y)
print("크거나 같음:", x >= y)
print("작거나 같음:", x <= y)
# 논리 연산자
a = True
b = False
print("\n논리 연산자:")
print("AND:", a and b)
print("OR:", a or b)
print("NOT:", not a)
print( 1 !=3)
print((3 > 0) and (3 < 5))
print("------------------------------------------")
# -------------------------------------------------------

# 3.입력과 출력
# 입력 받기
# user_name = input("이름을 입력하세요: ")
# user_age = input("나이를 입력하세요: ")
# print("안녕하세요, " + user_name + "님! 당신은 " + user_age + "살 입니다.")

# 출력하기
print("파이썬 프로그래밍에 오신 것을 환영합니다!")  
print("오늘은 즐거운 하루가 될 거예요.")
print("------------------------------------------")
# -------------------------------------------------------

# 4.숫자 처리 함수
from math import *
print("숫자 처리 함수:")
print("절댓값: -7 ->", abs(-7))
print("반올림 3.6 ->: ", round(3.6))
print("거듭제곱: 2,3 ->", pow(2, 3))
print("내림: 3.9 ->", floor(3.9))
print("올림: 3.1 ->" , ceil(3.1))
print("최대값: 10, 20, 5 ->", max(10, 20, 5))
print("최소값: 10, 20, 5 ->", min(10, 20, 5))
print("제곱근: 16 ->", sqrt(16))
print("------------------------------------------")
# -------------------------------------------------------

# 5.랜덤 함수
from random import *

print(random())
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10))
print(int(random() * 45) + 1) # 1~45 사이의 임의의 값 생성

print(randrange(1,46)) # 1~45 사이의 임의의 값 생성

random_day = randrange(4,29)
print ("오프라인 스터티 모임 날짜는 매월",random_day ,"일로 선정되었습니다.")
print("------------------------------------------")
# -------------------------------------------------------

# 6. 슬라이싱
jumin = "011016-3213213"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("------------------------------------------")
# -------------------------------------------------------

# 7.문자열 처리 함수 
python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # index("찾는 문자열" , 어느 인덱스 부터 찾을건지)
print(index) 

print(python.find("Java")) # 없으면 -1 반환
# print(python.index("Java")) # 실행 오류 남  

print(python.count("n"))