s1=input("請輸入第一組數字")
s2=input("請輸入第二組數字")
a=0
b=0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        a+=1
    elif s2[i] in s1:
        b+=1
if a==4:
    print(a,"A",b,"B","，全對")
else:
    print(a,"A",b,"B","，加油")
