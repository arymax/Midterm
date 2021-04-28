af=[]
bf=[]
s1=input("請輸入A的朋友").split(" ")
s2=input("請輸入B的朋友").split(" ")
for i in range(len(s1)):
    af.append(s1[i])
for i in range(len(s2)):
    bf.append(s2[i])
print(len(set(af)&set(bf)))
