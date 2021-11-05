import asyncio
import random
from datetime import datetime
from math import ceil
import discord
from discord.ext import commands

client = discord.Client()

osdict = {
    0: 1.00,
    1: 1.09,
    2: 1.18,
    3: 1.27,
    4: 1.36,
    5: 1.45,
    6: 1.54,
    7: 1.63,
    8: 1.72,
    9: 1.81,
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

castimedict = {
    0: 1.00,
    1: 0.95,
    2: 0.90,
    3: 0.85,
    4: 0.80,
    5: 0.75,
    6: 0.70,
    7: 0.65,
    8: 0.60,
    9: 0.55,
    10: 0.50
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

'''
ルーンオブアルカディア Lux et Tenebrae ,~Rune of Arcadia~ 追憶と創成の間 :

メテオストライク	スペシャル
マジックボール	ノーマル
ライトニングボルト	ノーマル
ファイヤ・ボルケーノ	ノーマル (ルーンキャスター)


氷龍の聖弓 IceCave

フロストアロー	スペシャル
アイスショット	ノーマル


浮世の冥剣 Loftgain ・ 死神の弓 Votive

バーサーク	スペシャル
狂気	ノーマル
レイジ	ノーマル


Dorachenbogen・HässlichesBogen ドラゴンの谷 

-黒竜- ヘイロン -滅-	スペシャル


Satans Bote (ストーリー報酬) エイドリアン城

血の斬撃	スペシャル


Angel_auf_Erden エイドリアン城 

ショックストーン	スペシャル
トゥルーロック	ノーマル


九例の弓 Clay Dungeon

遠距離スナイプ	スペシャル


×Heartsbane× ムスペルへイム(バジリスク溶岩洞窟)

炎帝 ~バジリスクの炎息~	スペシャル

'''
'''

class HogeButton(discord.ui.View):
    def __init__(self, args):
        super().__init__()
        for txt in args:
            self.add_item(HugaButton(txt))


class HugaButton(discord.ui.Button):
    def __init__(self, txt: str):
        super().__init__(label=txt, style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{interaction.user.display_name}は{self.label}を押しました')

'''
'''
@client.event
async def makeButton(ctx: commands.context, *args):
    await ctx.send('Press!', view=HogeButton(args))

'''
async def tokkoulist(message, dmg, os_power, tokkou):
    if len(tokkou) == 0:
        dmg_all = dmg * os_power
        return dmg_all

    elif 1 <= len(tokkou) <= 5:
        if '4.5' in tokkou:
            print(tokkou)
            tokkou.remove('4.5')
            print(tokkou)
            tokkou.append('4_5')
            print(tokkou)

        tokkou_list = list(set(tokkou))
        tokkou_add = 1.0
        alpha = 0

        if len(tokkou) != len(tokkou_list):
            print("$")
            await message.reply(f"{message.author.mention}, 重複しています。")

        elif (str("4_5") in tokkou) and (str("5") in tokkou):
            await message.reply(f"{message.author.mention}, 4_5と5は同時に装着できません")

        elif (str('4_5') in tokkou) and (str('leg') in tokkou):
            await message.reply(f"{message.author.mention}, 4_5とLEGEND石は同時に装着できません")

        elif (str('leg') in tokkou) and (str('5') in tokkou):
            await message.reply(f"{message.author.mention}, 5とLEGEND石は同時に装着できません")

        else:
            if str('1') in tokkou:
                tokkou_add *= 1.1
                tokkou.remove("1")
                print("1", tokkou_add, tokkou)

            if str('2') in tokkou:
                tokkou_add *= 1.15
                tokkou.remove("2")
                print("2", tokkou_add, tokkou)

            if str('3') in tokkou:
                tokkou_add *= 1.23
                tokkou.remove("3")
                print("3", tokkou_add, tokkou)

            if str('4') in tokkou:
                tokkou_add *= 1.35
                tokkou.remove('4')
                print("4", tokkou_add, tokkou)

            if str('4_5') in tokkou:
                tokkou_add *= 1.40
                tokkou.remove("4_5")
                print("4_5", tokkou_add, tokkou)

            if str('5') in tokkou:
                tokkou_add *= 1.55
                tokkou.remove("5")
                print("5", tokkou_add, tokkou)

            if str('leg') in tokkou:
                alpha = (dmg * 0.06)
                tokkou_add *= 1.55
                tokkou.remove("leg")
                print("leg", tokkou_add, tokkou)

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
    channelid = 886185192530780160
    for channel in client.get_all_channels():
        if channel.id == channelid:
            await channel.send("On Ready")


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
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    print(reaction, user)


@client.event
async def on_message(message: discord.Message):
    if message.content.startswith('.dmg'):
        msg = message.content.split()
        # ダメージ・OS・魔法石
        dmg = float(msg[1])
        os = int(msg[2])
        tokkou = msg[3:]

        try:
            if os > len(osdict):
                await message.reply(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
                os_power = 1

            else:
                os_power = osdict[os]

            attack = await tokkoulist(message, dmg, os_power, tokkou)
            print(os_power, attack, tokkou)
            sent_message = await message.reply(f"{message.author.mention}\n素火力 : {dmg}\nOS : {os}\n"
                                               f"OS倍率 : {os_power} 倍\n__**攻撃力 : {attack:.5f}**__")
            sent_message.is_system()
            await sent_message.add_reaction('🚮')


        except:
            print(tokkou)
            await message.reply(f':thinking: {message.author.mention}\n'
                                f'`.dmg [攻撃力] [OS] (魔法石)`の順に入力してください。')

    # 職業
    if message.content.startswith('.job'):
        try:
            msg = message.content.split()

            dmg = float(msg[1])
            os = int(msg[2])
            tokkou = msg[3:]
            os_power = osdict[os]
            attack = await tokkoulist(message, dmg, os_power, tokkou)
            embed_1 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
            embed_1.set_author(name=f"By {message.author}")
            embed_1.add_field(name='ソルジャー', value=f'__**攻撃力：剣：+5%: {float(attack + (dmg * os_power * 0.05)):.3f},'
                                                  f' 弓：-2%: {float(attack - (dmg * os_power * 0.02)):.3f},'
                                                  f' 魔法：-2%: {float(attack * 0.98):.3f}**__', inline=False)

            embed_1.add_field(name='アーチャー', value=f"__**攻撃力：剣：-2%: {float(attack - (dmg * os_power * 0.02)):.3f},"
                                                  f" 弓：+5%: {float(attack + (dmg * os_power * 0.05)):.3f},"
                                                  f" 魔法：-2%: {float(attack - (dmg * os_power * 0.02)):.3f}**__", inline=False)

            embed_1.add_field(name='マジシャン', value=f"__**攻撃力：剣：-2%: {float(attack - (dmg * os_power * 0.02)):.3f},"
                                                  f" 弓：-2%: {float(attack - (dmg * os_power * 0.02)):.3f},"
                                                  f" 魔法：+5%: {float(attack + (dmg * os_power * 0.05)):.3f}**__", inline=False)

            embed_1.set_footer(text='Page 1 of 4')

            embed_2 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

            embed_2.set_author(name=f"By {message.author}")

            embed_2.add_field(name='ウォーリア', value=f"__**攻撃力：剣：+10%: {float(attack + (dmg * os_power * 0.10)):.3f},"
                                                  f" 弓： -5%: {float(attack - (dmg * os_power * 0.05)):.3f},"
                                                  f" 魔法： -5%: {float(attack - (dmg * os_power * 0.05)):.3f}**__", inline=False)

            embed_2.add_field(name='ボウマン', value=f"__**攻撃力：剣： -5%: {float(attack - (dmg * os_power * 0.05)):.3f},"
                                                 f" 弓：+10%: {float(attack + (dmg * os_power * 0.10)):.3f},"
                                                 f" 魔法： -5%: {float(attack - (dmg * os_power * 0.05)):.3f}**__", inline=False)

            embed_2.add_field(name='メイジ', value=f"__**攻撃力：剣： -5%: {float(attack - (dmg * os_power * 0.05)):.3f},"
                                                f" 弓： -5%: {float(attack - (dmg * os_power * 0.05)):.3f},"
                                                f" 魔法：+10: {float(attack + (dmg * os_power * 0.10)):.3f}**__", inline=False)

            embed_2.set_footer(text='Page 2 of 4')

            embed_3 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

            embed_3.set_author(name=f"By {message.author}")

            embed_3.add_field(name='ロウニン', value=f"__**攻撃力：剣：-4%: {float(attack - (dmg * os_power * 0.04)):.3f},"
                                                 f" 弓：-4%: {float(attack - (dmg * os_power * 0.04)):.3f},"
                                                 f" 魔法：-4%: {float(attack - (dmg * os_power * 0.04)):.3f}**__", inline=False)

            embed_3.add_field(name='ドラゴンキラー', value=f"__**攻撃力：剣：-2%: {float(attack - (dmg * os_power * 0.02)):.3f}, "
                                                    f" 弓：+5%: {float(attack + (dmg * os_power * 0.05)):.3f},"
                                                    f" 魔法：-2%: {float(attack - (dmg * os_power * 0.02)):.3f}**__", inline=False)

            embed_3.add_field(name='プリースト', value=f"__**攻撃力：剣：-10%: {float(attack - (dmg * os_power * 0.10)):.3f},"
                                                  f" 弓：-10%: {float(attack - (dmg * os_power * 0.10)):.3f},"
                                                  f" 魔法：-10%: {float(attack - (dmg * os_power * 0.10)):.3f}**__", inline=False)

            embed_3.add_field(name='スカーミッシャー', value=f"__**攻撃力：剣：+5%: {float(attack + (dmg * os_power * 0.05)):.3f},"
                                                     f" 弓：{float(attack):.3f},"
                                                     f" 魔法：{float(attack):.3f}**__", inline=False)

            embed_3.set_footer(text='Page 3 of 4')

            embed_4 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

            embed_4.set_author(name=f"By {message.author}")

            embed_4.add_field(name='ハグレモノ', value=f"__**攻撃力：剣：-7%: {float(attack - (dmg * os_power * 0.07)):.3f},"
                                                  f" 弓：-7%: {float(attack - (dmg * os_power * 0.07)):.3f},"
                                                  f" 魔法：-7%: {float(attack - (dmg * os_power * 0.07)):.3f}**__", inline=False)

            embed_4.add_field(name='ルーンキャスター', value=f"__**攻撃力：剣：-7%: {float(attack - (dmg * os_power * 0.07)):.3f},"
                                                     f" 弓：-7%: {float(attack - (dmg * os_power * 0.07)):.3f},"
                                                     f" 魔法：+7%: {float(attack + (dmg * os_power * 0.07)):.3f}**__", inline=False)

            embed_4.add_field(name='スペランカー', value=f"__**攻撃力：剣：+10%: {float(attack + (dmg * os_power * 0.10)):.3f},"
                                                   f"  弓：+10%: {float(attack + (dmg * os_power * 0.10)):.3f},"
                                                   f" 魔法：+10%: {float(attack + (dmg * os_power * 0.10)):.3f}**__", inline=False)

            embed_4.add_field(name='アーサー', value=f"__**攻撃力：剣：+5%: {float(attack + (dmg * os_power * 0.05)):.3f},"
                                                 f" 弓：{float(attack):.3f},"
                                                 f" 魔法：{float(attack):.3f}**__", inline=False)

            embed_4.add_field(name='シーカー', value=f"__**攻撃力：剣：-7%: {float(attack - (dmg * os_power * 0.07)):.3f},"
                                                 f" 弓：+10%: {float(attack + (dmg * os_power * 0.10)):.3f},"
                                                 f" 魔法：-7%: {float(attack - (dmg * os_power * 0.07)):.3f}**__", inline=False)

            embed_4.set_footer(text='Page 4 of 4')

            sent_message = await message.reply(embed=embed_1)
            '''+
            emoji_selector = u'\U0000fe0f\U000020e3'
            emoji_1 = u'\N{DIGIT ONE}' + emoji_selector
            emoji_2 = u'\N{DIGIT TWO}' + emoji_selector  # 2⃣
            emoji_3 = u'\N{DIGIT THREE}' + emoji_selector  # 3⃣
            emoji_4 = u'\N{DIGIT FOUR}' + emoji_selector
            await sent_message.add_reaction(emoji_1)
            await sent_message.add_reaction(emoji_2)
            await sent_message.add_reaction(emoji_3)
            await sent_message.add_reaction(emoji_4)
            '''
            print(message.author, client.user)
            emoji_list = ['⏪', '⏩']
            page = 0
            embed_list = [embed_1, embed_2, embed_3, embed_4]

            for add_emoji in emoji_list:
                await sent_message.add_reaction(add_emoji)

            # リアクションチェック用の関数
            def check(reaction, user):
                # botを呼び出した本人からのリアクションのみ受け付ける
                # reaction.message == msg を入れないと複数出したときに全て連動して動いてしまう
                return user == message.author and reaction.message == sent_message and str(reaction.emoji) in emoji_list

            while True:
                try:
                    # リアクションが付けられるまで待機
                    reaction, user = await client.wait_for('reaction_add', timeout=20.0, check=check)

                except asyncio.TimeoutError:
                    # 一定時間経ったら消す
                    # for remove_emoji in emoji_list:
                    # await sent_message.remove_reaction(emoji=remove_emoji, member=client.user)
                    await sent_message.clear_reactions()
                    break

                else:
                    # 付けられたリアクションに対応した処理を行う
                    if str(reaction.emoji) == (emoji_list[0]):
                        # ページ戻し
                        # ページ数の更新(0~最大ページ数-1の範囲に収める)
                        page = (page - 1) % len(embed_list)

                    if str(reaction.emoji) == (emoji_list[1]):
                        # ページ送り
                        # ページ数の更新(0~最大ページ数-1の範囲に収める)
                        page = (page + 1) % len(embed_list)

                    print(page)
                    await sent_message.edit(embed=embed_list[page])

                    # リアクションをもう一度押せるように消しておく
                    await sent_message.remove_reaction(reaction.emoji, message.author)




        except:
            await message.reply(f':thinking: {message.author.mention}\n'
                                f'`.job [攻撃力] [OS] (魔法石)`の順に入力してください。')

    if message.content.startswith('.cas'):
        msg = message.content.split()
        xct = 1.0
        try:
            cas_time = float(msg[1])
            cas_perk = int(msg[2])
            cas_stone_1 = str(msg[3:])
            cas_stone_2 = list(set(cas_stone_1))

            ct_perk = castimedict[cas_perk]

            if cas_stone_2 != cas_stone_1:
                await message.reply(f"{message.author.mention}, 重複しています。")

            if '4.5' in cas_stone_2:
                print(cas_stone_2)
                cas_stone_2.remove("4.5")
                print(cas_stone_2)
                cas_stone_2.append("4_5")
                print(cas_stone_2)

            if (len(cas_stone_1) != len(cas_stone_2)) or (len(cas_stone_2) > 5):
                await message.reply(f':thinking: {message.author.mention}, キャスター石が重複しています。')

            elif ('4_5' in cas_stone_2) and ('4.5' in cas_stone_2):
                await message.reply(f":thinking: {message.author.mention}, 魔法石`4_5 と 4.5` は同じです。")

            elif '1' in cas_stone_2:
                xct *= 0.95

            elif '2' in cas_stone_2:
                xct *= 0.90

            elif '3' in cas_stone_2:
                xct *= 0.84

            elif '4' in cas_stone_2:
                xct *= 0.77

            elif '4_5' in cas_stone_2:
                xct *= 0.72

            elif '5' in cas_stone_2:
                xct *= 0.60

            ct = cas_time * ct_perk * xct
            await message.reply(f'元のCT : {cas_time}\nCTPrk : {cas_perk}\n'
                                f'魔法石 : {cas_stone_2}\n__**最終的なCT : {ct}**__')

        except:
            await message.reply(f':thinking: {message.author.mention}, `.cas [元のCT] [CTPerk (0~10)] (魔法石)`')

    if message.content.startswith('.ask'):
        msg = message.content.split()
        try:
            want_dmg = float(msg[1])
            now_dmg = msg[2]
            str_os = msg[3]
            tokkou = msg[4:]

            if now_dmg == '?':
                dmg = 1.0
                os = int(str_os)
                os_power = osdict[os]
                attack = await tokkoulist(message, dmg, os_power, tokkou)
                ans_dmg = want_dmg / attack
                await message.reply(f"OS：{os}の時\n{want_dmg}を出すには最低でも火力が__**{ceil(ans_dmg)}**__が必要です。")

            if str_os == '?':
                dmg = float(msg[2])
                os_power = 1.0
                attack = await tokkoulist(message, dmg, os_power, tokkou)
                xos = want_dmg / attack

                i = 0

                while xos >= osdict[i]:
                    if i > len(osdict):
                        i = 'miss'
                        break
                    i += 1

                if i == 'miss':
                    await message.reply(f"OSが{len(osdict)}以上必要、又は不可能な値です。")

                else:
                    await message.reply(f"{dmg}で{want_dmg}を出すには\n__**OSは{i}以上**__とってください。")

        except:
            await message.reply(f":thinking: {message.author.mention}, `.ask [欲しい火力] [今の素ダメ] '?' [魔法石]`\n"
                                f"又は　`.ask [欲しい火力] '?' [今のOS] [魔法石]`\n"
                                f"と入力してください。")

    if message.content.startswith('.skill'):
        msg = message.content.split()
        attack = float(msg[1])
        try:
            embed_1 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                    description=f"ルーンオブアルカディア (From: Lux et Tenebrae), \n"
                                                f"~Rune of Arcadia~ (From: 追憶と創成の間)")
            embed_1.set_author(name=f"By {message.author}")
            embed_1.add_field(name='',
                              value=f"メテオストライク (スペシャル)\n"
                                    f"{attack}")
            embed_1.add_field(name='', value='', inline=False)
            embed_1.set_footer(text='Page 1 of 4')

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
            if len(lists) <= 4:
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

            elif 5 > len(list_num) >= 1:
                pass

            elif len(list_num) == 0:
                await message.channel.send(f"存在しません。")

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
    if message.content.startswith('.help'):
        embed = discord.Embed(title="コマンド一覧", color=discord.Colour.gold(), timestamp=datetime.utcnow())
        embed.set_author(name=message.author.name)
        embed.add_field(name='ヘルプ', value='.help', inline=False)
        embed.add_field(
            name='ダメージ計算', value='.dmg [攻撃力] [OS] [魔法石(1~5, ただし4_5, 5, LEGは重複不可)]', inline=False)
        embed.add_field(
            name='職業込みでのダメージ計算', value='.job [攻撃力] [OS] [魔法石(1~5, ただし4_5と5は重複不可)]', inline=False)
        embed.add_field(
            name='キャスター', value='.cas [CT] [CTPerk] [魔法石(1 ~ 5)]', inline=False)
        embed.add_field(name='最低OSを求める場合', value='.ask [欲しい火力] [今の素ダメ] ? [魔法石]', inline=False)
        embed.add_field(name='最低火力を求める場合', value='.ask [欲しい火力] ? [OS] [魔法石]', inline=False)

        sent_message = await message.reply(embed=embed)
        await sent_message.add_reaction('🚮')


    
client.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
