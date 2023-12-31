#111
import random
Employee = list(range(1,301)) #员工编号
Employee_li = [] #获奖名单temp
b = input("是否进行抽奖活动，抽奖按“E”，反之退出抽奖系统")
while True:
    if b == "E":
        print("欢迎来到XXX年会抽奖环节")
# --------------------------------------三等奖--------------------------------------------
        Three = input("请输入'3'进行三等奖的抽取")
        if Three == "3":
            Employee_Three = random.sample(Employee, 30)
            if Employee_Three not in Employee_li:
                Employee_li.append(Employee_Three)
        else:
            print('输入有误，请重新输入')
            continue
        print(f"三等奖中奖名单编号为：{Employee_Three}，奖品为三斤苹果")
        for i in Employee_Three:
            Employee.remove(i)
# --------------------------------------二等奖--------------------------------------------
        Two = input("请输入'2'进行二等奖的抽取")
        if Two == "2":
            Employee_Two = random.sample(Employee, 6)
            if Employee_Two not in Employee_li:
                Employee_li.append(Employee_Two)
        else:
            print('输入有误，请重新输入')
            continue
        print(f"二等奖中奖名单编号为：{Employee_Two}，奖品为iPhone14手机")
        for j in Employee_Two:
            Employee.remove(j)
# --------------------------------------一等奖--------------------------------------------
        One = input("请输入'1'进行一等奖的抽取")
        if One == "1":
            Employee_One = random.sample(Employee, 3)
            if Employee_One not in Employee_li:
                Employee_li.append(Employee_One)
        else:
            print('输入有误，请重新输入')
            continue
        print(f"一等奖中奖名单编号为：{Employee_One}，奖品为泰国5日游+手术费报销")

        Finish = input("输入'A'重新进行抽奖活动，反之退出抽奖活动")
        if Finish == "A":
            pass
        else:
            break
    else:
        print("已退出路飞年会抽奖环节")
        break

