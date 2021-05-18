import discord
from discord.ext import tasks, commands

import re

class AbstractResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__last_member = None

    async def handle_messages(message):
        await AbstractResponses.replies(message)
        await AbstractResponses.reactions(message)

    async def replies(message):
        content = message.content.lower()
        for key in reply_list:
            if key in content:
                await message.reply(reply_list[key])

    async def reactions(message):
        content = message.content.lower()
        for key in react_list:
            if key in content.split():    
                await message.add_reaction(react_list[key])

react_list = {
        "this!":                "<:this:823714994424250368>",
        "fax":                  "<:Fax:816331584999391262>",
        "dababy":               "<:dababy:827036898504736788>",
        "cactus":               "🌵",
        "no":                   "❤️"
        }

reply_list = {
        "thisdge":      "https://cdn.discordapp.com/attachments/189827180610453505/822571054773174282/unknown.png",
        "salaander":    "salaander",
        "i cant quite find the words jaden, and i consider myself an erudite man,":   "what the actual fuck my son",
        "yes ma'am":    "https://cdn.discordapp.com/attachments/431240474188316672/837663670674522132/Screenshot_20210427-170307_Snapchat.png",
        "what if my birthday cake is like a mcyt dnf basori knightxhornet septiplier hamilton": "what the actual fuck",
        "revolution":   "动态网自由门 天安門 天安门 法輪功 李洪志 32 bugs 六四天安門事件 The Ogrecord N Word Ban 天安門大屠殺 Congratulations Will 反右派鬥爭 The Racist Struggle 大躍進政策 Titanfall Forever 文化大革命 The Great Jakecord Revolution人權 Don Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Glorious Rules Chat台灣 臺灣 Lucascord Formosa 中華民國 Republic of Ogrecord 西藏 土伯特 唐古特 Tiles 達賴喇嘛 Jaden Pagillo 法輪功 Owen Kung 新疆維吾爾自治區 The Balls Itch Server Autonomous Region 諾貝爾和平獎 Funny Animals 劉暁波 This! 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Campbell 劉曉波动态网自由门"
        }
