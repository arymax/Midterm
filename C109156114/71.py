def con(a):
    quotient=0
    remainder=0
    fs=""
    quotient =a//3
    remainder =a%3
    fs=str(remainder)+fs
    if a>=3:
        while True:
            if quotient==1 or quotient==2:
                fs=str(quotient)+fs
                break
            remainder=quotient%3
            quotient=quotient//3
            fs=str(remainder)+fs
    return fs
s=int(input("請輸入十進位的整數"))
print(con(s))

