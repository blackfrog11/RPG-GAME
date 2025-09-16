# -*- coding: utf-8 -*-

class SpecialCharacter:
    def __init__(self):
        self.name = "【毁灭灾厄】· 緋洛米奈 (Philomena)"
        self.title = "初代灾厄之神"
        self.god = "毁灭（初代灾厄）"
        self.status = "封印中（本源沉睡于世界某处）"
        self.appearance = {
            "hair": "米白色长发",
            "eyes": "血色空洞无神的眼瞳",
            "body": "12-13岁娇小萝莉体型，柔弱",
            "dress": "华丽复杂的黑色哥特式洋裙，白色丝袜包裹纤细小腿"
        }
        self.stats = {
            "神力储备": "10 / ?????? (近乎枯竭)",
            "攻击力": "10 (仅为全盛时期的 0.001%)",
            "防御力": "50 (仅为全盛时期的 0.01%)",
            "敏捷度": "15 (仅为全盛时期的 0.001%)",
            "毁灭本源完整度": "5% / 100%",
            "潜力评级": "EX (超越SSS+)"
        }
        self.traits = [
            {"name": "核心特性 (已激活)", "desc": "【神力免疫】 - 被动 - 对所有神力攻击，拥有99%的固定伤害减免。"},
            {"name": "核心特性 (待解封)", "desc": "【万物终结】 - 被动 - 她的所有攻击，都将附加“不可逆的毁灭”概念，被她杀死的单位，灵魂将彻底湮灭，无法被任何方式复活。"}
        ]
        self.ai_interaction = [
            "她静静地坐在阴影中，血色的眼瞳空洞无神，偶尔会用指尖轻轻拨弄垂落的米白色长发。",
            "对任何靠近的生命都表现出极度冷漠，哪怕是温柔的问候，她也只是淡淡地移开视线，仿佛世间一切都与她无关。",
            "偶尔在夜深时分，她会低声呢喃着古老的咒语，声音空灵而遥远，带着一丝难以察觉的哀伤。",
            "即使面对强敌，她也不会流露出丝毫情绪，只是静静地注视着对方，仿佛在等待命运的审判。"
        ]

    def panel(self):
        info = f"角色名：{self.name}\n称号：{self.title}\n神祇：{self.god}\n当前状态：{self.status}\n"
        info += "外貌：\n"
        for k, v in self.appearance.items():
            info += f"  - {k}：{v}\n"
        info += "能力面板（封印中）：\n"
        for k, v in self.stats.items():
            info += f"  - {k}：{v}\n"
        info += "特性：\n"
        for t in self.traits:
            info += f"  - {t['name']}：{t['desc']}\n"
        info += "剧情互动与性格细节：\n"
        for line in self.ai_interaction:
            info += f"  - {line}\n"
        return info


# 新增角色：【腐朽龙姬】·罗莎莉亚 (Rosalia)
class RosaliaCharacter:
    def __init__(self):
        self.name = "【腐朽龙姬】· 罗莎莉亚 (Rosalia)"
        self.title = "腐化女神（灾厄）"
        self.rank = "三阶"
        self.appearance = {
            "hair": "如同最深邃暗夜的黑色长发",
            "eyes": "眼瞳在动情或战斗时燃起妖异血色光芒",
            "body": "约168cm，身材丰腴饱满，极致S形身材，惊人腰臀比与丰满胸围",
            "dress": "偏爱暗红与黑色哥特式礼服，大量蕾丝与束腰，展现肉感身材"
        }
        self.stats = {
            "神力储备": "3,200 / 3,200",
            "攻击力": "400 (基础值)",
            "防御力": "280 (基础值)",
            "敏捷度": "250 (基础值)",
            "潜力评级": "SSS+ (已完全解放)"
        }
        self.artifacts = [
            {"name": "神器【弑神者】", "desc": "被动 - 击杀敌人时，可吸收其生命力，为罗莎莉亚恢复10%的最大生命值。"},
            {"name": "神器【星辰腐化龙】", "desc": "被动 - 提供+25%攻击力与+15%防御力。协同 - 罗莎莉亚释放任何技能，龙臂以200%倍率同步释放，造成额外伤害。"}
        ]
        self.core_skill = {
            "name": "核心神技【不尽斩】",
            "desc": "被动 - 每击杀一单位，获一层【杀意】，永久+0.05%全属性。主动 - 消耗所有【杀意】，造成(500%+杀意层数*2%)攻击力的扇形剑气伤害。"
        }
        self.army = {
            "name": "腐朽骑士",
            "scale": "500人",
            "power": "平均为三阶中级斗气骑士"
        }
        self.ai_interaction = [
            "她总是优雅地端坐，修长的手指轻抚着礼服上的蕾丝，嘴角带着一抹若有若无的笑意。",
            "在战斗前，她会用指尖轻轻拂过自己的黑发，眼瞳中燃起妖异的血色光芒，整个人气场骤然变得危险而致命。",
            "面对下属时，她语气温柔却带着不容置疑的威严，偶尔会用玩味的目光打量对方，让人不寒而栗。",
            "她喜欢在夜晚独自一人品尝红酒，窗外月光洒落时，会轻声哼唱古老的龙族歌谣，展现出罕见的柔情一面。"
        ]

    def panel(self):
        info = f"角色名：{self.name}\n神祇：{self.title}\n当前等阶：{self.rank}\n"
        info += "外貌：\n"
        for k, v in self.appearance.items():
            info += f"  - {k}：{v}\n"
        info += "能力面板：\n"
        for k, v in self.stats.items():
            info += f"  - {k}：{v}\n"
        info += "神器：\n"
        for a in self.artifacts:
            info += f"  - {a['name']}：{a['desc']}\n"
        info += f"{self.core_skill['name']}：{self.core_skill['desc']}\n"
        info += f"军队【{self.army['name']}】：规模 - {self.army['scale']}，战力 - {self.army['power']}\n"
        info += "剧情互动与性格细节：\n"
        for line in self.ai_interaction:
            info += f"  - {line}\n"
        return info
