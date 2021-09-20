from math import ceil
import discord
import asyncio

from discord import message
client = discord.Client()

osdict = {
    0:1.09,
    1:1.18,
    2:1.27,
    3:1.36,
    4:1.45,
    5:1.54,
    6:1.63,
    7:1.72,
    8:1.81,
    9:1.90,
    10:2.02659,
    11:2.15072,
    12:2.22172,
    13:2.26701,
    14:2.29829,
    15:2.32114,
    16:2.33856,
    17:2.35227,
    18:2.36334,
    19:2.37246,
    20:2.38011,
    21:2.38611,
    22:2.39221,
    23:2.39707,
    24:2.40135,
    25:2.40513,
    26:2.40849,
    27:2.41151,
    28:2.41424,
    29:2.4167,
    30:2.41895,
    31:2.421,
    32:2.42289,
    33:2.42462,
    34:2.42623,
    35:2.42772,
    36:2.4291,
    37:2.43039,
    38:2.43159,
    39:2.43272,
    40:2.43377,
    41:2.443476,
    42:2.4357,
    43:2.43658,
    44:2.43742,
    45:2.43821,
    46:2.43895,
    47:2.43966,
    48:2.44034,
    49:2.44098,
    50:2.44159,
    51:2.44217,
    52:2.44273,
    53:2.44326,
    54:2.44377,
    55:2.44426,
    56:2.44473,
    57:2.44518,
    58:2.44561,
    59:2.44602,
    60:2.44642
    }


'''
    else:
        await message.channel.send(f"すみませんまだ作成中です")
        os_power = 1.0
        return os_power
'''
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

        elif ((str("4_5") in tokkou) and (str("5") in tokkou)):
            await message.channel.send(f"{message.author.mention}, 4_5と5は同時に装着できません")

        elif ((str('4_5') in tokkou) and (str('leg') in tokkou)):
            await message.channel.send(f"{message.author.mention}, 4_5とLEGEND石は同時に装着できません")

        elif ((str('leg') in tokkou) and (str('5') in tokkou)):
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

            if str('4_5' or '4.5') in tokkou:
                tokkou_add *= 1.40

            if str('5') in tokkou:
                tokkou_add *= 1.55

            if (str('leg') or str('LEG')) in tokkou:
                alpha = (dmg * 0.06)
                tokkou_add *= 1.55

                #####
            alldmg = dmg * os_power * tokkou_add + alpha
            return alldmg


async def thumb(message: discord.Message):
    channel = message.channel
    await channel.send('Send me that 👍 reaction, mate')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) == '👍'

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await channel.send('👎')
    else:
        await channel.send('👍')



@client.event
async def on_message_delete(message):
    print(message)

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')


@client.event
async def on_member_join(member: discord.Member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention},こんにちは")
    await channel.send(f"分からないことがあれば、`.help` をしてください。")

@client.event
async def on_message(message: discord.Message):
    
    if message.content.startswith(".dmg"):
        msg = message.content.split()
        dmg = float(msg[1])
        os = int(msg[2])
        tokkou = msg[3:]
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
            await message.channel.send(f"__**攻撃力：剣：-4%: {float(attack * 0.96):.3f}, 弓：-4%: {float(attack * 0.96):.3f}, 魔法：-4%: {float(attack * 0.96):.3f}**__")

        elif job == str('d'):
            await message.channel.send(f"__**攻撃力：剣：-2%: {float(attack * 0.98):.3f}, 弓：+5%: {float(attack * 1.05):.3f}, 魔法：-2%: {float(attack * 0.98):.3f}**__")

        elif job == str('p'):
            await message.channel.send(f"__**攻撃力：剣：-10%: {float(attack * 0.90):.3f}, 弓：-10%: {float(attack * 0.90):.3f}, 魔法：-10%: {float(attack * 0.90):.3f}**__")

        elif job == str('s'):
            await message.channel.send(f"__**攻撃力：剣：+5%: {float(attack * 1.05):.3f}, 弓：{float(attack):.3f}, 魔法：{float(attack):.3f}**__")

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
            job_4 == 'アーサー'
        elif str(job) == 'se':
            job_4 == 'シーカー'
        await message.channel.send(f"職業：{job_4}\nOS={os}\n特攻：{tokkou}")
        if job == str('h'):
            await message.channel.send(f"__**攻撃力：剣：-7%: {float(attack * 0.93):.3f}, 弓：-7%: {float(attack * 0.93):.3f}, 魔法：-7%: {float(attack * 0.93):.3f}**__")

        elif job == str('r'):
            await message.channel.send(f"__**攻撃力：剣：-7%: {float(attack * 0.93):.3f}, 弓：-7%: {float(attack * 0.93):.3f}, 魔法：+7%: {float(attack * 1.07):.3f}**__")

        elif job == str('sp'):
            await message.channel.send(f"__**攻撃力：剣：+10%: {float(attack * 1.10):.3f}, 弓：+10%: {float(attack * 1.10):.3f}, 魔法：+10%: {float(attack * 1.10):.3f}**__")

        elif job == str('a'):
            await message.channel.send(f"__**攻撃力：剣：+5%: {float(attack * 1.05):.3f}, 弓：{float(attack):.3f}, 魔法：{float(attack):.3f}**__")

        elif job == str('se'):
            await message.channel.send(f"__**攻撃力：剣：-7%: {float(attack * 0.93):.3f}, 弓：+10%: {float(attack * 1.10):.3f}, 魔法：-7%: {float(attack * 0.93):.3f}**__")

# キャスター計算
    if message.content.startswith(".cas"):
        cas = message.content.split()
        ct = int(cas[1])
        ct_p = int(cas[2])
        cas_stones = cas[3:]
        ct_perk = 1
        cas_stone = 1

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
        await message.channel.send(f"元のCT：{str(ct)}\nCTPerk：{str(ct_perk)}\n魔法石：{str(cas_stones)}\n__**CT：{cas_all}**__")

    if message.content.startswith(".ask"):
        msg = message.content.split()
        wantdmg = float(msg[1])
        dmg = msg[2]
        os= msg[3]
        tokkou=msg[4:]
        
        if dmg == '?': # Dmg不明
            dmg = 1.0
            os = int(os)
            os_power = osdict[os]
            attack = await tokkoulist(message, dmg, os_power, tokkou)
            dmg = wantdmg / attack
            await message.channel.send(f"OS：{os}の時\n{wantdmg}を出すには最低でも火力が__**{dmg:.3f}**__が必要です。")

        
        if os == '?': # OS不明
            dmg = float(msg[2])
            os_power = 1.0
            # os_power = await oslist(message, os)

            attack = await tokkoulist(message, dmg, os_power, tokkou)
            # os比較
            xOS = wantdmg / attack
            await message.channel.send(f"{xOS}倍")
            i = 1
            while xOS >= osdict[i]:
                i += 1
                if i >= len(osdict):
                    i = None
                    break
            if i == None:
                await message.channel.send(f"OSが61以上必要、又は不可能な値です。")
            else:
                await message.channel.send(f"{dmg}で{wantdmg}を出すには\n__**OSは{i}以上**__とってください。")  

    if message.content.startswith(".help1"):
        embed = discord.Embed(title="コマンド一覧", color=discord.Colour.gold())
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
        

        await message.channel.send(embed=embed)
    
    if message.content.startswith(".help2"):
        embed = discord.Embed(title="コマンド一覧", color=discord.Colour.lighter_gray())
        embed.add_field(
            name='キャスター', value='.cas [CT] [CTPerk] [魔法石(1 ~ 5)]', inline=False)
        embed.add_field(name='最低OSを求める場合', value='.ask [欲しい火力] [今の素ダメ] ? [魔法石]', inline=False)
        embed.add_field(name='最低火力を求める場合', value='.ask [欲しい火力] ? [OS] [魔法石]', inline=False)

        await message.channel.send(embed=embed)
    
client.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
