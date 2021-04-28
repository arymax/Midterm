sa=input("請輸入string_a:")
sb=input("請輸入string_b:")
dic1=set(sa)&set(sb)
lis1=list(dic1)
lis1.sort()
if  len(dic1)==0:
    print("N")
else:
    for i in lis1:
        print(i,end="")