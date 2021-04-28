a=[]
for i in range(10):
    print("請輸入第",i+1,"個數字",end="")
    n=int(input())
    a.append(n)
a.sort()
print("最大的3個數字為",a[9],a[8],a[7])
print("最大的3個數字為",a[2],a[1],a[0])
