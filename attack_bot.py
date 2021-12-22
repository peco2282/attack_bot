import asyncio
import random
from datetime import datetime
from math import ceil

import nextcord as discord
import pytz

from nextcord.ext import commands

from definition import tokkoulist
from dictionaries import osdict, castimedict, dict_1, dict_2, dict_3, dict_4, dict_5

intents = discord.Intents.all()
now = datetime.now(pytz.timezone('Asia/Tokyo'))

bot = commands.Bot(command_prefix='.', help_command=None, intents=intents)

url = "https://discord.com/api/v8/applications/886486207394099220/commands"

emoji_selector = u'\U0000fe0f\U000020e3'
emoji_1 = u'\N{DIGIT ONE}' + emoji_selector
emoji_2 = u'\N{DIGIT TWO}' + emoji_selector  # 2⃣
emoji_3 = u'\N{DIGIT THREE}' + emoji_selector  # 3⃣
emoji_4 = u'\N{DIGIT FOUR}' + emoji_selector
emoji_5 = u'\N{DIGIT FIVE}' + emoji_selector
emoji_6 = u'\N{DIGIT SIX}' + emoji_selector
emoji_7 = u'\N{DIGIT SEVEN}' + emoji_selector
emoji_8 = u'\N{DIGIT EIGHT}' + emoji_selector
emoji_9 = u'\N{DIGIT NINE}' + emoji_selector


async def rand_ints_nodup(x, k):
    ns = []
    while len(ns) < k:
        n = random.randrange(x)
        if not n in ns:
            ns.append(n)
    return ns


# ---------------

@bot.event
async def on_ready():
    print('Logged in as: ' + bot.user.name + ', With ID:' + str(bot.user.id))
    print('Ver.:' + discord.__version__)
    channelid = 886185192530780160
    channelid_2 = 886495611728302091
    for channel in bot.get_all_channels():
        if (channel.id == channelid) or (channel.id == channelid_2):
            await channel.send(f"On Ready : {now}")

    if len(bot.guilds) >= 100:
        await bot.change_presence(activity=discord.Game(name='.help | ' + str(len(bot.guilds)) + 'guilds'))


@bot.event
async def on_message_delete(message):
    print(message)


@bot.event
async def on_guild_join(guild):
    print("!!!!")
    channelid = 886185192530780160
    channelid_2 = 886495611728302091
    for channel in bot.get_all_channels():
        if (channel.id == channelid) or (channel.id == channelid_2):
            await channel.send(guild)


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.user_id == bot.user.id:
        return

    # if the reacted message is the bot's
    # and the person who reacted is the person who typed the command
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if message.author == bot.user:
        if str(payload.emoji) in ('🚮', '✖️', '🗑️'):
            await message.delete()


@bot.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    print(reaction, user)


# ---------------


@bot.command(aliases=['?', 'h'])
async def help(ctx: commands.context):
    embed = discord.Embed(title="コマンド一覧", color=discord.Colour.gold(), timestamp=now)
    embed.set_author(name=ctx.author.name)
    embed.add_field(name='ヘルプ', value='.help', inline=False)
    embed.add_field(
        name='ダメージ計算', value='.dmg [攻撃力] [OS] [魔法石(1~5, ただし4_5, 5, LEGは重複不可)]', inline=False)
    embed.add_field(
        name='職業込みでのダメージ計算', value='.job [攻撃力] [OS] [魔法石(1~5, ただし4_5と5は重複不可)]', inline=False)
    embed.add_field(
        name='キャスター', value='.cas [CT] [CTPerk] [魔法石(1 ~ 5)]', inline=False)
    embed.add_field(name='最低OSを求める場合', value='.ask [欲しい火力] [今の素ダメ] ? [魔法石]', inline=False)
    embed.add_field(name='最低火力を求める場合', value='.ask [欲しい火力] ? [OS] [魔法石]', inline=False)
    embed.add_field(name='おすすめ魔法石', value='.magicstone (又は\'ms\') [欲しいダメージ] [素火力] [OS] [スロット数]', inline=False)
    embed.add_field(name='招待リンク', value='.inv', inline=False)

    sent_message = await ctx.send(embed=embed)
    await sent_message.add_reaction('🚮')

    while True:
        try:
            await bot.wait_for(event='reaction_add', timeout=20)

        except asyncio.TimeoutError:
            await sent_message.clear_reactions()
            break


@bot.command(aliases=['inv'])
async def invite(ctx: commands.context):
    inv_link = discord.utils.oauth_url(client_id=914669244178907176) + '&permissions=8'
    await ctx.send(inv_link)


@bot.command()
async def member(ctx: commands.context):
    # message インスタンスから guild インスタンスを取得
    guild = ctx.guild

    # ユーザとBOTを区別しない場合
    member_count = guild.member_count
    await ctx.send(f'メンバー数：{member_count}')


@bot.command()
async def guild(ctx: commands.context):
    await ctx.send("I'm in " + str(len(bot.guilds)) + " servers!")


@bot.command(aliases=['glist'])
async def guildlist(ctx: commands.context):
    i = 1
    embed = discord.Embed(title="Glist", color=discord.Colour.gold(), timestamp=now)
    async for guild in bot.fetch_guilds():
        embed.add_field(name=i, value=f'**`{guild.name}`**', inline=False)
        i += 1

    await ctx.send(embed=embed)


@bot.command(aliases=['rep'])
async def report(ctx, *kargs):
    list_a = []
    channelid = 886185192530780160
    channelid_2 = 912911804710150195
    await ctx.send(type(kargs))
    kargs_a = list(kargs)
    await ctx.send(f'{kargs_a[2]}')
    for i in kargs:
        list_a.append(i)

        await ctx.send(i)
    for channel in bot.get_all_channels():
        if (channel.id == channelid) or (channel.id == channelid_2):
            await channel.send('  /report/  \n```\n' + str(kargs) + f'\n```\non :{now}')


@bot.command()
async def channel(ctx):
    k = 1
    a = len(list(bot.get_all_channels()))
    embed = discord.Embed(title="チャンネル一覧", color=discord.Colour.gold(), timestamp=now)
    embed.add_field(name='チャンネル数', value=a, inline=False)
    for i in bot.get_all_channels():
        embed.add_field(name=k, value=f'**`{i}`**')
        k += 1
    sent_message = await ctx.send(embed=embed)
    await sent_message.add_reaction('🚮')

    while True:
        try:
            await bot.wait_for(event='reaction_add', timeout=20)

        except asyncio.TimeoutError:
            await sent_message.clear_reactions()
            break


@bot.command()
async def dmg(ctx: commands.Context, *args):
    # ダメージ・OS・魔法石
    print(type(ctx), type(args))
    dmg = float(args[0])
    os = int(args[1])
    tokkou_dmg = args[2:]
    tokkou = args[2:]
    try:
        if os > len(osdict):
            await ctx.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
            os_power = 1

        else:
            os_power = osdict[os]

        attack, tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)
        print(os_power, attack, tokkou)
        sent_message = await ctx.send(f"**By：{ctx.author.name}**\n\n素火力 : {dmg}\nOS : {os}\n"
                                      f"OS倍率 : {os_power} 倍\n魔法石：{tokkou_dmg}\n魔法石倍率：{tokkou_add}倍\n"
                                      f"__**攻撃力 : {attack:.5f}\n**__")
        await sent_message.add_reaction('🚮')

        while True:
            try:
                await bot.wait_for(event='reaction_add', timeout=20)

            except asyncio.TimeoutError:
                await sent_message.clear_reactions()
                break


    except:
        await ctx.send(f':thinking: {ctx.author.mention}\n'
                       f'`.dmg [攻撃力] [OS] (魔法石)`の順に入力してください。')

        
@bot.command(aliases=['ms'])
async def magicstone(ctx: commands.Context, *args):
    try:
        args = list(args)
        wantdmg = float(args[0])
        nowdmg = float(args[1])
        os = int(args[2])
        magicstoneslot = int(args[3])
        osadd = osdict[os]

        s = wantdmg / (nowdmg * osadd)
        ms = list()
        x = 0
        i = 1
        if magicstoneslot == 1:
            if s > 1.55:
                await ctx.send('Index out of range!\nスロットが足りません。')
                return
            for i in dict_1:
                if dict_1[i] > s:
                    await ctx.send(f'条件：\n魔法石付けた後の欲しいダメージ：{wantdmg}\n今の素火力：{nowdmg}\nOS：{os}\n魔法石スロット：1\n\n**結果：{i}**')



        elif magicstoneslot == 2:
            if s > (1.35 * 1.55):
                await ctx.send('Index out of range!!\nスロットが足りません。')
                return
            for y in dict_2:
                n = dict_2[y]
                if n > s:
                    await ctx.send(f'条件：\n魔法石付けた後の欲しいダメージ：{wantdmg}\n今の素火力：{nowdmg}\nOS：{os}\n魔法石スロット：2\n\n**結果：{y}**')
                    return

        elif magicstoneslot == 3:
            if s > (1.23 * 1.35 * 1.55):
                await ctx.send('Index out of range!!!\nスロットが足りません。')
                return
            for y in dict_3:
                n = dict_3[y]
                if n > s:
                    await ctx.send(f'条件：\n魔法石付けた後の欲しいダメージ：{wantdmg}\n今の素火力：{nowdmg}\nOS：{os}\n魔法石スロット：3\n\n**結果：{y}**')
                    return

        elif magicstoneslot == 4:
            if s > (1.55 * 1.23 * 1.35 * 1.55):
                await ctx.send('Index out of range!!!!\nスロットが足りません。')
                return
            for y in dict_4:
                n = dict_4[y]
                if n > s:
                    await ctx.send(f'条件：\n魔法石付けた後の欲しいダメージ：{wantdmg}\n今の素火力：{nowdmg}\nOS：{os}\n魔法石スロット：4\n\n**結果：{y}**')
                    return

        elif magicstoneslot == 5:
            if s > (1.10 * 1.15 * 1.23 * 1.35 * 1.55):
                await ctx.send('Index out of range!!!!!\nスロットが足りません。')
                return
            for y in dict_5:
                n = dict_5[y]
                if n > s:
                    await ctx.send(f'条件：\n魔法石付けた後の欲しいダメージ：{wantdmg}\n今の素火力：{nowdmg}\nOS：{os}\n魔法石スロット：5\n\n**結果：{y}**')
                    return
    except:
        await ctx.send('`.magicstone (又は\'ms\') 欲しいダメージ 素火力 OS スロット数`')


# 職業
@bot.command()
async def job(ctx, *args):
    try:
        dmg = float(args[0])
        os = int(args[1])
        raw_tokkou = args[2:]
        tokkou = args[2:]
        os_power = 1.0
        os_raw_power = osdict[os]
        attack, tokkou_dmg = await tokkoulist(ctx, dmg, os_power, tokkou)

        embed_1_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
        embed_1_job.set_author(name=f"By {ctx.author}")

        embed_1_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n'
                                               f'魔法石： {raw_tokkou}\n魔法石倍率： {tokkou_dmg}倍')
        embed_1_job.add_field(name='ソルジャー', value=f'__**攻撃力：剣：+5%: {float(attack * (os_raw_power + 0.05)):.3f},'
                                                  f' 弓：-2%: {float(attack * (os_raw_power - 0.02)):.3f},'
                                                  f' 魔法：-2%: {float(attack * (os_raw_power - 0.02)):.3f}**__',
                              inline=False)

        embed_1_job.add_field(name='アーチャー', value=f"__**攻撃力：剣：-2%: {float(attack * (os_raw_power - 0.02)):.3f},"
                                                  f" 弓：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                  f" 魔法：-2%: {float(attack * (os_raw_power - 0.02)):.3f}**__",
                              inline=False)

        embed_1_job.add_field(name='マジシャン', value=f"__**攻撃力：剣：-2%: {float(attack * (os_raw_power - 0.02)):.3f},"
                                                  f" 弓：-2%: {float(attack * (os_raw_power - 0.02)):.3f},"
                                                  f" 魔法：+5%: {float(attack * (os_raw_power + 0.05)):.3f}**__",
                              inline=False)

        embed_1_job.set_footer(text='Page 1 of 4')

        embed_2_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

        embed_2_job.set_author(name=f"By {ctx.author}")
        embed_2_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n魔法石： {raw_tokkou}'
                                               f'\n魔法石倍率： {tokkou_dmg}倍')

        embed_2_job.add_field(name='ウォーリア', value=f"__**攻撃力：剣：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                  f" 弓： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                  f" 魔法： -5%: {float(attack * (os_raw_power - 0.05)):.3f}**__",
                              inline=False)

        embed_2_job.add_field(name='ボウマン', value=f"__**攻撃力：剣： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                 f" 弓：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                 f" 魔法： -5%: {float(attack * (os_raw_power - 0.05)):.3f}**__",
                              inline=False)

        embed_2_job.add_field(name='メイジ', value=f"__**攻撃力：剣： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                f" 弓： -5%: {float(attack * (os_raw_power - 0.05)):.3f},"
                                                f" 魔法：+10: {float(attack * (os_raw_power + 0.10)):.3f}**__",
                              inline=False)

        embed_2_job.set_footer(text='Page 2 of 4')

        embed_3_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

        embed_3_job.set_author(name=f"By {ctx.author}")
        embed_3_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n魔法石： {raw_tokkou}\n'
                                               f'魔法石倍率： {tokkou_dmg}倍')
        embed_3_job.add_field(name='ロウニン', value=f"__**攻撃力：剣：-4%: {float(attack * (os_raw_power - 0.04)):.3f},"
                                                 f" 弓：-4%: {float(attack * (os_raw_power - 0.04)):.3f},"
                                                 f" 魔法：-4%: {float(attack * (os_raw_power - 0.04)):.3f}**__",
                              inline=False)

        embed_3_job.add_field(name='ドラゴンキラー', value=f"__**攻撃力：剣：-2%: {float(attack * (os_raw_power - 0.02)):.3f}, "
                                                    f" 弓：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                    f" 魔法：-2%: {float(attack * (os_raw_power - 0.02)):.3f}**__",
                              inline=False)

        embed_3_job.add_field(name='プリースト', value=f"__**攻撃力：剣：-10%: {float(attack * (os_raw_power - 0.10)):.3f},"
                                                  f" 弓：-10%: {float(attack * (os_raw_power - 0.10)):.3f},"
                                                  f" 魔法：-10%: {float(attack * (os_raw_power - 0.10)):.3f}**__",
                              inline=False)

        embed_3_job.add_field(name='スカーミッシャー', value=f"__**攻撃力：剣：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                     f" 弓：{float(attack):.3f},"
                                                     f" 魔法：{float(attack):.3f}**__", inline=False)

        embed_3_job.set_footer(text='Page 3 of 4')

        embed_4_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

        embed_4_job.set_author(name=f"By {ctx.author}")
        embed_4_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n魔法石： {raw_tokkou}\n'
                                               f'魔法石倍率： {tokkou_dmg}倍')

        embed_4_job.add_field(name='ハグレモノ', value=f"__**攻撃力：剣：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                  f" 弓：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                  f" 魔法：-7%: {float(attack * (os_raw_power - 0.07)):.3f}**__",
                              inline=False)

        embed_4_job.add_field(name='ルーンキャスター', value=f"__**攻撃力：剣：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                     f" 弓：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                     f" 魔法：+7%: {float(attack * (os_raw_power + 0.07)):.3f}**__",
                              inline=False)

        embed_4_job.add_field(name='スペランカー', value=f"__**攻撃力：剣：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                   f"  弓：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                   f" 魔法：+10%: {float(attack * (os_raw_power + 0.10)):.3f}**__",
                              inline=False)

        embed_4_job.add_field(name='アーサー', value=f"__**攻撃力：剣：+5%: {float(attack * (os_raw_power + 0.05)):.3f},"
                                                 f" 弓：{float(attack):.3f},"
                                                 f" 魔法：{float(attack):.3f}**__", inline=False)

        embed_4_job.add_field(name='シーカー', value=f"__**攻撃力：剣：-7%: {float(attack * (os_raw_power - 0.07)):.3f},"
                                                 f" 弓：+10%: {float(attack * (os_raw_power + 0.10)):.3f},"
                                                 f" 魔法：-7%: {float(attack * (os_raw_power - 0.07)):.3f}**__",
                              inline=False)

        embed_4_job.set_footer(text='Page 4 of 4')

        sent_message = await ctx.send(embed=embed_1_job)

        emoji_list = ['⏪', '⏩']
        page = 0
        embed_list = [embed_1_job, embed_2_job, embed_3_job, embed_4_job]

        for add_emoji in emoji_list:
            await sent_message.add_reaction(add_emoji)

        # リアクションチェック用の関数
        def check(reaction, user):
            # botを呼び出した本人からのリアクションのみ受け付ける
            # reaction.message == ctx を入れないと複数出したときに全て連動して動いてしまう
            return user == ctx.author and reaction.message == sent_message and str(reaction.emoji) in emoji_list

        while True:
            try:
                # リアクションが付けられるまで待機
                reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)

            except asyncio.TimeoutError:
                # 一定時間経ったら消す
                # for remove_emoji in emoji_list:
                # await sent_message.remove_reaction(emoji=remove_emoji, member=bot.user)
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
                await sent_message.remove_reaction(reaction.emoji, ctx.author)

    except:
        await ctx.send(f':thinking: {ctx.author.mention}\n'
                       f'`.job [攻撃力] [OS] (魔法石)`の順に入力してください。')


@bot.command()
async def ask(ctx: commands.Context, *args):
    try:
        want_dmg = float(args[0])
        now_dmg = args[1]
        str_os = args[2]
        tokkou = args[3:]

        if now_dmg == '?':
            print("A")
            dmg = 1.0
            os = int(str_os)
            os_power = osdict[os]
            attack, tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)
            ans_dmg = want_dmg / attack
            sent_message = await ctx.send(f"OS：{os}の時\n{want_dmg}を出すには最低でも火力が__**{ceil(ans_dmg)}**__が必要です。")
            await sent_message.add_reaction('🚮')
            while True:
                try:
                    await bot.wait_for(event='reaction_add', timeout=20)

                except asyncio.TimeoutError:
                    await sent_message.clear_reactions()
                    break

        if str_os == '?':
            print("W")
            dmg = float(args[1])
            os_power = 1.0
            attack, tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)
            print(dmg, type(dmg))
            print(want_dmg, type(want_dmg))
            print(attack, type(attack))

            xos = float(want_dmg / attack)
            print("R")
            i = 0
            print({xos}, {i})
            print(len(osdict))

            if xos > osdict[len(osdict)-1]:
                sent_message = await ctx.send("OSを積んでもその攻撃力は出せません。")

            else:
                while xos >= osdict[i]:
                    if i > len(osdict):
                        i = 'miss'
                        return i
                    i += 1

                if xos < osdict[0]:
                    sent_message = await ctx.send('OSを積む必要はありません。')

                if i == 'miss':
                    sent_message = await ctx.send(f"OSが{len(osdict)}以上必要、又は不可能な値です。")

                else:
                    sent_message = await ctx.send(f"{dmg}で{want_dmg}を出すには\n__**OSは{i}以上**__とってください。")

            await sent_message.add_reaction('🚮')

            while True:
                try:
                    await bot.wait_for(event='reaction_add', timeout=20)

                except asyncio.TimeoutError:
                    await sent_message.clear_reactions()
                    break

    except:
        await ctx.send(f":thinking: {ctx.author.mention}, `.ask [欲しい火力] [今の素ダメ] '?' (魔法石)`\n"
                       f"又は　`.ask [欲しい火力] '?' [今のOS] (魔法石)`\n"
                       f"と入力してください。")


@bot.command()
async def cas(ctx, *args):
    xct = 1.0
    try:
        cas_time = float(args[0])
        cas_perk = int(args[1])
        cas_stone_1 = str(args[2:])
        cas_stone_2 = list(set(cas_stone_1))

        ct_perk = castimedict[cas_perk]

        if 'leg' in cas_stone_2:
            await ctx.send(f'{ctx.author}、キャスター石に\'leg\'はありません。')

        if '4.5' in cas_stone_2:
            cas_stone_2.remove("4.5")
            cas_stone_2.append("4_5")

        if ('4_5' in cas_stone_2) and ('4.5' in cas_stone_2):
            await ctx.send(f":thinking: {ctx.author.mention}, 魔法石`4_5 と 4.5` は同じです。")

        if '1' in cas_stone_2:
            xct *= 0.95
            cas_stone_2.remove('1')

        if '2' in cas_stone_2:
            xct *= 0.90
            cas_stone_2.remove('2')

        if '3' in cas_stone_2:
            xct *= 0.84
            cas_stone_2.remove('3')

        if '4' in cas_stone_2:
            xct *= 0.77
            cas_stone_2.remove('4')

        if '4_5' in cas_stone_2:
            xct *= 0.72
            cas_stone_2.remove('4_5')

        if '5' in cas_stone_2:
            xct *= 0.60
            cas_stone_2.remove('5')

        ct = cas_time * ct_perk * xct
        sent_message = await ctx.send(f'元のCT : {cas_time}\nCTPrk : {cas_perk}\n'
                                      f'魔法石 : {cas_stone_1}\n魔法石倍率 ： {xct}倍\n'
                                      f'__**最終的なCT : {ct}**__')

        await sent_message.add_reaction('🚮')

        while True:
            try:
                await bot.wait_for(event='reaction_add', timeout=20)

            except asyncio.TimeoutError:
                await sent_message.clear_reactions()
                break

    except:
        await ctx.send(f':thinking: {ctx.author.mention}, `.cas [元のCT] [CTPerk (0~10)] (魔法石)`')


@bot.command()
async def skill(ctx):
    embed = discord.Embed(title='`.skill` 使い方', timestamp=now)
    embed.set_author(name=ctx.author)
    embed.add_field(name='**`.skill1`**', value=f'{emoji_1}：`ノービス`\n'
                                                f'{emoji_2}：`ソルジャー`\n'
                                                f'{emoji_3}：`アーチャー`\n'
                                                f'{emoji_4}：`マジシャン` \n'
                                                f'{emoji_5}：`ウォーリア`\n'
                                                f'{emoji_6}：`ボウマン`\n'
                                                f'{emoji_7}：`メイジ`',
                    inline=False)

    embed.add_field(name='**`.skill2`**', value=f'{emoji_1}：`ロウニン`\n'
                                                f'{emoji_2}：`ドラゴンキラー`\n'
                                                f'{emoji_3}：`プリースト`\n'
                                                f'{emoji_4}：`スカ―ミッシャー`\n'
                                                f'{emoji_5}：`ハグレモノ`\n'
                                                f'{emoji_6}：`ルーンキャスター`\n'
                                                f'{emoji_7}：`スペランカー`\n'
                                                f'{emoji_8}：`アーサー`\n'
                                                f'{emoji_9}：`シーカー`',
                    inline=False)
    sent_message = await ctx.send(embed=embed)

    while True:
        try:
            await bot.wait_for(event='reaction_add', timeout=20)

        except asyncio.TimeoutError:
            await sent_message.clear_reactions()
            break


# リスト位置変更！！！
@bot.command()
async def skill1(ctx, *args):
    try:
        dmg = float(args[0])
        skill_dmg = float(args[0])

        os = int(args[1])
        skill_os = int(args[1])

        skill_tokkou = args[2:]
        tokkou = args[2:]

        skill_os_power = osdict[os]
        os_power = 1.0

        print(os_power)
        skill_attack, skill_tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)

        # ノービス
        embed_1 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：ノービス**")

        embed_1.set_author(name=ctx.author.name)

        embed_1.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_1.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * skill_os_power:.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * skill_os_power:.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * skill_os_power:.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * skill_os_power:.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_1.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * skill_os_power:.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * skill_os_power:.3f}__**', inline=False)

        embed_1.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * skill_os_power:.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * skill_os_power:.3f}__**', inline=False)

        embed_1.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * skill_os_power:.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * skill_os_power:.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * skill_os_power:.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * skill_os_power:.3f}__**',
                          inline=False)

        embed_1.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * skill_os_power:.3f}__**', inline=False)

        embed_1.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * skill_os_power:.3f}**__')

        embed_1.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * skill_os_power:.3f} / 通常mob {skill_attack * 0.7 * skill_os_power:.3f}__**',
                          inline=False)

        # ソルジャー
        embed_2 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：ソルジャー**")

        embed_2.set_author(name=ctx.author.name)

        embed_2.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_2.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * 0.98 * (skill_os_power - 0.02):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.02):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * 0.98 * (skill_os_power - 0.02):.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_2.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.05):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.05):.3f}__**',
                          inline=False)

        embed_2.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.02):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_2.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.02):.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power - 0.02):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.02):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_2.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power + 0.05):.3f}__**',
                          inline=False)

        embed_2.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.02):.3f}**__')

        embed_2.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power + 0.05):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power + 0.05):.3f}__**',
                          inline=False)

        # アーチャー
        embed_3 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：アーチャー**")

        embed_3.set_author(name=ctx.author.name)

        embed_3.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_3.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.02):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.02):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power - 0.02):.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_3.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.02):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_3.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.05):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.05):.3f}__**',
                          inline=False)

        embed_3.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power + 0.05):.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power + 0.05):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power + 0.05):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power + 0.05):.3f}__**',
                          inline=False)

        embed_3.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_3.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power + 0.05):.3f}**__')

        embed_3.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.02):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        # マジシャン
        embed_4 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：マジシャン**")

        embed_4.set_author(name=ctx.author.name)

        embed_4.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_4.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power + 0.05):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power + 0.05):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power + 0.05):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power + 0.05):.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_4.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.02):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_4.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.02):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_4.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.02):.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power - 0.02):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.02):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_4.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_4.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.02):.3f}**__')

        embed_4.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.02):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        # ウォーリア
        embed_5 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：ウォーリア**")

        embed_5.set_author(name=ctx.author.name)

        embed_5.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_5.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.05):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.05):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.05):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power - 0.05):.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_5.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.10):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.10):.3f}__**',
                          inline=False)

        embed_5.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.05):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_5.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.05):.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power - 0.05):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.05):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_5.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power + 0.10):.3f}__**',
                          inline=False)

        embed_5.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.05):.3f}**__')

        embed_5.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power + 0.10):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power + 0.10):.3f}__**',
                          inline=False)

        # ボウマン
        embed_6 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：ボウマン**")

        embed_6.set_author(name=ctx.author.name)

        embed_6.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}魔法石倍率：{skill_tokkou_add}倍')

        embed_6.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.05):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.05):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.05):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power - 0.05):.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_6.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.05):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_6.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.10):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.10):.3f}__**',
                          inline=False)

        embed_6.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power + 0.10):.3f}__, パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power + 0.10):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power + 0.10):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power + 0.10):.3f}__**',
                          inline=False)

        embed_6.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_6.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power + 0.10):.3f}**__')

        embed_6.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.05):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        # メイジ
        embed_7 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：メイジ**")

        embed_7.set_author(name=ctx.author.name)

        embed_7.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_7.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power + 0.10):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power + 0.10):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power + 0.10):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power + 0.10):.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_7.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.05):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_7.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.05):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_7.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.05):.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power - 0.05):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.05):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_7.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        embed_7.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.05):.3f}**__')

        embed_7.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.05):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.05):.3f}__**',
                          inline=False)

        emoji_list_1 = [emoji_1, emoji_2, emoji_3, emoji_4, emoji_5, emoji_6, emoji_7]
        sent_message = await ctx.send(embed=embed_1)
        for emoji in emoji_list_1:
            await sent_message.add_reaction(emoji=emoji)

        # リアクションチェック用の関数
        def check(reaction, user):
            # botを呼び出した本人からのリアクションのみ受け付ける
            # reaction.message == msg を入れないと複数出したときに全て連動して動いてしまう
            return user == ctx.author and reaction.message == sent_message and str(
                reaction.emoji) in emoji_list_1

        while True:
            try:
                # リアクションが付けられるまで待機
                reaction, user = await bot.wait_for('reaction_add', timeout=40.0, check=check)

            except asyncio.TimeoutError:
                # 一定時間経ったら消す
                # for remove_emoji in emoji_list:
                # await sent_message.remove_reaction(emoji=remove_emoji, member=bot.user)
                await sent_message.clear_reactions()
                break

            else:
                # 付けられたリアクションに対応した処理を行う
                if str(reaction.emoji) == (emoji_list_1[0]):
                    await sent_message.edit(embed=embed_1)

                if str(reaction.emoji) == (emoji_list_1[1]):
                    await sent_message.edit(embed=embed_2)

                if str(reaction.emoji) == (emoji_list_1[2]):
                    await sent_message.edit(embed=embed_3)

                if str(reaction.emoji) == (emoji_list_1[3]):
                    await sent_message.edit(embed=embed_4)

                if str(reaction.emoji) == (emoji_list_1[4]):
                    await sent_message.edit(embed=embed_5)

                if str(reaction.emoji) == (emoji_list_1[5]):
                    await sent_message.edit(embed=embed_6)

                if str(reaction.emoji) == (emoji_list_1[6]):
                    await sent_message.edit(embed=embed_7)

                # リアクションをもう一度押せるように消しておく
                await sent_message.remove_reaction(reaction.emoji, ctx.author)

    except:
        await ctx.send(f':thinking: {ctx.author.mention},`.skill1 [総ダメージ] [OS] (魔法石)`')


@bot.command()
async def skill2(ctx, *args):
    try:
        dmg = float(args[0])
        skill_dmg = float(args[0])

        os = int(args[1])
        skill_os = int(args[1])

        skill_tokkou = args[2:]
        tokkou = args[2:]

        skill_os_power = osdict[os]
        os_power = 1.0

        print(os_power)
        skill_attack, skill_tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)

        # ロウニン
        embed_8 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：ロウニン**")

        embed_8.set_author(name=ctx.author.name)

        embed_8.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_8.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.04):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.04):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.04):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * skill_os_power:.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_8.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.04):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.04):.3f}__**',
                          inline=False)

        embed_8.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.04):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.04):.3f}__**',
                          inline=False)

        embed_8.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.04):.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power - 0.04):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.04):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.04):.3f}__**',
                          inline=False)

        embed_8.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.04):.3f}__**',
                          inline=False)

        embed_8.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.04):.3f}**__')

        embed_8.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.04):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.04):.3f}__**',
                          inline=False)

        # ドラゴンキラー
        embed_9 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                description=f"**職業：ドラゴンキラー**")

        embed_9.set_author(name=ctx.author.name)

        embed_9.add_field(name='条件',
                          value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_9.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                          value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.02):.3f}__**\n'
                                f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**, '
                                f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.02):.3f}__**)'
                                f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power - 0.02):.3f}__**\n'
                                f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                          inline=False)

        embed_9.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                          value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.02):.3f}__**'
                                f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_9.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                          value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.05):.3f}__**'
                                f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * skill_os_power:.3f}__**', inline=False)

        embed_9.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                          value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power + 0.05):.3f}__, '
                                f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power + 0.05):.3f}__**'
                                f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power + 0.05):.3f}__**'
                                f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power + 0.05):.3f}__**',
                          inline=False)

        embed_9.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                          value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        embed_9.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                          value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power + 0.05):.3f}**__')

        embed_9.add_field(name='**聖剣 (In 浮世の砂海)**',
                          value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.02):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.02):.3f}__**',
                          inline=False)

        # プリースト
        embed_10 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                 url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                 description=f"**職業：プリースト**")

        embed_10.set_author(name=ctx.author.name)

        embed_10.add_field(name='条件',
                           value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_10.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                           value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.10):.3f}__**\n'
                                 f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.10):.3f}__**, '
                                 f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.10):.3f}__**)'
                                 f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power - 0.10):.3f}__**\n'
                                 f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                           inline=False)

        embed_10.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                           value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.10):.3f}__**'
                                 f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.10):.3f}__**',
                           inline=False)

        embed_10.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                           value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.10):.3f}__**'
                                 f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.10):.3f}__**',
                           inline=False)

        embed_10.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                           value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.10):.3f}__, '
                                 f'パッシブあり：__{skill_attack * 12.5 * 1.5 * skill_os_power:.3f}__**'
                                 f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.10):.3f}__**'
                                 f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.10):.3f}__**',
                           inline=False)

        embed_10.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                           value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.10):.3f}__**',
                           inline=False)

        embed_10.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                           value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.10):.3f}**__')

        embed_10.add_field(name='**聖剣 (In 浮世の砂海)**',
                           value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.10):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.10):.3f}__**',
                           inline=False)

        # スカ―ミッシャー
        embed_11 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                 url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                 description=f"**職業：スカ―ミッシャー**")

        embed_11.set_author(name=ctx.author.name)

        embed_11.add_field(name='条件',
                           value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_11.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                           value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * skill_os_power:.3f}__**\n'
                                 f'マジックボール (ノーマル)**：__{skill_attack * 4 * skill_os_power:.3f}__**, '
                                 f'**(詠唱時：__{skill_attack * 8 * skill_os_power:.3f}__**)'
                                 f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * skill_os_power:.3f}__**\n'
                                 f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                           inline=False)

        embed_11.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                           value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.05):.3f}__**'
                                 f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.05):.3f}__**',
                           inline=False)

        embed_11.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                           value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * skill_os_power:.3f}__**'
                                 f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * skill_os_power:.3f}__**', inline=False)

        embed_11.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                           value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * skill_os_power:.3f}__, '
                                 f'パッシブあり：__{skill_attack * 12.5 * 1.5 * skill_os_power:.3f}__**'
                                 f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * skill_os_power:.3f}__**'
                                 f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * skill_os_power:.3f}__**',
                           inline=False)

        embed_11.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                           value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power + 0.05):.3f}__**',
                           inline=False)

        embed_11.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                           value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * skill_os_power:.3f}**__')

        embed_11.add_field(name='**聖剣 (In 浮世の砂海)**',
                           value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power + 0.05):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power + 0.05):.3f}__**',
                           inline=False)

        # ハグレモノ
        embed_12 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                 url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                 description=f"**職業：ハグレモノ**")

        embed_12.set_author(name=ctx.author.name)

        embed_12.add_field(name='条件',
                           value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_12.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                           value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.07):.3f}__**\n'
                                 f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.07):.3f}__**, '
                                 f'**(詠唱時：__{skill_attack * 8 * skill_os_power:.3f}__**)'
                                 f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power - 0.07):.3f}__**\n'
                                 f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                           inline=False)

        embed_12.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                           value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.07):.3f}__**'
                                 f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_12.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                           value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.07):.3f}__**'
                                 f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * skill_os_power - 0.07:.3f}__**',
                           inline=False)

        embed_12.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                           value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.07):.3f}__, '
                                 f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power - 0.07):.3f}__**'
                                 f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.07):.3f}__**'
                                 f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_12.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                           value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_12.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                           value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.07):.3f}**__')

        embed_12.add_field(name='**聖剣 (In 浮世の砂海)**',
                           value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.07):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        # ルーンキャスター
        embed_13 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                 url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                 description=f"**職業：ルーンキャスター**")

        embed_13.set_author(name=ctx.author.name)

        embed_13.add_field(name='条件',
                           value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_13.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                           value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power + 0.07):.3f}__**\n'
                                 f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power + 0.07):.3f}__**, '
                                 f'**(詠唱時：__{skill_attack * 8 * (skill_os_power + 0.07):.3f}__**)'
                                 f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power + 0.07):.3f}__**\n'
                                 f'ファイヤ・ボルケーノ (ノーマル)**：__{skill_attack * 22 * (skill_os_power + 0.07):.3f}__**',
                           inline=False)

        embed_13.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                           value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.07):.3f}__**'
                                 f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_13.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                           value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.07):.3f}__**'
                                 f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_13.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                           value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power - 0.07):.3f}__, '
                                 f'パッシブあり：__{skill_attack * 12.5 * 1.5 * skill_os_power:.3f}__**'
                                 f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power - 0.07):.3f}__**'
                                 f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_13.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                           value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_13.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                           value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.07):.3f}**__')

        embed_13.add_field(name='**聖剣 (In 浮世の砂海)**',
                           value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.07):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        # スペランカー
        embed_14 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                 url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                 description=f"**職業：スペランカー**")

        embed_14.set_author(name=ctx.author.name)

        embed_14.add_field(name='条件',
                           value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_14.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                           value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power + 0.10) :.3f}__**\n'
                                 f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power + 0.10):.3f}__**, '
                                 f'**(詠唱時：__{skill_attack * 8 * (skill_os_power + 0.10):.3f}__**)'
                                 f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power + 0.10):.3f}__**\n'
                                 f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                           inline=False)

        embed_14.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                           value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.10):.3f}__**'
                                 f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.10):.3f}__**',
                           inline=False)

        embed_14.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                           value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.10):.3f}__**'
                                 f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.10):.3f}__**',
                           inline=False)

        embed_14.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                           value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power + 0.10):.3f}__, '
                                 f'パッシブあり：__{skill_attack * 12.5 * 1.5 * (skill_os_power + 0.10):.3f}__**'
                                 f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power + 0.10):.3f}__**'
                                 f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power + 0.10):.3f}__**',
                           inline=False)

        embed_14.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                           value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power + 0.10):.3f}__**',
                           inline=False)

        embed_14.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                           value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power + 0.10):.3f}**__')

        embed_14.add_field(name='**聖剣 (In 浮世の砂海)**',
                           value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power + 0.10):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power + 0.10):.3f}__**',
                           inline=False)

        # アーサー
        embed_15 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                 url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                 description=f"**職業：アーサー**")

        embed_15.set_author(name=ctx.author.name)

        embed_15.add_field(name='条件',
                           value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_15.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                           value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * skill_os_power :.3f}__**\n'
                                 f'マジックボール (ノーマル)**：__{skill_attack * 4 * skill_os_power :.3f}__**, '
                                 f'**(詠唱時：__{skill_attack * 8 * skill_os_power :.3f}__**)'
                                 f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * skill_os_power :.3f}__**\n'
                                 f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                           inline=False)

        embed_15.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                           value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.05):.3f}__**'
                                 f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.05):.3f}__**',
                           inline=False)

        embed_15.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                           value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * skill_os_power :.3f}__**'
                                 f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * skill_os_power :.3f}__**',
                           inline=False)

        embed_15.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                           value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * skill_os_power :.3f}__, '
                                 f'パッシブあり：__{skill_attack * 12.5 * 1.5 * skill_os_power :.3f}__**'
                                 f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * skill_os_power :.3f}__**'
                                 f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * skill_os_power :.3f}__**',
                           inline=False)

        embed_15.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                           value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power + 0.05):.3f}__**',
                           inline=False)

        embed_15.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                           value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * skill_os_power :.3f}**__')

        embed_15.add_field(name='**聖剣 (In 浮世の砂海)**',
                           value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power + 0.05):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power + 0.05):.3f}__**',
                           inline=False)

        # シーカー
        embed_16 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                                 url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                                 description=f"**職業：シーカー**")

        embed_16.set_author(name=ctx.author.name)

        embed_16.add_field(name='条件',
                           value=f'素火力： {skill_dmg}\nOS： {skill_os}\nOS倍率： {skill_os_power}\n魔法石： {skill_tokkou}\n魔法石倍率：{skill_tokkou_add}倍')

        embed_16.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                           value=f'メテオストライク (スペシャル)：**__{skill_attack * 9 * (skill_os_power - 0.07):.3f}__**\n'
                                 f'マジックボール (ノーマル)**：__{skill_attack * 4 * (skill_os_power - 0.07):.3f}__**, '
                                 f'**(詠唱時：__{skill_attack * 8 * (skill_os_power - 0.07):.3f}__**)'
                                 f'\nライトニングボルト (ノーマル)：**__{skill_attack * 3 * (skill_os_power - 0.07):.3f}__**\n'
                                 f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                           inline=False)

        embed_16.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                           value=f'ショックストーン (スペシャル)：**__{skill_attack * 7 * (skill_os_power - 0.07):.3f}__**'
                                 f'\nトゥルーロック (ノーマル)：**__{skill_attack * 4 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_16.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                           value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{skill_attack * 7 * (skill_os_power + 0.07):.3f}__**'
                                 f'\n雪柱 (ノーマル)：**__{skill_attack * 4 * (skill_os_power + 0.07):.3f}__**',
                           inline=False)

        embed_16.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                           value=f'オーバーシュート (スペシャル)：**__{skill_attack * 12.5 * (skill_os_power + 0.07):.3f}__, '
                                 f'パッシブあり：__{skill_attack * 12.5 * 1.5 * skill_os_power:.3f}__**'
                                 f'\nシャドウパワー (ノーマル)：**__{skill_attack * 1.5 * (skill_os_power + 0.07):.3f}__**'
                                 f'\nエレメンタルパワー	(パッシブ)：**__{skill_attack * 1.5 * (skill_os_power + 0.07):.3f}__**',
                           inline=False)

        embed_16.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                           value=f'血の斬撃 (スペシャル)：**__{skill_attack * 2.5 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        embed_16.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                           value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{skill_attack * 8 * (skill_os_power - 0.07):.3f}**__')

        embed_16.add_field(name='**聖剣 (In 浮世の砂海)**',
                           value=f'下克上 (パッシブ)：**__ボスmob {skill_attack * 1.2 * (skill_os_power - 0.07):.3f} / 通常mob {skill_attack * 0.7 * (skill_os_power - 0.07):.3f}__**',
                           inline=False)

        # embed_list_2 = [embed_8, embed_9, embed_10, embed_11, embed_12, embed_13, embed_14, embed_15, embed_16]
        emoji_list_2 = [emoji_1, emoji_2, emoji_3, emoji_4, emoji_5, emoji_6, emoji_7, emoji_8, emoji_9]
        sent_message = await ctx.channel.send(embed=embed_8)

        for emoji in emoji_list_2:
            await sent_message.add_reaction(emoji=emoji)

        # リアクションチェック用の関数
        def check(reaction, user):
            # botを呼び出した本人からのリアクションのみ受け付ける
            # reaction.message == msg を入れないと複数出したときに全て連動して動いてしまう
            return user == ctx.author and reaction.message == sent_message and str(
                reaction.emoji) in emoji_list_2

        while True:
            try:
                # リアクションが付けられるまで待機
                reaction, user = await bot.wait_for('reaction_add', timeout=40.0, check=check)

            except asyncio.TimeoutError:
                # 一定時間経ったら消す
                # for remove_emoji in emoji_list:
                # await sent_message.remove_reaction(emoji=remove_emoji, member=bot.user)
                await sent_message.clear_reactions()
                break

            else:

                # 付けられたリアクションに対応した処理を行う
                if str(reaction.emoji) == (emoji_list_2[0]):
                    await sent_message.edit(embed=embed_8)

                if str(reaction.emoji) == (emoji_list_2[1]):
                    await sent_message.edit(embed=embed_9)

                if str(reaction.emoji) == (emoji_list_2[2]):
                    await sent_message.edit(embed=embed_10)

                if str(reaction.emoji) == (emoji_list_2[3]):
                    await sent_message.edit(embed=embed_11)

                if str(reaction.emoji) == (emoji_list_2[4]):
                    await sent_message.edit(embed=embed_12)

                if str(reaction.emoji) == (emoji_list_2[5]):
                    await sent_message.edit(embed=embed_13)

                if str(reaction.emoji) == (emoji_list_2[6]):
                    await sent_message.edit(embed=embed_14)

                if str(reaction.emoji) == (emoji_list_2[7]):
                    await sent_message.edit(embed=embed_15)

                if str(reaction.emoji) == (emoji_list_2[8]):
                    await sent_message.edit(embed=embed_16)

                # リアクションをもう一度押せるように消しておく
                await sent_message.remove_reaction(reaction.emoji, ctx.author)
    except:
        await ctx.send(f':thinking: {ctx.author.mention},`.skill2 [総ダメージ] [OS] (魔法石)`')

bot.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
#bot.run('ODg2NDg2MjA3Mzk0MDk5MjIw.YT2SnQ.7xCgf-xymfPEl519dztE0Gle8Fs')
