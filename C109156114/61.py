def lol(a):
    b=0
    c=0
    a=a-75
    b+=1
    c+=6
    rou=1
    while a>=30:
        rou+=1
        b+=1
        a-=30
        if b<3:
            c+=6
        elif b==3:
            b=0
            c+=7
        if rou%2==0:
            c-=1
    return (a,b,c)
time=input("輸入遊戲時間").split(":")
second=int(time[0])*60+int(time[1])
result=lol(second)
print(result[2],"隻兵")


