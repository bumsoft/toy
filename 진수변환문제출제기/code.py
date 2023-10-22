## 2 8 10 16진수 변환 문제출제기##
import random
import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

aa=10
a=2
b=10
c=8
d=16
list=[a,b,c,d]
while aa>0:
    x = random.randrange(1,1000)
    random.shuffle(list)
    print("다음",list[0],"진수를", list[1],"진수로 바꾸시오: ",convert(x,list[0]))
    k = int(input("정답을 보려면 아무키 입력:"))
    if k!=1000000:
          print(convert(x,list[1]))
    aa=int(input("다음문제를 푸려면 아무 숫자 입력(종료는 0:"))
    print("\n\n")
