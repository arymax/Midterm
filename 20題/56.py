d1={"1":72,"2":62,"3":82,"4":44,"5":60}
s1=input("請輸入主餐及升級的套餐")
s2=input("是否升級成大杯飲料")
s3=input("是否升級成大薯")
p=0
if s1[1]=="A":
    p+=55
    p+=d1.get(s1[0])
elif s1[1]=="B":
    p+=68
    p+=d1.get(s1[0])
if s2=="是":
    p+=7
if s3=="是":
    p+=13
print("總共為",p,"元")

