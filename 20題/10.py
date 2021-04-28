s=input().split(" ")
n=int(s[0])
m=int(s[1])
arr=[list(range(m))for i in range(n)]
for i in range(n):
    v=input("輸入第"+str(i+1)+"列").split(" ")
    for j in range(m):
        arr[i][j]=v[j]
print(arr)
for i in range(m):
    print("輸出反轉後矩陣第"+str(i+1)+"列")
    for j in range(n):
        print(arr[j][i],end=" ")
    print("")
