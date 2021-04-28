def com(a):
    a=a.split(",")
    a=list(map(int,a))
    a.sort()
    c=1
    for i in range(len(a)):
        if a[len(a)-1]%a[i]==0:
            c=a[i]
        if i+1==len(a)-1:
            break
    return c
s=input("輸入M個正整數，並找出任兩個正整數中最大的公因數")
print(com(s))

