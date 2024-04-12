'''
 작성일:2024년 4월 12일
 작성자:컴퓨터공학부 202495004 김현근
  설명: 구구단을 구하는 프로그램
  '''
  
  #단을 입력받는다
num=int(input("단을 입력하세요:"))
print(f"={num}단 출력=")
for su in range(1,10) :
    print (f"{num} X {su} = {num * su}")