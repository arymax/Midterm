def decade(a):
    if a[0]==".":
        n=0
        for i in range(len(a)):
            if a[i]==".":
                n+=1

    elif a[0]=="-":
        n=10
        for i in range(len(a)):
            if a[i]==".":
                n-=1
    if a[0]=="." and a[len(a)-1]==".":
        n=5
    if a[0]=="-" and a[len(a)-1]=="-":
        n=0
    return n
password=input("輸入摩斯密碼").split(" ")
for i in password:
    print(decade(i),end="")

