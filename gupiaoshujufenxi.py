# 程序启动后，给⽤户提供查询接⼝，允许⽤户᯿复查股票⾏情信息(⽤到循环)
# 2. 允许⽤户通过模糊查询股票名，⽐如输⼊“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来
# 3. 允许按股票价格、涨跌幅、换⼿率这⼏列来筛选信息，⽐如输⼊“价格>50”则把价格⼤于50的股票
# 都打印，输⼊“市盈率<50“，则把市盈率⼩于50的股票都打印，不⽤判断等于。
# 思路提示：加载⽂件内容到内存，转成dict or list结构，然后对dict or list 进⾏查询等操作。 这样以后
# 就不⽤每查⼀次就要打开⼀次⽂件了，效率会⾼。

gp_dit = {

}
f = open("stock_data.txt", "r", encoding="utf-8")
# data=f.read()
# print(data)
for i in f:
    gp_num = i.strip().split(",")
    gp_dit[gp_num[1]] = gp_num
# print(gp_dit)
a = input("请输入要查询的股票信息")
for key, value in gp_dit.items():

    if a == value[1]:
        print(f"{value}")
    else:
        print(f"没有{value[1]}股票信息",end="")
        exit()
