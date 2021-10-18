from math import ceil
from datetime import datetime
import random
import discord
import asyncio

client = discord.Client()

osdict = {
    0: 1.09,
    1: 1.18,
    2: 1.27,
    3: 1.36,
    4: 1.45,
    5: 1.54,
    6: 1.63,
    7: 1.72,
    8: 1.81,
    9: 1.90,
    10: 2.02659,
    11: 2.15072,
    12: 2.22172,
    13: 2.26701,
    14: 2.29829,
    15: 2.32114,
    16: 2.33856,
    17: 2.35227,
    18: 2.36334,
    19: 2.37246,
    20: 2.38011,
    21: 2.38611,
    22: 2.39221,
    23: 2.39707,
    24: 2.40135,
    25: 2.40513,
    26: 2.40849,
    27: 2.41151,
    28: 2.41424,
    29: 2.4167,
    30: 2.41895,
    31: 2.421,
    32: 2.42289,
    33: 2.42462,
    34: 2.42623,
    35: 2.42772,
    36: 2.4291,
    37: 2.43039,
    38: 2.43159,
    39: 2.43272,
    40: 2.43377,
    41: 2.443476,
    42: 2.4357,
    43: 2.43658,
    44: 2.43742,
    45: 2.43821,
    46: 2.43895,
    47: 2.43966,
    48: 2.44034,
    49: 2.44098,
    50: 2.44159,
    51: 2.44217,
    52: 2.44273,
    53: 2.44326,
    54: 2.44377,
    55: 2.44426,
    56: 2.44473,
    57: 2.44518,
    58: 2.44561,
    59: 2.44602,
    60: 2.44642,
    61: 2.4468,
    62: 2.44717,
    63: 2.44753,
    64: 2.44787,
    65: 2.4482,
    66: 2.44852,
    67: 2.44883,
    68: 2.44913,
    69: 2.44942,
    70: 2.4497,
    71: 2.44997,
    72: 2.45024,
    73: 2.45049,
    74: 2.45074
}

dangeondict = {
    '知識の水路  --(-53, 114, 6)': 0,
    '愛の結晶  --(-3, 106, -9)': 0,
    'パントリー2  --(69, 112, 17)': 2,
    'エルドール地下室  --(12, 116, 2)': 2,
    '精錬所の地下  --(-9, 111, -50)': 2,
    'Forssa  --(799, 74, -218)': 3,
    'Forssa迷いの森  --(Forssa内)': 3,
    'エルドール鉱山  --(118, 112, -27)': 3,
    'スワロー洞窟  --(-404, 136, 121)': 4,
    '始まりの遺跡  --(91, 128, 191)': 4,
    'エルドール牢獄跡  --(-35, 118, -65)': 4,
    'エルドール洞窟  --(93, 125, 25)': 5,
    'Lovers2  --(-91, 112, -113)': 5,
    'グランスメル  --(113, 87, -204)': 5,
    'Celia\'s Big Tree  --(-514, 79, -181)': 6,
    'エルドール墓地  --(-98, 140, -6)': 7,
    'Library  --(Lovers内)': 8,
    '畑の風車小屋  --(54, 119, 64)': 8,
    'Ice Age  --(197, 120, -350)': 9,
    'エルドールの森  --(-10, 122, 47)': 9,
    'ソラリス大木  --(-300, 163, 82)': 10,
    'ルーレイ洞窟  --(-698, 79, 204)': 10,
    'FrederickMount  --(350, 75, -219)': 10,
    'エルドールのレストラン  --(40, 115, -7)': 10,
    'エルドール教会の地下  --(-55, 118, -37)': 10,
    '奈落アスレポルボー  --(トロールガ 内)': 11,
    'Deep Woods  --(516, 101, 376)': 12,
    'エルドールの不思議な森  --(57, 118, -122)': 13,
    'ロンゴノット  --(556, 86, 95)': 14,
    'マイセン洞窟  --(465, 94, 325)': 15,
    'シーク  --(-965, 65, -488)': 15,
    'Remains Corrupt  --(54, 87, -351)': 15,
    'Water Maze  --(-397, 77, 556)': 15,
    'ガルダ  --(154, 120, -1055)': 16,
    'スライム洞窟  --(527, 96, 329)': 18,
    'Oma海底ダンジョン  --(-1321, 72, 894)': 18,
    'sorrow tunnel  --(旧エルドール採掘場 内)': 19,
    'Ali\'s nest  --(210, 111, 431)': 19,
    '名もなき池  --(-150, 88, -238)': 20,
    'Flotrave  --(1336, 68, -1092)': 20,
    'Calanchies  --(-638, 135, -516)': 20,
    '底深き洞窟  --(276, 78, -962)': 20,
    'ポッポの森  --(-104, 101, 480)': 20,
    'マシュー  --(934, 30, -1286)': 21,
    'Curse mansion  --(-595, 20, -1054)': 22,
    'アラマンダー  --(-1049, 110, -803)': 23,
    'Book world  --(-475, 174, -620)': 23,
    'キャラウェイ  --(-950, 72, -1358)': 24,
    'Abandoned Waterway  --(-639, 65, -618)': 24,
    'Icicle Temple  --(1386, 142, -1125)': 25,
    '神父の地下墓地  --(1364, 84, -448)': 25,
    '精霊の巣窟  --(255, 98, -161)': 25,
    'ソドンの滝  --(364, 92, -662)': 27,
    '図書館の地下  --(Library内)': 28,
    'コロセウム  --(-1334, 73, -903)': 29,
    'Qanat  --(-985, 86, -956)': 30,
    'グリムスヴォトン  --(-1280, 98, -1186)': 30,
    'コキュートス  --(1522, 76, 197)': 31,
    'マンティナ洞窟  --(1165, 88, -1222)': 33,
    '訓練所　第1,2訓練室  --(-1014, 69, 822)': 34,
    'ジャデュベ廃坑  --(-838, 108, -1250)': 35,
    'Deja_Boo  --(907, 90, -400)': 36,
    'カシュガル(Qesqer)  --(-1123, 62, -670)': 37,
    'パーゴタリー  --(-196, 125, 389)': 38,
    'FinalFestival  --(-180, 160, -7)': 39,
    'ホートン鉱山  --(-201, 85, -103)': 40,
    'カラ・ルーナ  --(-1366, 70, -547)': 40,
    '深き洞窟  --(-1020, 104, 1225)': 40,
    '憑依船  --(-1297, 73, 705)': 41,
    'Unreasonable Gravity Island  --(194, 49, 1176)': 41,
    'Los cyanyones  --(-879, 71, -1167)': 42,
    'Red Hell Tree  --(-668, 114, -1128)': 43,
    'ザルモザラ  --(-1220, 102, -858)': 44,
    'Collapse Experiment Site  --(1110, 90, -1318)': 45,
    'タオピピ  --(パルジャ(海底村) 内)': 46,
    'マナナスラ  --(-1193, 73, -535)': 47,
    'Amber Break Cave  --(965, 76, 79)': 48,
    'Trollga  --(61, 66, -512)': 50,
    'Lavatree  --(-1096, 75, -1112)': 51,
    'ベルフォート鉱山  --(-1070, 63, 708)': 52,
    'クリベラ洞窟  --(-345, 92, -363)': 53,
    'VenLin回廊  --(1360, 114, 722)': 53,
    '死者の谷  --(-1016, 65, 119)': 54,
    'monte sub terra(モンテサブテラ)  --(-1380, 72, -745)': 55,
    'Mycelium cave  --(870, 22, -1283)': 55,
    'クラバスタ(厄災去りて闇に沈む)  --(1220, 17, -1294)': 55,
    '碧の洞窟  --(-500, 42, 1284)': 55,
    '訓練所　第3,4訓練室  --(-1014, 69, 822)': 56,
    '虚空の地下  --(-902, 69, 1124)': 57,
    '不完全な拷問所  --(-386, 130, 246)': 58,
    '芋虫ダンジョン(高難度アスレ)  --(Trollga 内)': 59,
    'bocyanyu  --(-979, 58, -1158)': 60,
    'cature  --(550, 105, -1158)': 60,
    'マリンディ鉱山  --(109, 118, -801)': 60,
    'Clay Dungeon  --(1189, 88, 410)': 60,
    'Loftgain  --(-989, 65, -1117)': 64,
    'Vambrila Castle  --(クラバスタ(厄災去りて闇に沈む) 内)': 65,
    'Votive  --(ドンケル・エルドール内)': 65,
    'Barco de la Liebre  --(574, 67, 907)': 66,
    'エイドリアン城  --(-1102, 70, 340)': 68,
    '輝煌の残滓(EX)  --(Lux et Tenebrae 内)': 68,
    '力試し  --(-80, 187, 1221)': 70,
    '永久に眠る図書館  --(-619, 29, -658)': 75,
    '厄災降臨  --(クラバスタ(厄災去りて闇に沈む) 内)': 75,
    '追憶と創成の間  --(Lux et Tenebrae-光- 又は 輝煌の残滓 クリア後 TP)': 80,
    '海底谷に沈む研究所(2鯖)  --(海底村(マーラン) 内)': 83
}

highlv_dangeondict = {
    'Underground  --(260, 155, 1)': 'アスレS',
    'Qubasar  --(364, 167, -855)': 'BossRush',
    'カルグラス遺跡  --(nyakonyan\'s secret room1(-1269,79,-927)でNPC(nyakonyan)からクエストを受ける)': 'BossRush',
    '魔界:ココリ山  --(1406, 104, 700)': 'BossRush+++',
    'Estrada Of Cave  --(-1023, 71, -107)': 'Elite',
    'Desert Templum  --(-1197, 121, -1165)': 'Elite',
    'IceCave  --(1437, 153, -1222)': 'Elite',
    'Lux et Tenebrae  --(90,88,-567 (入口: 143,170,-486))': 'Elite',
    'Tower of Judgement  --(-378, 30, 1360)': 'Extream',
    'ムスペルヘイム(バジリスク溶岩洞窟)': 'Expert',
    '魔界:封印の洞窟  --(1470, 70, -790)': 'Expert',
    '魔界:ヘルスラ  --(-906, 78, -704)': 'Expert',
    'AGNI ruins (高難易度アスレ)  --(-474, 150, -622)': 'Extra',
    'Vaaasa  --(1424, 133, -1180)': 'Extra',
    '蒼天に舞う輝煌の創者(1,2鯖)  --(Lux et Tenebrae 最初の部屋)': 'Ulutimate',
    'ドラゴンの谷  --(-1106, 89, 623)': 'Impossible(2鯖)',
    '冥界  --(ドンケル・エル・ドール内)': 'Impossible++',
    'Xen\'s Castle  --(857, 66, -745)': 'XEN',
    '魔界:ソマの谷  --(972, 75, 214)': 'UNKNOWN',
    '浮世の砂海(N)(2鯖)  --(-992,46,-1145)': '未知数',
    '浮世の砂海(T)(2鯖)  --(-992,46,-1145)': '未知数',
    'Last Judgement(2鯖)  --(-948,178,865 (入口: 90 181 -458))': 'Insanity'
}

async def tokkoulist(message, dmg, os_power, tokkou):
    if len(tokkou) == 0:
        dmg_all = dmg * os_power
        return dmg_all

    elif 1 <= len(tokkou) <= 5:
        tokkou_list = list(set(tokkou))
        tokkou_add = 1.0
        alpha = 0

        if len(tokkou) != len(tokkou_list):
            print("$")
            await message.channel.send(f"{message.author.mention}, 重複しています。")

        elif ((str("4_5") in tokkou) and (str("5") in tokkou)) or ((str("4.5") in tokkou) and (str("5") in tokkou)):
            await message.channel.send(f"{message.author.mention}, 4_5と5は同時に装着できません")

        elif ((str('4_5') in tokkou) and (str('leg') in tokkou)) or ((str('4.5') in tokkou) and (str('leg') in tokkou)):
            await message.channel.send(f"{message.author.mention}, 4_5とLEGEND石は同時に装着できません")

        elif (str('leg') in tokkou) and (str('5') in tokkou):
            await message.channel.send(f"{message.author.mention}, 5とLEGEND石は同時に装着できません")

        else:
            if str('1') in tokkou:
                tokkou_add *= 1.1

            if str('2') in tokkou:
                tokkou_add *= 1.15

            if str('3') in tokkou:
                tokkou_add *= 1.23

            if str('4') in tokkou:
                tokkou_add *= 1.35

            if (str('4_5') in tokkou) or (str('4.5') in tokkou):
                tokkou_add *= 1.40

            if str('5') in tokkou:
                tokkou_add *= 1.55

            if (str('leg') or str('LEG')) in tokkou:
                alpha = (dmg * 0.06)
                tokkou_add *= 1.55

                #####
            alldmg = dmg * os_power * tokkou_add + alpha
            return alldmg


@client.event
async def rand_ints_nodup(a, k):
    ns = []
    while len(ns) < k:
        n = random.randrange(a)
        if not n in ns:
            ns.append(n)
    return ns


print({discord.__version__})


@client.event
async def on_message_delete(message):
    print(message)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')


@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.user_id == client.user.id:
        return

    # if the reacted message is the bot's
    # and the person who reacted is the person who typed the command
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if message.author == client.user:
        if str(payload.emoji) in ('🚮', '✖️', '🗑️'):
            await message.delete()


@client.event
async def on_member_join(member: discord.Member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention}")
    await channel.send(f"分からないことがあれば、`.help` をしてください。")


@client.event
async def on_message(message: discord.Message):
    if message.content.startswith(".dmg"):
        msg = message.content.split()
        dmg = float(msg[1])
        os = int(msg[2])
        tokkou = msg[3:]

        if os >= len(osdict):
            await message.channel.send(f"OS：{os}は倍率がわかっていません。OS=0として計算します。{len(osdict)}以下にしてください。")
            os_power = 0
        else:
            os_power = osdict[os]
        attack = await tokkoulist(message, dmg, os_power, tokkou)
        async with message.channel.typing():
            # simulate something heavy
            await asyncio.sleep(0.5)
            await message.channel.send(f"素火力：{dmg}\nOS={os} \n特攻：{tokkou} \n__**攻撃力：{attack:.3f}**__")


    # ソルジャー・アーサー・マジシャン
    if message.content.startswith(".job1"):
        msg_job = message.content.split()
        job = str(msg_job[1])  # 職業
        dmg = float(msg_job[2])
        os = int(msg_job[3])
        tokkou = msg_job[4:]
        job_1 = ''
        os_power = osdict[os]
        attack = await tokkoulist(message, dmg, os_power, tokkou)
        a = float(attack) * 1.05
        b = float(attack) * 0.98
        if str(job) == 's':
            job_1 = 'ソルジャー'
        elif str(job) == 'a':
            job_1 = 'アーチャー'
        elif str(job) == 'm':
            job_1 = 'マジシャン'
        await message.channel.send(f"職業：{job_1}\nOS={os}\n特攻：{tokkou}")
        if job == str('s'):
            await message.channel.send(f"__**攻撃力：剣：+5%: {a:.3f}, 弓：-2%: {b:.3f}, 魔法：-2%: {b:.3f}**__")

        elif job == str('a'):
            await message.channel.send(f"__**攻撃力：剣：-2%: {b:.3f}, 弓：+5%: {a:.3f}, 魔法：-2%: {b:.3f}**__")

        elif job == str('m'):
            await message.channel.send(f"__**攻撃力：剣：-2%: {b:.3f}, 弓：-2%: {b:.3f}, 魔法：+5%: {a:.3f}**__")


    # ウォーリア・ボウマン・メイジ
    if message.content.startswith(".job2"):
        msg_job = message.content.split()
        job = str(msg_job[1])  # 職業
        dmg = float(msg_job[2])
        os = int(msg_job[3])
        tokkou = msg_job[4:]
        job_2 = ''
        os_power = osdict[os]
        attack = await tokkoulist(message, dmg, os_power, tokkou)
        a = float(attack) * 1.10
        b = float(attack) * 0.95
        if str(job) == 'w':
            job_2 = 'ウォーリア'
        elif str(job) == 'b':
            job_2 = 'ボウマン'
        elif str(job) == 'm':
            job_2 = 'メイジ'
        await message.channel.send(f"職業：{job_2}\nOS={os}\n特攻：{tokkou}")
        if job == str('w'):
            await message.channel.send(f"__**攻撃力：剣：+10%: {a:.3f}, 弓：-5%: {b:.3f}, 魔法：-5%: {b:.3f}**__")

        elif job == str('b'):
            await message.channel.send(f"__**攻撃力：剣：-5%: {b:.3f}, 弓：+10%: {a:.3f}, 魔法：-5%: {b:.3f}**__")

        elif job == str('m'):
            await message.channel.send(f"__**攻撃力：剣：-5%: {b:.3f}, 弓：-5%: {b:.3f}, 魔法：+10%: {a:.3f}**__")


    # ロウニン・ドラゴンキラー・プリースト・スカーミッシャー
    if message.content.startswith(".job3"):
        msg_job = message.content.split()
        job = str(msg_job[1])  # 職業
        dmg = float(msg_job[2])
        os = int(msg_job[3])
        tokkou = msg_job[4:]
        job_3 = ''
        os_power = osdict[os]
        attack = await tokkoulist(message, dmg, os_power, tokkou)
        if str(job) == 'r':
            job_3 = 'ロウニン'
        elif str(job) == 'd':
            job_3 = 'ドラゴンキラー'
        elif str(job) == 'p':
            job_3 = 'プリースト'
        elif str(job) == 's':
            job_3 = 'スカーミッシャー'
        await message.channel.send(f"職業：{job_3}\nOS={os}\n特攻：{tokkou}")
        if job == str('r'):
            await message.channel.send(
                f"__**攻撃力：剣：-4%: {float(attack * 0.96):.3f},"
                f"弓：-4%: {float(attack * 0.96):.3f},"
                f"魔法：-4%: {float(attack * 0.96):.3f}**__")

        elif job == str('d'):
            await message.channel.send(
                f"__**攻撃力：剣：-2%: {float(attack * 0.98):.3f}, "
                f"弓：+5%: {float(attack * 1.05):.3f},"
                f"魔法：-2%: {float(attack * 0.98):.3f}**__")

        elif job == str('p'):
            await message.channel.send(
                f"__**攻撃力：剣：-10%: {float(attack * 0.90):.3f},"
                f"弓：-10%: {float(attack * 0.90):.3f},"
                f"魔法：-10%: {float(attack * 0.90):.3f}**__")

        elif job == str('s'):
            await message.channel.send(
                f"__**攻撃力：剣：+5%: {float(attack * 1.05):.3f},"
                f"弓：{float(attack):.3f},"
                f"魔法：{float(attack):.3f}**__")


    # ハグレモノ・ルーンキャスター・スペランカー・アーサー・シーカー
    if message.content.startswith(".job4"):
        msg_job = message.content.split()
        job = str(msg_job[1])  # 職業
        dmg = float(msg_job[2])
        os = int(msg_job[3])
        tokkou = msg_job[4:]
        job_4 = ''
        os_power = osdict[os]
        attack = await tokkoulist(message, dmg, os_power, tokkou)
        if str(job) == 'h':
            job_4 = 'ハグレモノ'
        elif str(job) == 'r':
            job_4 = 'ルーンキャスター'
        elif str(job) == 'sp':
            job_4 = 'スペランカー'
        elif str(job) == 'a':
            job_4 = 'アーサー'
        elif str(job) == 'se':
            job_4 = 'シーカー'
        await message.channel.send(f"職業：{job_4}\nOS={os}\n特攻：{tokkou}")
        if job == str('h'):
            await message.channel.send(
                f"__**攻撃力：剣：-7%: {float(attack * 0.93):.3f},"
                f"弓：-7%: {float(attack * 0.93):.3f},"
                f"魔法：-7%: {float(attack * 0.93):.3f}**__")

        elif job == str('r'):
            await message.channel.send(
                f"__**攻撃力：剣：-7%: {float(attack * 0.93):.3f},"
                f"弓：-7%: {float(attack * 0.93):.3f},"
                f"魔法：+7%: {float(attack * 1.07):.3f}**__")

        elif job == str('sp'):
            await message.channel.send(
                f"__**攻撃力：剣：+10%: {float(attack * 1.10):.3f},"
                f"弓：+10%: {float(attack * 1.10):.3f},"
                f"魔法：+10%: {float(attack * 1.10):.3f}**__")

        elif job == str('a'):
            await message.channel.send(
                f"__**攻撃力：剣：+5%: {float(attack * 1.05):.3f},"
                f"弓：{float(attack):.3f},"
                f"魔法：{float(attack):.3f}**__")

        elif job == str('se'):
            await message.channel.send(
                f"__**攻撃力：剣：-7%: {float(attack * 0.93):.3f},"
                f"弓：+10%: {float(attack * 1.10):.3f},"
                f"魔法：-7%: {float(attack * 0.93):.3f}**__")


    # キャスター計算
    if message.content.startswith(".cas"):
        cas = message.content.split()
        ct = int(cas[1])
        ct_p = int(cas[2])
        cas_stones = cas[3:]
        ct_perk = 1
        cas_stone = 1
        try:
            if 1 == ct_p:
                ct_perk = 0.95

            elif 2 == ct_p:
                ct_perk = 0.90

            elif 3 == ct_p:
                ct_perk = 0.85

            elif 4 == ct_p:
                ct_perk = 0.80

            elif 5 == ct_p:
                ct_perk = 0.75

            elif 6 == ct_p:
                ct_perk = 0.70

            elif 7 == ct_p:
                ct_perk = 0.65

            elif 8 == ct_p:
                ct_perk = 0.60

            elif 9 == ct_p:
                ct_perk = 0.55

            elif 10 == ct_p:
                ct_perk = 0.50

            if 1 <= len(cas_stones) <= 5:

                if len(cas_stones) != len(list(set(cas_stones))):
                    print("$")
                    await message.channel.send(f"{message.author.mention}, 重複しています。")

                if str('1') in cas_stones:
                    cas_stone *= 0.95

                if str('2') in cas_stones:
                    cas_stone *= 0.90

                if str('3') in cas_stones:
                    cas_stone *= 0.84

                if str('4') in cas_stones:
                    cas_stone *= 0.77

                if (str('4_5') or str('4.5')) in cas_stones:
                    cas_stone *= 0.72

                if str('5') in cas_stones:
                    cas_stone *= 0.60

            cas_all = float(ct * ct_perk * cas_stone)
            await message.channel.send(
                f"元のCT：{str(ct)}\nCTPerk：{str(ct_perk)}\n魔法石：{str(cas_stones)}\n__**CT：{cas_all}**__")

        except:
            pass
    # Dmg, OS計算
    if message.content.startswith(".ask"):
        msg = message.content.split()
        wantdmg = float(msg[1])
        dmg = msg[2]
        os = msg[3]
        tokkou = msg[4:]
        try:
            if dmg == '?':  # Dmg不明
                dmg = 1.0
                os = int(os)
                os_power = osdict[os]
                attack = await tokkoulist(message, dmg, os_power, tokkou)
                dmg = wantdmg / attack
                await message.channel.send(f"OS：{os}の時\n{wantdmg}を出すには最低でも火力が__**{ceil(dmg)}**__が必要です。")

            if os == '?':  # OS不明
                dmg = float(msg[2])
                os_power = 1.0
                # os_power = await oslist(message, os)

                attack = await tokkoulist(message, dmg, os_power, tokkou)
                # os比較
                xos = wantdmg / attack
                await message.channel.send(f"{xos}倍")
                i = 1
                while xos >= osdict[i]:
                    i += 1
                    if i >= len(osdict):
                        i = 'miss'
                        break
                if i == 'miss':
                    await message.channel.send(f"OSが61以上必要、又は不可能な値です。")
                else:
                    await message.channel.send(f"{dmg}で{wantdmg}を出すには\n__**OSは{i}以上**__とってください。")

        except:
            pass

    if message.content.startswith('.choice1'):
        msg = message.content.split()
        lists = []
        lvs = []
        try:
            low = int(msg[1])
            high = int(msg[2])
            print(low, high)

            for i in dangeondict:
                value = int(dangeondict[i])
                # print(value, i)
                if low <= value <= high:
                    lists.append(i)
                    lvs.append(value)
            print('?')
            if lists <= 4:
                print('!Q')
            list_num = await rand_ints_nodup(len(lists), 5)
            embed = discord.Embed(title='**ダンジョン選択結果**', color=discord.Color.dark_green(), timestamp=datetime.utcnow())
            embed.set_author(name=message.author.name)
            nums = 1
            print(list_num)
            if len(list_num) >= 5:
                for i in list_num:
                    embed.add_field(name=nums, value=f'lv. **{lvs[i]}** , ダンジョン名：**{lists[i]}**', inline=False)
                    nums += 1

                sent_message = await message.reply(embed=embed)
                print('$')

                await sent_message.add_reaction('🚮')
            else:
                await message.channel.send(f':thinking:')

        except:
            await message.reply(f'`.choice` の後に(最低lv.) (最高lv.) を入れてください。(最低lv < 最高lv), 又はもう少し範囲を広くしてください。')


    if message.content.startswith('.choice2'):
        dangeon = []
        lvs = []
        list_num = await rand_ints_nodup(len(highlv_dangeondict), 5)
        try:
            for i in highlv_dangeondict:
                value = str(highlv_dangeondict[i])
                dangeon.append(i)
                lvs.append(value)
            nums = 1
            embed = discord.Embed(title='ダンジョン選択結果', color=discord.Color.dark_gold(), timestamp=datetime.utcnow())
            embed.set_author(name=message.author.name)
            for i in list_num:
                embed.add_field(name=nums, value=f"lv. **{lvs[i]}**, ダンジョン名 : **{dangeon[i]}**", inline=False)
                nums += 1

            sent_message = await message.reply(embed=embed)
            await sent_message.add_reaction('🚮')
        except:
            pass

    # help
    if message.content == '.help1':
        embed = discord.Embed(title="コマンド一覧", color=discord.Colour.gold(), timestamp=datetime.utcnow())
        embed.set_author(name=message.author.name)
        embed.add_field(name='ヘルプ', value='.help', inline=False)
        embed.add_field(
            name='ダメージ計算', value='.dmg [攻撃力] [OS] [魔法石(1~5, ただし4_5, 5, LEGは重複不可)]', inline=False)
        embed.add_field(
            name='職業込みでのダメージ計算', value='.job(1~4) [職業] [攻撃力] [OS] [魔法石(1~5, ただし4_5と5は重複不可)]', inline=False)
        embed.add_field(name='職業[.job1]について',
                        value='ソルジャー:s, アーチャー:a, マジシャン:m', inline=False)
        embed.add_field(name='職業[.job2]について',
                        value='ウォーリア:w, ボウマン:b, メイジ:m', inline=False)
        embed.add_field(
            name='職業[.job3]について', value='ロウニン:r, ドラゴンキラー:d, プリースト:p, スカーミッシャー:s', inline=False)
        embed.add_field(
            name='職業[.job4]について', value='ハグレモノ:h, ルーンキャスター:r, スペランカー:sp, アーサー:a, シーカー:se', inline=False)

        sent_message = await message.reply(embed=embed)
        await sent_message.add_reaction('🚮')


    if message.content == '.help2':
        embed = discord.Embed(title="コマンド一覧", color=discord.Colour.lighter_gray(), timestamp=datetime.utcnow())
        embed.set_author(name=message.author.name)
        embed.add_field(
            name='キャスター', value='.cas [CT] [CTPerk] [魔法石(1 ~ 5)]', inline=False)
        embed.add_field(name='最低OSを求める場合', value='.ask [欲しい火力] [今の素ダメ] ? [魔法石]', inline=False)
        embed.add_field(name='最低火力を求める場合', value='.ask [欲しい火力] ? [OS] [魔法石]', inline=False)

        sent_message = await message.reply(embed=embed)
        await sent_message.add_reaction('🚮')


    if message.content == '.help3':
        embed = discord.Embed(title='', color=discord.Color.dark_green(), timestamp=datetime.utcnow())
        embed.set_author(name=message.author.name)
        embed.add_field(name='レベルが数値であるダンジョンの時', value='.choice1 [最低lv] [最高lv]', inline=False)
        embed.add_field(name='レベルが特殊なダンジョンの時', value='.choice2', inline=False)
        sent_message = await message.reply(embed=embed)
        await sent_message.add_reaction('🚮')
    
client.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
