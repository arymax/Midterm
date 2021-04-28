data={}
n=int(input("輸入n的值"))
for i in range(n):
    name=input("請輸入姓名")
    email=input("請輸入電子郵件")
    data.update({name:email})
search=input("請輸入要查詢的電子郵件")
if search in data.keys():
    print(data.get(search))
else:
    print("無此人")