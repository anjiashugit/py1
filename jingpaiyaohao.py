# 京A·88888
import random
import string

count = 0
district = "京"

while count < 3:
    jin_pai = []
    # a = print("欢迎来到车牌摇号程序，您有三次摇号机会，小心超过了哟！！！")
    for i in range(20):
        pai = random.choice(string.ascii_uppercase)
        card = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        jin = [f"{i}", f"{district}{pai}：{card}"]
        jin_pai.append(jin)
        print(jin)
        count += 1
    b = input("进入选号环节请按“X”，反之继续摇号")
    che_pai = input("请输入车牌对应")
    for num in jin_pai:
        if che_pai == num[0]:
            print(f"您选择的车牌号为：{num[1]}",end="")
            break