"""
#NOTE - 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#NOTE - 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#NOTE - boolean (참/거짓)
print(5>10) # False
print(5<10) # True
print(True) # True
print(False) # False
print(not True) # True
print(not (5>10)) # True

#NOTE - 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은 " + name + "예요")
print(name + "는 " + str(age) + "살이며 " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

Quiz)  변수를 이용하여 다음 문장을 출력하시오

변수명
 : station

변수값
 : "사당", "신도림", "인청공항" 순서대로 입력

출력문장
 : xx 행 열차가 들어오고 있습니다.

station = "사당"
print(station + " 행 열차가 들어오고 있습니다.")

#NOTE - 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2.0

print(2**3) # 2^3 = 8
print(5%3) # 5(mod) 3 = 2 나머지 구하기는 %
print(10%3) # 10(mod) 3 = 1
print(5//3) # 5(반수) 3 = 1 몫 구하기 //

#NOTE - 비교
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(1 <= 3) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 5 == 8) # True

print(1 < 3 < 5 < 7 < 9) # True

#NOTE - 더 동작
print(1 != 3) # True
print(not(1 != 3)) # False

print((3>0) and (3<5)) # True
print((3>0) & (3<5)) # True

print (3>0) or (3>5) # True
print (3>0) | (3>5) # True

print(5>4>3) # True
print(5>4>7) # False

#NOTE - 간단한 수식
print(2+2*3) # 8
print((2+2)*3) # 10
number = 2+2*3 #8
print(number) # 8
number = number + 2 #10
print(number) # 10
number += 2 # 12
print(number) # 12
number *= 2 # 24
print(number) # 24
number /= 2 # 12
print(number) # 12
number -= 2 # 10
print(number) # 10
number %= 5 # 0
print(number) # 0

#NOTE - 숫자 처리 함수
print(abs(-5)) # 5 절대값 absolate value
print(pow(4,2)) # 4^2 = 16  power
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 4 내림
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 제곱근

#NOTE - 랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0
print(random()*10) # 0.0 ~ 10.0
print(int(random()*10)) # 0 ~ 10 int를 붙이는 이유는 정수를 만들기 위해서
print(int(random()*10)+1) # 1 ~ 10
print(randrange(1,46)) # 1 ~ 46
print(randint(1,45))

Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정 되었습니다.

from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정 되었습니다.")

#NOTE - 문자열
sentence = '나는 소년입니다.'
print(sentence) => 나는 소년입니다.
sentence2 = "파이썬은 쉬워요."
print(sentence2) => 파이썬은 쉬워요.

#NOTE - 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0~ 2 직전 까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 :" + jumin[7:]) # 7직전까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

#NOTE - 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 모든문자 소문자
print(python.upper()) # 모든문자 대문자
print(python[0].isupper()) #파이썬의 문자가 첫번째 문자가 대문자 인지 확인 맞으면 True, 틀리면 False

print(len(python)) # 길이
print(python.replace("Python","Java"))

index = python.index("n")
print(index) #첫번째 n의 위치
index = python.index("n",index+1)
print(index) #첫번째 n의 위치 다음 순서부터 n을 찾음

print(python.find("Java")) # 원하는 값이 없을경우 -1 을 출력
print(python.index("Java")) # 원하는 값이 없을경우 오류로 실행 종료

print(python.count("n")) # n의 갯수를 세줌

#NOTE - 문자열 포멧
#방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "python")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20) => %s사용법
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}살입니다. {1}색과 {2}색을 좋아해요.".format(20, "파란", "빨간"))

#방법 3
print("나는 {age}살입니다. {name}색과 {food}색을 좋아해요.".format(age = 20, name = "파란", food = "빨간"))

#방법 4(v3.6)
age = 20
color = "빨간"
print(f"나는 {age}살입니다. {color}색을 좋아해요.")

#NOTE - 탈출 문자
# \n : new line
print("백문이 불여일견\n 백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "개발고수" 입니다.
print('저는 "개발고수" 입니다.')
print("저는 \"개발고수\" 입니다.")

#\\ : 문장 내에서 \ 경로 출력할때
print("C:\\Users\\songj\\Desktop\\python")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

#\t : 탭 (여러칸을 띄운다)
print("Red\tApple")


# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분읜 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 "e" 갯수 + "!" 로 구성
#                    (nav)               (5)            (1)           (!)
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
print (my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print ("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

"""

#NOTE - 리스트





