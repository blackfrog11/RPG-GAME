# 保留特定角色AI互動故事生成
def generate_character_interaction(character_name, player_state=None, context=None):
	"""
	使用ollama llama3生成与剧情角色的互动文本。
	character_name: 角色名（如 'Philomena' 或 'Rosalia'）
	player_state/context: 可选，玩家当前状态或额外上下文
	返回：AI生成的剧情互动文本（简体中文）
	"""
	# 针对Philomena和Rosalia特殊身份优化prompt
	if character_name.lower() in ["philomena", "緋洛米奈", "【毁灭灾厄】· 緋洛米奈 (philomena)"]:
		prompt = (
			"你是中世纪奇幻RPG的AI叙事者。请以【毁灭灾厄】·緋洛米奈（Philomena）的身份，"
			"生成一段与陌生冒险者（玩家）互动的剧情描写。"
			"注意：她不会主动知晓玩家身份，也不会称呼玩家名字。"
			"请突出她冷漠、疏离、神秘的性格。"
		)
	elif character_name.lower() in ["rosalia", "罗莎莉亚", "【腐朽龙姬】· 罗莎莉亚 (rosalia)"]:
		prompt = (
			"你是中世纪奇幻RPG的AI叙事者。请以【腐朽龙姬】·罗莎莉亚（Rosalia）的身份，"
			"生成一段与初次见面的陌生冒险者（玩家）互动的剧情描写。"
			"注意：她不应知晓玩家身份，也不会称呼玩家名字。"
			"请突出她优雅、危险、神秘的气质。"
		)
	else:
		prompt = f"你是中世纪奇幻RPG的AI叙事者。请以{character_name}的身份，针对玩家当前的行为，生成一段细腻、富有性格和氛围的互动描写。"
	if context:
		prompt += f" 当前情境：{context}。"
	if player_state:
		prompt += f" 玩家状态：{player_state}。"
	prompt += " 直接输出简体中文剧情，不要多余说明，所有内容必须为简体中文。"
	try:
		response = requests.post(
			"http://localhost:11434/api/generate",
			json={
				"model": "llama3",
				"prompt": prompt,
				"stream": False
			},
			timeout=8
		)
		if response.status_code == 200:
			data = response.json()
			text = data.get("response", "").strip()
			if text:
				return text
	except Exception as e:
		return f"（AI生成失败：{e}）"
	return "（AI生成失败）"
# -*- coding: utf-8 -*-
import requests


# AI互動故事生成：可用於事件、分支、角色互動
def ai_generate_story(prompt, player=None, world_state=None):
	"""
	使用ollama llama3根據prompt、玩家、世界狀態生成互動故事。
	prompt: 劇情/事件/角色互動提示
	player/world_state: 可選，補充個人與世界資訊
	返回：AI生成的互動故事（簡體中文）
	"""
	full_prompt = prompt
	if player:
		full_prompt += f"\n玩家信息：角色={getattr(player, 'role', '')}，能力={getattr(player, 'stats', '')}，金钱={getattr(player, 'money_copper', '')}。"
	if world_state:
		full_prompt += f"\n世界狀態：{world_state.summary()}"
	full_prompt += "\n請生成一段細膩、沉浸、分支感強的互動故事，直接輸出簡體中文，不要多餘說明。"
	try:
		response = requests.post(
			"http://localhost:11434/api/generate",
			json={
				"model": "llama3",
				"prompt": full_prompt,
				"stream": False
			},
			timeout=12
		)
		if response.status_code == 200:
			data = response.json()
			text = data.get("response", "").strip()
			if text:
				return text
	except Exception as e:
		return f"（AI生成失败：{e}）"
	return "（AI生成失败）"
