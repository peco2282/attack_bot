import discord

client = discord.Client()


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
        tokkou_add = 1
        msg=message.content.split()
        dmg=float(msg[1])
        os=int(msg[2])
        tokkou=msg[3:]
        await message.channel.send(f"OS={os}")
        await message.channel.send(f"特攻：{tokkou}")
        if os == 0:
            os_power = 1.0
        elif 13 >=os >= 1:
            if 1 <= os <= 9:
                os_power =  0.09 * os + 1.0
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

        elif os >= 27:
            await message.channel.send(f"すみませんまだ作成中です")
            os_power = 1.0
            await message.channel.send(f"OS増加分：{os_power}倍")
            
            #####
        else:
            print("a")

        if len(tokkou) == 0:
            print("0")
            dmg_all = dmg * os_power
            await message.channel.send(f"__**攻撃力：{dmg_all}**__")

        elif 1 <= len(tokkou) <= 5:
            tokkou_list = list(set(tokkou))
            print(len(tokkou))
            
            if len(tokkou) != len(tokkou_list):
                print("$")
                await message.channel.send(f"{message.author.mention}, 重複しています。")
            
            elif (str("4_5") in tokkou)  and (str("5") in tokkou):
                await message.channel.send("4_5と5は同時に装着できません")

            else:    
                if str('1') in tokkou:
                    tokkou_add *= 1.1
                
                if str('2') in tokkou:
                    tokkou_add *= 1.15
                
                if str('3') in tokkou:
                    tokkou_add *= 1.23
                                    
                if str('4') in tokkou:
                    tokkou_add *= 1.35
                
                if str('4_5') in tokkou:
                    tokkou_add *= 1.40
                
                if str('5') in tokkou:
                    tokkou_add *= 1.55
                
                #####
                alldmg = dmg * os_power * tokkou_add
                print(alldmg)
                await message.channel.send(f"攻撃力：{alldmg}")
        else:
            await message.channel.send(f"{message.author.mention}, 間違っています。")

        
        
    if message.content.startswith(".help"):
        embed = discord.Embed(title="コマンド一覧", color=discord.Colour.blue())
        embed.add_field(name='ダメージ計算', value='.dmg [攻撃力] [OS] [魔法石(1~5, ただし4_5と5は重複不可)]', inline=False)
        embed.add_field(name='ヘルプ', value='.help', inline=False)
        await message.channel.send(embed=embed)

client.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
