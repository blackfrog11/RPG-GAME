# 主流程：角色出生地选择与分配
def player_birthplace_flow(player_name, player_role):
	# 强势角色可选全部地区，弱角只能选弱势地区
	strong_roles = ["贵族", "领主", "神选者"]
	all_places = []
	for f, v in FACTIONS.items():
		for r in v["regions"]:
			all_places.append(f"{f}-{r}")
	weak_places = [
		"狮鹫帝国-村落", "兽人群落-兽人村", "龙塔国-边境村落", "腐化之地-废墟", "精灵森林-精灵村"
	]
	if player_role in strong_roles:
		print("------------------------------")
		print("请选择出生地（可选任意地区）：")
		print("------------------------------")
		for i, place in enumerate(all_places, 1):
			print(f"{i}: {place}")
		sel = input(f"请输入出生地编号(1~{len(all_places)})：")
		try:
			sel = int(sel)
			if 1 <= sel <= len(all_places):
				want_place = all_places[sel-1]
			else:
				want_place = all_places[0]
		except:
			want_place = all_places[0]
		real_place, reason = assign_birthplace(player_role, force_weak=False, want_place=want_place)
	else:
		print("------------------------------")
		print("请选择出生地（仅限弱势地区）：")
		print("------------------------------")
		for i, place in enumerate(weak_places, 1):
			print(f"{i}: {place}")
		sel = input(f"请输入出生地编号(1~{len(weak_places)})：")
		try:
			sel = int(sel)
			if 1 <= sel <= len(weak_places):
				want_place = weak_places[sel-1]
			else:
				want_place = weak_places[0]
		except:
			want_place = weak_places[0]
		real_place, reason = assign_birthplace(player_role, force_weak=True, want_place=want_place)
	msg = birthplace_message(want_place, real_place, reason)
	print(msg)
	return real_place
# 勢力與地圖資料結構
FACTIONS = {
	"狮鹫帝國": {
		"center": True,
		"duke": "中央大公",
		"nobles": ["帝國貴族", "領主", "神選者"],
		"regions": ["帝都", "貴族領地", "村落"]
	},
	"龍塔國": {
		"direction": "東",
		"duke": "東方大公",
		"nobles": ["龍族貴族", "龍裔"],
		"regions": ["龍塔", "邊境村落"]
	},
	"獸人群落": {
		"direction": "西",
		"duke": "西方大公",
		"nobles": ["獸人首領", "部落勇士"],
		"regions": ["獸人村", "荒野"]
	},
	"精靈森林": {
		"direction": "南",
		"duke": "南方大公",
		"nobles": ["精靈王族", "長老"],
		"regions": ["精靈村", "古樹林"]
	},
	"腐化之地": {
		"direction": "北",
		"duke": "北方大公",
		"nobles": ["腐化領主", "災厄神選者"],
		"regions": ["腐化城", "廢墟"]
	}
}

# 出生地分配邏輯
def assign_birthplace(player_role, force_weak=False, want_place=None):
	import random
	weak_places = [
		"狮鹫帝國-村落", "獸人群落-獸人村", "龍塔國-邊境村落", "腐化之地-廢墟", "精靈森林-精靈村"
	]
	if force_weak:
		# 強制只從弱勢地區分配
		if want_place and want_place in weak_places:
			birthplace = want_place
		else:
			birthplace = random.choice(weak_places)
		reason = "你只能出生於弱勢地區，命運多舛但充滿可能。"
		return birthplace, reason
	# 原有分配邏輯
	if player_role in ["貴族", "領主"]:
		birthplace = random.choice(["狮鹫帝國-帝都", "狮鹫帝國-貴族領地"])
		reason = "你的身份屬於上層階級，出生於帝國核心地區。"
	elif player_role == "神選者":
		birthplace = random.choice([
			"神殿遺跡", "精靈森林-古樹林", "腐化之地-廢墟", "狮鹫帝國-神殿"
		])
		reason = "神選者多半在特殊地點誕生，命運非凡。"
	elif player_role == "農奴":
		birthplace = random.choice([
			"狮鹫帝國-村落", "獸人群落-獸人村", "龍塔國-邊境村落"
		])
		reason = "農奴多半出生於偏遠村落，生活艱辛。"
	else:
		all_regions = []
		for f, v in FACTIONS.items():
			for r in v["regions"]:
				all_regions.append(f"{f}-{r}")
		birthplace = random.choice(all_regions)
		reason = "你的身份無明顯限制，出生地隨機分配。"
	return birthplace, reason

# 出生地提示
def birthplace_message(want_place, real_place, reason):
	if want_place != real_place:
		return f"你原本想出生在{want_place}，但因為你的身份，實際出生在{real_place}。({reason})"
	else:
		return f"你如願出生在{real_place}。({reason})"
