'''
 작성일:2024년 4월 25일
 작성자:컴퓨터공학부 202495004 김현근
  설명:튜플 => 한번 생성되면 그 값을 고필 수 없는 자료형
'''
#튜플 생성
colors1 = ('red','green','blue','orange')

print("color1 : ",colors1)

print("색상중 2,3,4 번은 ?", colors1[1:4])
print("색상 거꾸로 출력 :", colors1[::-1])

# + * 연산자 사용 가능
coldrs = colors1 + colors1
print(coldrs)
print("colors1 * 10 =", colors1 * 10)
# 튜플은 추가 삭제 안됨

colors2 = ('red','green','blue','orange','pink','white','white')
print(colors2)
print("white의 개수는? ", colors2.count('white'))
print("색상에서 'green'의 위치 ", colors2.index('green'))
#튜플은 find 사용 안됨
#튜플은 생성된 후에 변경 될 수 없는 자료향 이여서 제공될 수 있는 메소드가 2개이다 