'''
 작성일:2024년 3월 28일
 작성자:컴퓨터공학부 202495004 김현근
  설명: 숫자를 입력받아 양수인지 음수인지 0인지 판단하시오.
         
  {문제분석}
     필요한 변수:num
     숫자를 입력 받는다.->정수로 변환->변수에 저장
     양수는 0보다 큰 수입니다
     음수는 0보다 작은 수 입니다
     입력받은 숫자가 양수인지 음수인지 판단하는 조건문을 만들자
     
  {알고리즘}
  1. 숫자를 입력받아 정수로 변환하여 변수에 저장한다
  2. 숫자가 0보다 큰수일때
   2-1."양수입니다"출력
  3.아니고 만약 숫자가 0보다 작은수 일때
   3-1."음수입니다"출력
  4.아니면
   4-1"0입니다" 출력
  5."감사합니다" 출력=> 조건과 상없
  
'''

#숫자를 입력받는다
num=int(input("점수를 입력하세요:"))

#숫자가 0보다 큰수일때 양수입니다 출력
if num>0 :
    print("양수입니다")
elif num<0 :
    print("음수입니다")
else :
    print("0입니다.")
print("감사합니다")


