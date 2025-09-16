# -*- coding: utf-8 -*-

from player import CHARACTER_TEMPLATES, Player, choose_weak_character, choose_random_character
from story import player_birthplace_flow


# 只允许选择弱角或随机角色
def choose_character(name):
	while True:
		print("\n------------------------------")
		print("请选择角色模式：")
		print("------------------------------")
		print("1: 选择弱角\n2: 随机选角")
		sel = input("请输入 1 或 2，或按 b 返回：")
		if sel.strip().lower() == 'b':
			return None
		if sel == "1":
			player = choose_weak_character(name)
			if player is not None:
				return player
		elif sel == "2":
			player = choose_random_character(name)
			if player is not None:
				return player
		else:
			print("输入错误，请重新选择。")



import random
import requests

def random_fantasy_name():
	# 先尝试用 ollama llama3 生成
	try:
		prompt = "请生成一个中世纪虚幻小说风格的人名，直接输出简体中文名字，不要多余说明。"
		response = requests.post(
			"http://localhost:11434/api/generate",
			json={
				"model": "llama3",
				"prompt": prompt,
				"stream": False
			},
			timeout=5
		)
		if response.status_code == 200:
			data = response.json()
			name = data.get("response", "").strip().replace("\n", "")
			if name:
				return name
	except Exception:
		pass
	# fallback: 默认随机
	first = ["艾尔", "赛拉", "雷恩", "希尔", "亚瑟", "莉雅", "卡恩", "伊凡", "梅莉", "罗兰", "维克", "艾莉", "格兰", "菲欧", "西格", "艾德", "莉丝", "诺亚", "凯伦", "法兰"]
	last = ["·银月", "·星语", "·暗影", "·炎心", "·苍狼", "·晨曦", "·夜歌", "·烈风", "·霜刃", "·赤瞳", "·苍穹", "·铁卫", "·白羽", "·黑鸦", "·金鳞", "·雷霆", "·暮雪", "·幽兰", "·苍鹰", "·赤焰"]
	return random.choice(first) + random.choice(last)

def main():
	print("------------------------------")
	print("欢迎来到无限可能的RPG世界！")
	print("------------------------------")
	while True:
		print("请选择名字模式：")
		print("1: 自定义名字  2: 随机生成(中世纪虚幻风)")
		name_mode = input("请输入1或2：").strip()
		if name_mode == "1":
			name = input("请输入你的名字：").strip()
			if name:
				break
			else:
				print("名字不能为空，请重新输入。")
		elif name_mode == "2":
			name = random_fantasy_name()
			print(f"你的随机名字是：{name}")
			break
		else:
			print("输入错误，请重新选择。")
	while True:
		player = choose_character(name)
		if player is not None:
			break
		else:
			print("你已返回主菜单，请重新选择角色。")
	print("------------------------------")
	print(player)
	print(f"你目前拥有金钱：{player.money_str()}")
	print("------------------------------")
	birthplace = player_birthplace_flow(name, player.role)
	print(f"你的冒险将从 {birthplace} 开始！")
	print("------------------------------")
	# 简单背包与地图系统
	inventory = list(player.inventory)
	visited_places = set([birthplace])
	all_places = []
	from story import FACTIONS
	for f, v in FACTIONS.items():
		for r in v["regions"]:
			all_places.append(f"{f}-{r}")
	from story_ai import generate_character_interaction
	while True:
		print("\n------------------------------")
		print("请选择你的行动：")
		print("------------------------------")
		print("a: 探索  b: 交涉  c: 背包/状态  d: 离开")
		print(f"你目前拥有金钱：{player.money_str()}")
		action = input("请输入 a/b/c/d：").strip().lower()
		if action == "d":
			print("感谢游玩！")
			break
		elif action == "a":
			print("你选择了：探索。世界将根据你的选择动态变化……")
			# 示例：探索新地点
			import random
			unexplored = [p for p in all_places if p not in visited_places]
			if unexplored:
				new_place = random.choice(unexplored)
				visited_places.add(new_place)
				print(f"你发现了新地点：{new_place}")
			else:
				print("你已探索完所有已知地区！")
		elif action == "b":
			print("你选择了：交涉。世界将根据你的选择动态变化……")
		elif action == "c":
			while True:
				print("------------------------------")
				print("【背包/状态】  (按b返回)")
				# 六维能力展示（当前/100）
				stats_line = []
				for k, v in player.stats.items():
					stats_line.append(f"{k}{v}/100")
				print(" ".join(stats_line))
				# 生命值x/y（如85/85），最大值取自player.max_hp
				print(f"生命值 {player.hp}/{getattr(player, 'max_hp', 100)}")
				print(f"金钱：{player.money_str()}")
				print("物品：" + ("、".join(inventory) if inventory else "无"))
				print("地图：")
				for p in all_places:
					if p in visited_places:
						print(f"  - {p}")
					else:
						print(f"  - ? ? ? (未知)")
				print("------------------------------")
				sel = input("输入b返回主菜单：").strip().lower()
				if sel == "b":
					break
		else:
			print("输入错误，请重新选择。")

if __name__ == "__main__":
	main()
