def prime(a):
    if a ==2:
        boo=1
    if a%2==0:
        boo=0
    if a%2!=0:
        for i in range(2,a):
            if a%i == 0:
                boo=0
                break
            if i+1==a:
                boo=1
    return boo
n1=int(input("請輸入第一個要判斷的數字"))
n2=int(input("請輸入第二個要判斷的數字"))
if n2-n1 ==2 or n1-n2==2:
    if prime(n1)==1 and prime(n2)==1:
        print("Y")
    else:
        print("N")
else:
    print("N")
