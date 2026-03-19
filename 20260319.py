a = int(input("입력 진수 결정(16/10/8/2) : "))
if a == 16 :
      num10 = int(input("값입력 :"), 16)
if a == 10 :
      num10 = int(input("값입력 :"), 10)
if a == 8  :
      num10 = int(input("값입력 :"), 8)
if a == 2  :
      num10 = int(input("값입력 :"), 2)
    

print("16진수 ==> ", hex(num10))
print("10진수 ==> ", dec(num10))
print("8진수 ==> ", oct(num10))
print("2진수 ==> ", bin(num10))