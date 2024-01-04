# 要求⽤户输⼊帐号密码进⾏登陆
# ⽤户账号信息保存在⽂件内
# ⽤户密码输⼊错误三次后锁定⽤户，下次再登录，检测到是这个被锁定的⽤户，则依然不允许其它
# 登录，提示已被锁

name_dict = {

}
f = open("password_SQL", "r", encoding="utf-8")
for i in f:
    i = i.strip().split(",")
    name_dict[i[0]] = i
print(name_dict)

while 1:
    user = input("请输入登录账户")
    if user not in name_dict:
        print("非系统注册用户")
        continue
    if name_dict[user][2]=="1":
        print("当前用户已锁定重新输入")
        continue

    count = 0
    while count < 3:
        b = input("请输入登录密码")
        print(f"{name_dict[user][1]}")
        if b != name_dict[user][1]:
            print("密码错误")

        else:
            print("登录成功")
        count += 1

    if count == 3:
        name_dict[user][2] = "1"
        f1 = open("password_SQL", "w", encoding="utf-8")
        for name, pword in name_dict.items():
            line = ",".join(pword) + "\n"
            print("--------------")
            print(line)
            f1.write(line)
        f1.close()
