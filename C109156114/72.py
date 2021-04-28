n=int(input("請輸入n"))
k=int(input("請輸入k"))
total=0
remainder1=n//k
total=n+remainder1

if remainder1>=k:
    remainder2=remainder1//k
    total+=remainder2


print(total)