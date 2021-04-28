def check(l):
    if  l == "a"or l == "e"or l=="i"or l == "o"or l == "u":
        l="."
    return l
s=input("請輸入一串小寫英文")
s1=""
for i in range(len(s)):
    s1+=check(s[i])
print(s1)