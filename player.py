# 弱角色索引（根据 CHARACTER_TEMPLATES 顺序）
WEAK_CHARACTER_INDICES = [
    3,  # 農奴
    4,  # 吟遊詩人
    5,  # 學者
    8,  # 商人
    9,  # 盜賊
    11, # 煉金術師
    14, # 流浪漢
    16  # 窮鬼
]

import random

def choose_weak_character(name):
    print("\n------------------------------")
    print("Choose your weak character:")
    print("------------------------------")
    for i, idx in enumerate(WEAK_CHARACTER_INDICES, 1):
        t = CHARACTER_TEMPLATES[idx]
        print(f"{i}: {t.role}(HP:{t.base_hp}) {t.description}")
    while True:
        sel = input(f"請輸入角色編號(1~{len(WEAK_CHARACTER_INDICES)})，或按b返回：")
        if sel.strip().lower() == 'b':
            return None
        try:
            sel = int(sel)
            if 1 <= sel <= len(WEAK_CHARACTER_INDICES):
                real_idx = WEAK_CHARACTER_INDICES[sel-1]
                t = CHARACTER_TEMPLATES[real_idx]
                print("------------------------------")
                print(f"你選擇的是：{t.role} (HP:{t.base_hp}) {t.description}")
                print("------------------------------")
                confirm = input("請再次確認，輸入Y以確認，N返回上一層，其他鍵重新選擇：")
                confirm = confirm.strip().upper()
                if confirm == "Y":
                    return Player(name, real_idx)
                elif confirm == "N":
                    return None
                else:
                    continue
            else:
                print("輸入錯誤，請重新輸入。")
        except:
            print("輸入錯誤，請重新輸入。")
    print("\n------------------------------")
    print("请选择你的弱角色：")
    print("------------------------------")
    for i, idx in enumerate(WEAK_CHARACTER_INDICES, 1):
        t = CHARACTER_TEMPLATES[idx]
        print(f"{i}: {t.role}(HP:{t.base_hp}) {t.description}")
    while True:
        sel = input(f"请输入角色编号(1~{len(WEAK_CHARACTER_INDICES)})，或按b返回：")
        if sel.strip().lower() == 'b':
            return None
        try:
            sel = int(sel)
            if 1 <= sel <= len(WEAK_CHARACTER_INDICES):
                real_idx = WEAK_CHARACTER_INDICES[sel-1]
                t = CHARACTER_TEMPLATES[real_idx]
                print("------------------------------")
                print(f"你选择的是：{t.role} (HP:{t.base_hp}) {t.description}")
                print("------------------------------")
                confirm = input("请再次确认，输入Y以确认，N返回上一层，其他键重新选择：")
                confirm = confirm.strip().upper()
                if confirm == "Y":
                    return Player(name, real_idx)
                elif confirm == "N":
                    return None
                else:
                    continue
            else:
                print("输入错误，请重新输入。")
        except:
            print("输入错误，请重新输入。")

def choose_random_character(name):
    while True:
        print("\n------------------------------")
        print("隨機角色選擇：")
        print("------------------------------")
        sel = input("按Enter隨機選角，或按b返回：")
        if sel.strip().lower() == 'b':
            return None
        idx = random.randint(0, len(CHARACTER_TEMPLATES)-1)
        t = CHARACTER_TEMPLATES[idx]
        print("------------------------------")
        print(f"隨機選擇到：{t.role} (HP:{t.base_hp}) {t.description}")
        print("------------------------------")
        confirm = input("是否接受此角色？輸入Y以確認，N返回上一層，其他鍵重新隨機：")
        confirm = confirm.strip().upper()
        if confirm == "Y":
            return Player(name, idx)
        elif confirm == "N":
            return None
    while True:
        print("\n------------------------------")
        print("随机角色选择：")
        print("------------------------------")
        sel = input("按Enter随机选角，或按b返回：")
        if sel.strip().lower() == 'b':
            return None
        idx = random.randint(0, len(CHARACTER_TEMPLATES)-1)
        t = CHARACTER_TEMPLATES[idx]
        print("------------------------------")
        print(f"随机选择到：{t.role} (HP:{t.base_hp}) {t.description}")
        print("------------------------------")
        confirm = input("是否接受此角色？输入Y以确认，N返回上一层，其他键重新随机：")
        confirm = confirm.strip().upper()
        if confirm == "Y":
            return Player(name, idx)
        elif confirm == "N":
            return None


class CharacterTemplate:
    def __init__(self, role, base_hp, base_level, description, stats, base_money=0):
        self.role = role
        self.base_hp = base_hp
        self.base_level = base_level
        self.description = description
        # stats: dict, e.g. {"智慧": 80, "力量": 50, ...}
        self.stats = stats
        self.base_money = base_money



# 内建角色模板（新增 base_money）
CHARACTER_TEMPLATES = [
    CharacterTemplate("神選者", 120, 1, "被女神選中的戰士，擁有特殊天賦與美貌。", {"智慧": 85, "力量": 70, "敏捷": 80, "耐力": 75, "幸運": 90, "魔力": 95}, base_money=200),
    CharacterTemplate("領主", 150, 1, "統治領地、可契約神選者的貴族。", {"智慧": 80, "力量": 65, "敏捷": 60, "耐力": 80, "幸運": 75, "魔力": 60}, base_money=300),
    CharacterTemplate("貴族", 110, 1, "享有特權的上層階級，資源豐富。", {"智慧": 70, "力量": 55, "敏捷": 55, "耐力": 60, "幸運": 80, "魔力": 50}, base_money=150),
    CharacterTemplate("農奴", 80, 1, "底層勞動者，生命力頑強但地位低下。", {"智慧": 30, "力量": 60, "敏捷": 40, "耐力": 70, "幸運": 35, "魔力": 10}, base_money=5),
    CharacterTemplate("吟遊詩人", 90, 1, "遊歷四方，傳唱故事的自由人。", {"智慧": 60, "力量": 30, "敏捷": 65, "耐力": 50, "幸運": 85, "魔力": 40}, base_money=20),
    CharacterTemplate("學者", 100, 1, "追求知識與真理的智者。", {"智慧": 95, "力量": 25, "敏捷": 40, "耐力": 45, "幸運": 60, "魔力": 70}, base_money=30),
    CharacterTemplate("騎士", 130, 1, "效忠領主、勇敢善戰的戰士。", {"智慧": 50, "力量": 90, "敏捷": 65, "耐力": 85, "幸運": 55, "魔力": 20}, base_money=50),
    CharacterTemplate("祭司", 100, 1, "侍奉神明，能治癒與祈福。", {"智慧": 80, "力量": 35, "敏捷": 45, "耐力": 60, "幸運": 70, "魔力": 90}, base_money=40),
    CharacterTemplate("商人", 95, 1, "精於貿易，擅長資源調度與談判。", {"智慧": 75, "力量": 30, "敏捷": 55, "耐力": 50, "幸運": 95, "魔力": 25}, base_money=100),
    CharacterTemplate("盜賊", 85, 1, "行動敏捷，擅長潛行與竊取。", {"智慧": 55, "力量": 40, "敏捷": 90, "耐力": 45, "幸運": 80, "魔力": 15}, base_money=10),
    CharacterTemplate("獵人", 105, 1, "熟悉野外生存，擅長追蹤與狩獵。", {"智慧": 60, "力量": 70, "敏捷": 80, "耐力": 70, "幸運": 60, "魔力": 20}, base_money=25),
    CharacterTemplate("煉金術師", 90, 1, "研究藥劑與魔法物品的神秘學者。", {"智慧": 85, "力量": 25, "敏捷": 50, "耐力": 40, "幸運": 65, "魔力": 85}, base_money=60),
    CharacterTemplate("工匠", 100, 1, "精於打造武器、防具與建築。", {"智慧": 65, "力量": 75, "敏捷": 55, "耐力": 80, "幸運": 50, "魔力": 30}, base_money=35),
    CharacterTemplate("冒險者", 110, 1, "勇於探索未知、追求刺激的自由人。", {"智慧": 60, "力量": 70, "敏捷": 75, "耐力": 70, "幸運": 70, "魔力": 40}, base_money=15),
    CharacterTemplate("流浪漢", 70, 1, "無家可歸，卻有頑強的生存意志。", {"智慧": 35, "力量": 40, "敏捷": 45, "耐力": 80, "幸運": 30, "魔力": 5}, base_money=1),
    CharacterTemplate("魔法師", 90, 1, "掌握魔法力量，能施展各種法術。", {"智慧": 90, "力量": 20, "敏捷": 50, "耐力": 40, "幸運": 60, "魔力": 100}, base_money=80),
    CharacterTemplate("窮鬼", 60, 1, "一無所有，卻有著最強的求生本能與韌性。", {"智慧": 40, "力量": 30, "敏捷": 35, "耐力": 95, "幸運": 10, "魔力": 1}, base_money=0)
]




# 金钱范围设计（单位：铜币）
MONEY_RANGE = {
    "窮鬼": (0, 10),
    "流浪漢": (5, 50),
    "農奴": (10, 100),
    "吟遊詩人": (50, 300),
    "學者": (100, 500),
    "盜賊": (20, 150),
    "冒險者": (50, 200),
    "工匠": (100, 400),
    "獵人": (80, 300),
    "煉金術師": (200, 800),
    "祭司": (150, 600),
    "騎士": (200, 700),
    "商人": (500, 2000),
    "貴族": (2000, 10000),
    "領主": (5000, 20000),
    "神選者": (1000, 5000),
    "魔法師": (300, 1200)
}

def format_money(copper):
    gold = copper // 10000
    remain = copper % 10000
    silver = remain // 100
    copper = remain % 100
    parts = []
    if gold > 0:
        parts.append(f"{gold}金币")
    if silver > 0:
        parts.append(f"{silver}银币")
    if copper > 0 or not parts:
        parts.append(f"{copper}铜币")
    return " ".join(parts)

class Player:
    def __init__(self, name, role_index=0):
        import random
        template = CHARACTER_TEMPLATES[role_index]
        self.name = name
        self.role = template.role
        # 最大HP為角色初始值且不超過100
        self.max_hp = min(template.base_hp, 100)
        self.hp = self.max_hp
        self.level = template.base_level
        self.description = template.description
        # 六維能力
        self.stats = template.stats.copy()
        # 随机金钱
        rng = MONEY_RANGE.get(self.role, (10, 100))
        self.money_copper = random.randint(rng[0], rng[1])
        # 不同角色初始物品
        role_items = {
            "神選者": ["神秘吊坠", "精致短剑"],
            "領主": ["家族徽章", "贵族斗篷"],
            "貴族": ["金戒指", "香水瓶"],
            "農奴": ["干粮"],
            "吟遊詩人": ["破旧竖琴", "羽毛笔"],
            "學者": ["羊皮卷", "羽毛笔"],
            "騎士": ["铁剑", "旧盾牌"],
            "祭司": ["祈祷书", "圣徽"],
            "商人": ["账本", "铜秤"],
            "盜賊": ["小刀", "开锁工具"],
            "獵人": ["猎弓", "兽夹"],
            "煉金術師": ["药剂瓶", "炼金手册"],
            "工匠": ["铁锤", "工具包"],
            "冒險者": ["干粮", "短剑"],
            "流浪漢": [],
            "魔法師": ["法杖", "魔法书"],
            "窮鬼": []
        }
        items = role_items.get(self.role, [])
        # 最多2件，最少0件
        self.inventory = items[:2]

    def money_str(self):
        return format_money(self.money_copper)

    def __str__(self):
        stats_str = "，".join([f"{k}:{v}" for k, v in self.stats.items()])
        return (
            f"玩家: {self.name} | 角色: {self.role} | HP: {self.hp}/{self.max_hp} | 等级: {self.level} | 金钱: {self.money_str()}\n"
            f"说明: {self.description}\n能力：{stats_str}"
        )
