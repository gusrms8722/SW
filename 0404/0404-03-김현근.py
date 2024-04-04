'''
 작성일:2024년 4월 4일
 작성자:컴퓨터공학부 202495004 김현근
  설명: 숫자와 연산자를 입력 받아 사칙연산의 결과 출력
         
  {문제분석}
     필요한 변수:num1,num2,op
     사칙연산은 +, -, *, /
     두개의 정수와 연산자를 입력받는다
     더하기는 +
     뺴기는 -
     곱하기는 *
     나누기는 /
     @,#,$, 등은 연산자가 아니다
     사칙연산을 제외한 나머지 모든 문자는 잘못된 입력이다
     
  {알고리즘}
  1.첫번째 숫자를 입력 받는다
  2.연산자 입력 받는다
  3.두번째 숫자를 입력 받는다
  4.만약에 연산자가 +이면
   4-1.덧셈을 출력한다
  5.아니고 연산자가 -이면
   5-1. 뺼셈을 출력한다
  6.아니고 연산자가 *이면
   6-1. 곱셈을 출력한다
  7.아니고 연산자가 /이면
   7-1. 나누기를 계산한다
  8.아니면
   8-1. 해당 연산자는 없습니다
   
'''

#2개의 정수를 입력받기
num1=int(input("첫번째수를 입력하세요:"))
op = input("연산자를 입력하세요:")
num2=int(input("두번째수를 입력하세요:"))

if op=="+" :
    print (f"{num1} + {num2} = {num1 + num2}입니다")
elif op=="-" :
    print (f"{num1} - {num2} = {num1 - num2}입니다")
elif op=="*" :
    print (f"{num1} * {num2} = {num1 * num2}입니다")
elif op=="/" :
    print (f"{num1} / {num2} = {num1 / num2}입니다")
else :
    print("해당 연산자는 없습니다")