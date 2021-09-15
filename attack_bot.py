import discord

client = discord.Client()

async def calc(message, dmg, os, tokkou):
    # OS
    if os == 0:
        os_power = 1.0
    elif 60 >= os >= 1:
        if 1 <= os <= 9:
            os_power = 0.09 * os + 1.0
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 10:
            os_power = 2.02659
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 11:
            os_power = 2.15072
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 12:
            os_power = 2.22172
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 13:
            os_power = 2.26701
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 14:
            os_power = 2.29829
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 15:
            os_power = 2.32114
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 16:
            os_power = 2.33856
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 17:
            os_power = 2.35227
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 18:
            os_power = 2.36334
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 19:
            os_power = 2.37246
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 20:
            os_power = 2.38011
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 21:
            os_power = 2.38611
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 22:
            os_power = 2.39221
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 23:
            os_power = 2.39707
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 24:
            os_power = 2.40135
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 25:
            os_power = 2.40513
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 26:
            os_power = 2.40849
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 27:
            os_power = 2.41151
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 28:
            os_power = 2.41424
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 29:
            os_power = 2.4167
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 30:
            os_power = 2.41895
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 31:
            os_power = 2.421
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 32:
            os_power = 2.42289
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 33:
            os_power = 2.42462
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 34:
            os_power = 2.42623
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 35:
            os_power = 2.42772
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 36:
            os_power = 2.4291
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 37:
            os_power = 2.43039
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 38:
            os_power = 2.43159
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 39:
            os_power = 2.43272
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 40:
            os_power = 2.43377
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 41:
            os_power = 2.443476
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 42:
            os_power = 2.4357
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 43:
            os_power = 2.43658
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 44:
            os_power = 2.43742
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 45:
            os_power = 2.43821
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 46:
            os_power = 2.43895
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 47:
            os_power = 2.43966
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 48:
            os_power = 2.44034
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 49:
            os_power = 2.44098
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 50:
            os_power = 2.44159
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 51:
            os_power = 2.44217
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 52:
            os_power = 2.44273
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 53:
            os_power = 2.44326
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 54:
            os_power = 2.44377
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 55:
            os_power = 2.44426
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 56:
            os_power = 2.44473
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 57:
            os_power = 2.44518
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 58:
            os_power = 2.44561
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 59:
            os_power = 2.44602
            await message.channel.send(f"OS増加分：{os_power}倍")

        elif os == 60:
            os_power = 2.44642
            await message.channel.send(f"OS増加分：{os_power}倍")

    else:
        await message.channel.send(f"すみませんまだ作成中です")
        os_power = 1.0
        await message.channel.send(f"OS増加分：{os_power}倍")

        # 特攻
    if len(tokkou) == 0:
        dmg_all = dmg * os_power
        return dmg_all
        
    elif 1 <= len(tokkou) <= 5:
        tokkou_list = list(set(tokkou))
        tokkou_add = 1.0

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
                alpha= (dmg * 0.06)
                print(alpha)
                tokkou_add = 1.55 * alpha
                print(tokkou_add)
                
                #####
            alldmg = dmg * os_power * tokkou_add
            print(alldmg)
            return alldmg
    else:
        await message.channel.send(f"{message.author.mention}, 間違っています。")

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')


@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention},こんにちは")
    await channel.send(f"分からないことがあれば、`.help` をしてください。")


@client.event
async def on_message(message):
    if message.content.startswith(".dmg"):
        msg = message.content.split()
        dmg = float(msg[1])
        os = int(msg[2])
        tokkou = msg[3:]
        attack = await calc(message, dmg, os, tokkou)
        await message.channel.send(f"素火力：{dmg}\nOS={os} \n特攻：{tokkou} \n__**攻撃力：{attack:.3f}**__")


# ソルジャー・アーサー・マジシャン
    if message.content.startswith(".job1"):
        msg_job = message.content.split()
        job = str(msg_job[1]) # 職業
        dmg = float(msg_job[2])
        os = int(msg_job[3])
        tokkou = msg_job[4:]
        job_1 = ''
        attack =await calc(message, dmg, os, tokkou)
        print(attack)
        print(type(attack))
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
        attack = await calc(message, dmg, os, tokkou)
        print(attack)
        print(type(attack))
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
        attack = await calc(message, dmg, os, tokkou)
        print(attack)
        print(type(attack))
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
        attack = await calc(message, dmg, os, tokkou)
        print(attack)
        print(type(attack))
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

    
    if message.content.startswith(".help"):
        embed = discord.Embed(title="コマンド一覧", color=discord.Colour.blue())
        embed.add_field(name='ヘルプ', value='.help', inline=False)
        embed.add_field(name='ダメージ計算', value='.dmg [攻撃力] [OS] [魔法石(1~5, ただし4_5, 5, LEGは重複不可)]', inline=False)
        embed.add_field(name='職業込みでのダメージ計算', value='.job(1~4) [職業] [攻撃力] [OS] [魔法石(1~5, ただし4_5と5は重複不可)]', inline=False)
        embed.add_field(name='職業[.job1]について', value='ソルジャー:s, アーチャー:a, マジシャン:m', inline=False)
        embed.add_field(name='職業[.job2]について', value='ウォーリア:w, ボウマン:b, メイジ:m', inline=False)
        embed.add_field(name='職業[.job3]について', value='ロウニン:r, ドラゴンキラー:d, プリースト:p, スカーミッシャー:s', inline=False)
        embed.add_field(
            name='職業[.job4]について', value='ハグレモノ:h, ルーンキャスター:r, スペランカー:sp, アーサー:a, シーカー:se', inline=False)
        embed.add_field(name='キャスター', value='.cas [CT] [CTPerk] [魔法石(1 ~ 5)]', inline=False)

        await message.channel.send(embed=embed)
    
client.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
