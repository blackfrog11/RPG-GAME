# -*- coding: utf-8 -*-
"""
世界狀態管理模組
- 管理全局大事件、各勢力/地區狀態、玩家聲望、主線/分支進度、結局等
"""

class WorldState:
    def __init__(self):
        # 世界大事件進度
        self.events = {
            "北境保衛戰": False,
            "龍族盟約": False,
            "龍族戰爭": False,
            "帝國內戰": False,
            "災厄紀元": False
        }
        # 各地區/勢力狀態
        self.faction_status = {
            "狮鹫帝國": {"安全": True, "內亂": False},
            "龍塔國": {"盟約": False, "戰爭": False},
            "獸人群落": {"叛亂": False},
            "精靈森林": {"詛咒": False},
            "腐化之地": {"怪物潮": False, "威脅等級": 1}
        }
        # 玩家與各勢力聲望（-100~100）
        self.reputation = {
            "狮鹫帝國": 0,
            "龍塔國": 0,
            "獸人群落": 0,
            "精靈森林": 0,
            "腐化之地": 0,
            "北境大公": 0,
            "龍族": 0,
            "精靈": 0,
            "獸人": 0,
            "女神": 0,
            "百姓": 0
        }
        # 主線/分支進度
        self.mainline = None  # 當前主線名
        self.flags = set()    # 劇情觸發標記
        # 已解鎖結局
        self.unlocked_endings = set()

    def set_event(self, event, value=True):
        if event in self.events:
            self.events[event] = value

    def set_faction_status(self, faction, key, value):
        if faction in self.faction_status and key in self.faction_status[faction]:
            self.faction_status[faction][key] = value

    def add_reputation(self, target, delta):
        if target in self.reputation:
            self.reputation[target] = max(-100, min(100, self.reputation[target] + delta))

    def set_mainline(self, mainline):
        self.mainline = mainline

    def add_flag(self, flag):
        self.flags.add(flag)

    def unlock_ending(self, ending):
        self.unlocked_endings.add(ending)

    def summary(self):
        s = ["【世界狀態總覽】"]
        s.append("大事件：" + ", ".join([k for k, v in self.events.items() if v]))
        s.append("主線進度：" + (self.mainline or "無"))
        s.append("聲望：" + ", ".join([f"{k}:{v}" for k, v in self.reputation.items()]))
        s.append("已解鎖結局：" + ("、".join(self.unlocked_endings) if self.unlocked_endings else "無"))
        return "\n".join(s)
