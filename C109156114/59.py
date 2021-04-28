def cal(a, b):
    ti=0
    for i in range(a//b):
        a=a-b
        ti+=1
    return a,ti

p=int(input("輸入金額"))
c=[100,50,10,5,1]
t=0
count=0
temp=0
while True:
    if p>0:
        for i in range(5):
            if p<c[i]:
                continue
            else:
                count=i
                break
        p,t=cal(p,c[count])
        count+=1
        temp+=t
    else:
        break
print(temp)






