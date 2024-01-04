import random
# 获取玩家的牌型
# 1. 生成牌
def AT ():
    poke_num = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    poke_hua = ['♥','♠','♣','♦']
    poke_list = []
    for poke_hua in poke_hua:
        count = 2
        for p_num in poke_num:
            card = [f"{poke_hua}{p_num}", count]
            poke_list.append(card)
            count += 1
    return poke_list

pokeList = AT()
# print(pokeList)
players = ['玩家一', '玩家二', '玩家三', '玩家四', '玩家五']

# 2. 发牌
def blackGirl(pl ,pk, pn):#女
    player_dir = {}
    for p_name in pl:
        p_cards = random.sample(pk, pn)
        for card in p_cards:
            pk.remove(card)
        player_dir[p_name] = p_cards
        print(f"为玩家【{p_name}】生成了牌：{p_cards}")
    return player_dir

playerDic = blackGirl(players, pokeList, 3)


# 3. 写好每种牌型的判断函数
# 冒泡排序
def sortList(dataList):
    length = len(dataList)
    for i in range(length):
        for j in range(length - i - 1):
            if dataList[j][1] > dataList[j + 1][1]:
                dataList[j], dataList[j + 1] = dataList[j + 1], dataList[j]
    return dataList

# 单张
def Dan_pair(p_cards,score):

    p_cards = sortList(p_cards)
    Quanzhong = [0.1 , 1 , 10]
    count = 0
    for card in p_cards:
        score += card[1] * Quanzhong[count]
        count += 1
    print(f"计算单牌的结果是：{score}")
    return score

#对子

def Dui_pair(p_cards,score):

    p_cards = sortList(p_cards)
    #列表推导式
    cards_val =[i[1] for i in p_cards]
    if len(set(cards_val)) == 2:
        if cards_val[0] == cards_val[1]:
            score = (cards_val[0] + cards_val[1]) * 50 +cards_val[2]
        else:
            score = (cards_val[1] + cards_val[2]) * 50 + cards_val[0]
    print(f"计算对子的结果是:{score}")
    return score

def calculate_pair(p_cards, score):
    p_cards = sortList(p_cards)
    # 列表推导式
    card_val = [i[1] for i in p_cards]
    if len(set(card_val)) == 2:
        if card_val[0] == card_val[1]:  # aab
            score = (card_val[0] + card_val[1]) * 50 + card_val[2]
        else:  # abb
            score = (card_val[1] + card_val[2]) * 50 + card_val[0]
    print(f"计算对子的结果是:{score}")
    return score

#顺子
def Sun_pair(p_cards, score):
    p_cards = sortList(p_cards)
    card_val = [i[1] for i in p_cards]
    a, b, c = card_val
    if b - a == 1 and c - b == 1:
        score *= 100
    print(f"计算顺子的结果是:{score}")
    return score
#同花
def Hua_pair(p_cards, score):
    color_val = [i[0][0] for i in p_cards]
    if len(set(color_val)) == 1:
        score *= 1000
    print(f"计算同花的结果是:{score}")
    return score

#同花顺
def Hua_Sun_pair(p_cards, score):
    # 同花
    color_val = [i[0][0] for i in p_cards]
    if len(set(color_val)) == 1:
        # 顺子
        p_cards = sortList(p_cards)
        card_val = [i[1] for i in p_cards]
        a, b, c = card_val
        if b - a == 1 and c - b == 1:
            score *= 0.1
    print(f"计算同花顺的结果是:{score}")
    return score

# # 豹子
def Bao_pair(p_cards, score):
    card_val = {i[1] for i in p_cards}
    if len(card_val) == 1:
        score *= 100000
    print(f"计算豹子的结果是:{score}")
    return score

# # 4. 比对
calc_func_orders = [
    Dan_pair,
    Dui_pair,
    Sun_pair,
    Hua_pair,
    Hua_Sun_pair,
    Bao_pair
]
player_score = []
for p_name, p_cards in playerDic.items():
    print(f"开始计算玩家【{p_name}】的牌:{p_cards}")
    score = 0
    for calc_func in calc_func_orders:
        score = calc_func(p_cards, score)
    player_score.append([p_name, score])
winner = sortList(player_score)[-1]
print(f"恭喜最后获胜的玩家是【{winner[0]}】，得分是:{winner[1]}")




















