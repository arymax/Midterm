def breakdown(a):
    c=0
    for i in range(1,a):
        if a%i==0:
            c+=i
    return c
n=int(input("請輸入正整數n:"))
if n==breakdown(n):
    print("perfect")
else:
    print("deficient")