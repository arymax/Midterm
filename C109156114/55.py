n=int(input("輸入正整數"))
for i in range(1,n+1):
    temp=i
    for j in range(1,i+1):
        print(i,end=" ")
        i+=temp
    print("")