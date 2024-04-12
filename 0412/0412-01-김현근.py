'''
 작성일:2024년 4월 12일
 작성자:컴퓨터공학부 202495004 김현근
  설명: 구구단을 구하는 프로그램
  
  {문제분석}
  구구단은 단에 1~9을 1씩 증가시키면서 곱한다
  곱하는 수의 초기값은 1이다
  단은 고정이다
  단은 정수로 입력받아야 한다
  해당 구구단은 곱하기 하면서 바로바로 출력된다
  
  
  
  
  {알고리즘}
  1.단을 정수로 입력받는다
  2.곱하는수를 1로 초기화 한다
  3.곱하는 수를 9보다 크거나 같을 떄 까지 반복한다
   3-1.곱하는 수는 1씩증가한다
  4.구구단을 출력한다
 
  
'''
#단을 입력받는다
num=int(input("단을 입력하세요:"))
print(f"={num}단 출력=")
#곱하는 수를 1로 초기화 한다
su = 1
while su <= 9 :
    num1 = num * su
    su = su + 1
    print(f"{num} X {su-1} = {num1}")

    
    