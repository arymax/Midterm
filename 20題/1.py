s=input()
b=len(s)
a=0
while True:
    for i in range(a,b,1):
        for j in range(a,i+1):
            if j==b:
                break
            print(s[j],end="")
            if j==i:
                print(" ")
    a+=1
    if a==len(s):
        break

