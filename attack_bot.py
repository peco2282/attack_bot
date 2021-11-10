import asyncio
import random
from datetime import datetime
from math import ceil
import nextcord as discord
from dictionaries import osdict, castimedict, dangeondict, highlv_dangeondict

# import discord
# from discord.ext import commands

# Jobについて変更

client = discord.Client()

'''
ルーンオブアルカディア Lux et Tenebrae ,~Rune of Arcadia~ 追憶と創成の間 :

メテオストライク	スペシャル　  x9
マジックボール	ノーマル    x4
ライトニングボルト	ノーマル    x3
ファイヤ・ボルケーノ	ノーマル (ルーンキャスター)    x22


氷龍の聖弓 IceCave

フロストアロー	スペシャル    x5
アイスショット	ノーマル    x1.5


浮世の冥剣 Loftgain ・ 死神の弓 Votive

バーサーク	スペシャル    x2.5
狂気	ノーマル    x1.5
レイジ	ノーマル    x2


Dorachenbogen・HässlichesBogen ドラゴンの谷 

-黒竜- ヘイロン -滅-	スペシャル    x8


Satans Bote (ストーリー報酬) エイドリアン城

血の斬撃	スペシャル    x2.5


Angel_auf_Erden エイドリアン城 

ショックストーン	スペシャル    x7
トゥルーロック	ノーマル     x4


†Twilight HeavenRay† 輝煌の残滓
神の鉄槌	スペシャル

光ある場所に	パッシブ



九例の弓 Clay Dungeon

遠距離スナイプ	スペシャル    x6 / スタン時 x13
ロックオン	ノーマル    x1.5



×Heartsbane× ムスペルへイム(バジリスク溶岩洞窟)

炎帝 ~バジリスクの炎息~	スペシャル    x8
猛火斬り	ノーマル    x1.2
'''

'''
下剋上(Boss:1.2, Mob:0.7)

ボルケ(22)

マジックボール(8倍, 4倍)

ショックストーン(7)

カオブリ(7)

雪柱(4)

オーバーシュート(1.875(スキルあり), 1.25(スキルなし))

覚醒使用時(2)

血の斬撃(2.5)

ヘイロン -滅-(8)
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
            await message.channel.send(f"{message.author.mention}, 重複しています。")

        elif (str("4_5") in tokkou) and (str("5") in tokkou):
            await message.channel.send(f"{message.author.mention}, 4_5と5は同時に装着できません")

        elif (str('4_5') in tokkou) and (str('leg') in tokkou):
            await message.channel.send(f"{message.author.mention}, 4_5とLEGEND石は同時に装着できません")

        elif (str('leg') in tokkou) and (str('5') in tokkou):
            await message.channel.send(f"{message.author.mention}, 5とLEGEND石は同時に装着できません")

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


@client.event
async def on_message_delete(message):
    print(message)


@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name + ', With ID:' + str(client.user.id))
    print('Ver.:' + discord.__version__)
    channelid = 886185192530780160
    channelid_2 = 886495611728302091
    for channel in client.get_all_channels():
        if (channel.id == channelid) or (channel.id == channelid_2):
            await channel.send("On Ready")


@client.event
async def on_resumed():
    channelid = 886185192530780160
    channelid_2 = 886495611728302091
    for channel in client.get_all_channels():
        if (channel.id == channelid) or (channel.id == channelid_2):
            await channel.send("On Resumed")


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
                await message.channel.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
                os_power = 1

            else:
                os_power = osdict[os]

            attack = await tokkoulist(message, dmg, os_power, tokkou)
            print(os_power, attack, tokkou)
            sent_message = await message.channel.send(f"{message.author.mention}\n素火力 : {dmg}\nOS : {os}\n"
                                                      f"OS倍率 : {os_power} 倍\n__**攻撃力 : {attack:.5f}**__")
            sent_message.is_system()
            await sent_message.add_reaction('🚮')


        except:
            print(tokkou)
            await message.channel.send(f':thinking: {message.author.mention}\n'
                                       f'`.dmg [攻撃力] [OS] (魔法石)`の順に入力してください。')

    # 職業
    if message.content.startswith('.job'):
        try:
            msg = message.content.split()

            dmg = float(msg[1])
            os = int(msg[2])
            tokkou_self = msg[3:]
            tokkou = msg[3:]
            os_power = 1.0
            os_raw_power = osdict[os]
            attack = await tokkoulist(message, dmg, os_power, tokkou)
            print(f'{attack}, {dmg}, {os}, {tokkou}, {os_power}')
            embed_1 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
            embed_1.set_author(name=f"By {message.author}")
            embed_1.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_power}\n魔法石： {tokkou_self}')
            embed_1.add_field(name='ソルジャー', value=f'__**攻撃力：剣：+5%: {float(attack * (os_raw_power + 0.05)):.3f},'
                                                  f' 弓：-2%: {float(attack * (os_raw_power - 0.02)):.3f},'
                                                  f' 魔法：-2%: {float(attack * (os_raw_power - 0.02)):.3f}**__', inline=False)

            embed_1.add_field(name='アーチャー', value=f"__**攻撃力：剣：-2%: {float(attack * (os_raw_power - 0.02)):.3f},"
                                                  f" 弓：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                  f" 魔法：-2%: {float(attack * (os_raw_power - 0.02)):.3f}**__",
                              inline=False)

            embed_1.add_field(name='マジシャン', value=f"__**攻撃力：剣：-2%: {float(attack * (os_raw_power - 0.02)):.3f},"
                                                  f" 弓：-2%: {float(attack * (os_raw_power - 0.02)):.3f},"
                                                  f" 魔法：+5%: {float(attack * (os_raw_power + 0.05)):.3f}**__",
                              inline=False)

            embed_1.set_footer(text='Page 1 of 4')

            embed_2 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
            embed_2.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_power}\n魔法石： {tokkou_self}')
            embed_2.set_author(name=f"By {message.author}")

            embed_2.add_field(name='ウォーリア', value=f"__**攻撃力：剣：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                  f" 弓： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                  f" 魔法： -5%: {float(attack * (os_raw_power - 0.05)):.3f}**__",
                              inline=False)

            embed_2.add_field(name='ボウマン', value=f"__**攻撃力：剣： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                 f" 弓：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                 f" 魔法： -5%: {float(attack * (os_raw_power - 0.05)):.3f}**__",
                              inline=False)

            embed_2.add_field(name='メイジ', value=f"__**攻撃力：剣： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                f" 弓： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                f" 魔法：+10: {float(attack * (os_raw_power + 0.10)):.3f}**__",
                              inline=False)

            embed_2.set_footer(text='Page 2 of 4')

            embed_3 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

            embed_3.set_author(name=f"By {message.author}")
            embed_3.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_power}\n魔法石： {tokkou_self}')
            embed_3.add_field(name='ロウニン', value=f"__**攻撃力：剣：-4%: {float(attack * (os_raw_power - 0.04)):.3f},"
                                                 f" 弓：-4%: {float(attack * (os_raw_power - 0.04)):.3f},"
                                                 f" 魔法：-4%: {float(attack * (os_raw_power - 0.04)):.3f}**__",
                              inline=False)

            embed_3.add_field(name='ドラゴンキラー', value=f"__**攻撃力：剣：-2%: {float(attack * (os_raw_power - 0.02)):.3f}, "
                                                    f" 弓：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                    f" 魔法：-2%: {float(attack * (os_raw_power - 0.02)):.3f}**__",
                              inline=False)

            embed_3.add_field(name='プリースト', value=f"__**攻撃力：剣：-10%: {float(attack * (os_raw_power - 0.10)):.3f},"
                                                  f" 弓：-10%: {float(attack * (os_raw_power - 0.10)):.3f},"
                                                  f" 魔法：-10%: {float(attack * (os_raw_power - 0.10)):.3f}**__",
                              inline=False)

            embed_3.add_field(name='スカーミッシャー', value=f"__**攻撃力：剣：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                     f" 弓：{float(attack):.3f},"
                                                     f" 魔法：{float(attack):.3f}**__", inline=False)

            embed_3.set_footer(text='Page 3 of 4')

            embed_4 = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

            embed_4.set_author(name=f"By {message.author}")
            embed_4.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_power}\n魔法石： {tokkou_self}')
            embed_4.add_field(name='ハグレモノ', value=f"__**攻撃力：剣：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                  f" 弓：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                  f" 魔法：-7%: {float(attack * (os_raw_power - 0.07)):.3f}**__",
                              inline=False)

            embed_4.add_field(name='ルーンキャスター', value=f"__**攻撃力：剣：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                     f" 弓：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                     f" 魔法：+7%: {float(attack * (os_raw_power + 0.07)):.3f}**__",
                              inline=False)

            embed_4.add_field(name='スペランカー', value=f"__**攻撃力：剣：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                   f"  弓：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                   f" 魔法：+10%: {float(attack * (os_raw_power + 0.10)):.3f}**__",
                              inline=False)

            embed_4.add_field(name='アーサー', value=f"__**攻撃力：剣：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                 f" 弓：{float(attack):.3f},"
                                                 f" 魔法：{float(attack):.3f}**__", inline=False)

            embed_4.add_field(name='シーカー', value=f"__**攻撃力：剣：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                 f" 弓：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                 f" 魔法：-7%: {float(attack * (os_raw_power - 0.07)):.3f}**__",
                              inline=False)

            embed_4.set_footer(text='Page 4 of 4')

            sent_message = await message.channel.send(embed=embed_1)
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
            await message.channel.send(f':thinking: {message.author.mention}\n'
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
                await message.channel.send(f"{message.author.mention}, 重複しています。")

            if '4.5' in cas_stone_2:
                print(cas_stone_2)
                cas_stone_2.remove("4.5")
                print(cas_stone_2)
                cas_stone_2.append("4_5")
                print(cas_stone_2)

            if (len(cas_stone_1) != len(cas_stone_2)) or (len(cas_stone_2) > 5):
                await message.channel.send(f':thinking: {message.author.mention}, キャスター石が重複しています。')

            elif ('4_5' in cas_stone_2) and ('4.5' in cas_stone_2):
                await message.channel.send(f":thinking: {message.author.mention}, 魔法石`4_5 と 4.5` は同じです。")

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
            await message.channel.send(f'元のCT : {cas_time}\nCTPrk : {cas_perk}\n'
                                       f'魔法石 : {cas_stone_2}\n__**最終的なCT : {ct}**__')

        except:
            await message.channel.send(f':thinking: {message.author.mention}, `.cas [元のCT] [CTPerk (0~10)] (魔法石)`')

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
                await message.channel.send(f"OS：{os}の時\n{want_dmg}を出すには最低でも火力が__**{ceil(ans_dmg)}**__が必要です。")

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
                    await message.channel.send(f"OSが{len(osdict)}以上必要、又は不可能な値です。")

                else:
                    await message.channel.send(f"{dmg}で{want_dmg}を出すには\n__**OSは{i}以上**__とってください。")

        except:
            await message.channel.send(f":thinking: {message.author.mention}, `.ask [欲しい火力] [今の素ダメ] '?' [魔法石]`\n"
                                       f"又は　`.ask [欲しい火力] '?' [今のOS] [魔法石]`\n"
                                       f"と入力してください。")

    if message.content.startswith('.skill'):

        try:
            msg = message.content.split()
            dmg = float(msg[1])
            os = int(msg[2])
            tokkou = msg[3:]
            os_power = osdict[os]
            print(os_power)
            attack = await tokkoulist(message, dmg, os_power, tokkou)
            embed_1 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                    description=f"**職業：ノービス**")

            embed_1.set_author(name=message.author.name)

            embed_1.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                              value=f'メテオストライク (スペシャル)：**__{attack * 9:.3f}__**\nマジックボール (ノーマル)**：__{attack * 4:.3f}__**, **(詠唱時：__{attack * 8:.3f}__**)'
                                    f'\nライトニングボルト (ノーマル)：**__{attack * 3:.3f}__**\n**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                              inline=False)

            embed_1.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                              value=f'ショックストーン (スペシャル)：**__{attack * 7:.3f}__**'
                                    f'\nトゥルーロック (ノーマル)：**__{attack * 4:.3f}__**', inline=False)

            embed_1.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                              value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{attack * 7:.3f}__**'
                                    f'\n雪柱 (ノーマル)：**__{attack * 4:.3f}__**', inline=False)

            embed_1.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                              value=f'オーバーシュート (スペシャル)：**__{attack * 12.5:.3f}__, パッシブあり：__{attack * 12.5 * 1.5:.3f}__**'
                                    f'\nシャドウパワー (ノーマル)：**__{attack * 1.5:.3f}__**'
                                    f'\nエレメンタルパワー	(パッシブ)：**__{attack * 1.5:.3f}__**', inline=False)

            embed_1.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                              value=f'血の斬撃 (スペシャル)：**__{attack * 2.5:.3f}__**', inline=False)

            embed_1.add_field(name=f'Dorachenbogen・HässlichesBogen (In ドラゴンの谷)',
                              value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{attack * 8:.3f}**__')

            embed_2 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                                    url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                    description=f"**職業：ソルジャー**")

            embed_2.set_author(name=message.author.name)

            embed_2.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                              value=f'メテオストライク (スペシャル)：**__{attack * 9 * 0.98:.3f}__**\nマジックボール (ノーマル)**：__{attack * 4:.3f}__**, **(詠唱時：__{attack * 8:.3f}__**)'
                                    f'\nライトニングボルト (ノーマル)：**__{attack * 3 * 0.98 :.3f}__**\n**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                              inline=False)

            embed_2.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                              value=f'ショックストーン (スペシャル)：**__{attack * 7:.3f}__**'
                                    f'\nトゥルーロック (ノーマル)：**__{attack * 4:.3f}__**', inline=False)

            embed_2.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                              value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{attack * 7:.3f}__**'
                                    f'\n雪柱 (ノーマル)：**__{attack * 4:.3f}__**', inline=False)

            embed_2.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                              value=f'オーバーシュート (スペシャル)：**__{attack * 12.5:.3f}__, パッシブあり：__{attack * 12.5 * 1.5:.3f}__**'
                                    f'\nシャドウパワー (ノーマル)：**__{attack * 1.5:.3f}__**'
                                    f'\nエレメンタルパワー	(パッシブ)：**__{attack * 1.5:.3f}__**', inline=False)

            embed_2.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                              value=f'血の斬撃 (スペシャル)：**__{attack * 2.5:.3f}__**', inline=False)

            embed_2.add_field(name=f'Dorachenbogen・HässlichesBogen (In ドラゴンの谷)',
                              value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{attack * 8:.3f}**__')

            await message.channel.send(embed=embed_1)


        except:
            await message.channel.send(f':thinking: {message.author.mention},`.skill [総ダメージ]`')
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
                    embed.add_field(name=f"{nums}", value=f'lv. **{lvs[i]}** , ダンジョン名：**{lists[i]}**', inline=False)
                    nums += 1

                sent_message = await message.channel.send(embed=embed)
                print('$')

                await sent_message.add_reaction('🚮')

            elif 5 > len(list_num) >= 1:
                pass

            elif len(list_num) == 0:
                await message.channel.send(f"存在しません。")

            else:
                await message.channel.send(f':thinking:')

        except:
            await message.channel.send(f'`.choice` の後に(最低lv.) (最高lv.) を入れてください。(最低lv < 最高lv), 又はもう少し範囲を広くしてください。')

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
                embed.add_field(name=str(nums), value=f"lv. **{lvs[i]}**, ダンジョン名 : **{dangeon[i]}**", inline=False)
                nums += 1

            sent_message = await message.channel.send(embed=embed)
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

        sent_message = await message.channel.send(embed=embed)
        await sent_message.add_reaction('🚮')

    if message.content.startswith('.??'):
        for guild in client.guilds:
            for member in guild.members:
                await message.channel.send(str(member))


    
client.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
