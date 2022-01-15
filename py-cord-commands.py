# coding=utf-8
import discord
from discord.commands import Option
from discord.ext import commands
import asyncio
import pytz
from datetime import datetime

from re_dictionary import osdict, castimedict, dict_1, dict_2, dict_3, dict_4, dict_5
from re_definition import tokkou, ctcalc, tokkoulist, embed_list

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', help_command=None, intents=intents)
now = datetime.now(pytz.timezone('Asia/Tokyo'))
token = 'ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY'

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

magicstonelist = ['1', '2', '3', '4', '4_5', '5', 'legend']
casmagiclist = ['1', '2', '3', '4', '4_5', '5']
ctperk = [i for i in range(11)]
osperk = [i for i in range(75)]
slotlist = [1, 2, 3, 4, 5]


async def magicstone(ctx: discord.ApplicationContext):
    return [ms for ms in magicstonelist if ms.startswith(ctx.value)]


@bot.event
async def on_ready():
    print(bot.user.id)
    print(bot.user.name)
    print('Ver.:' + discord.__version__)


@bot.command()
async def guild(ctx: commands.Context):
    await ctx.send("I'm in **" + str(len(bot.guilds)) + "** servers!")
    await ctx.send(str(bot.guilds))


@bot.command(aliases=['q'])
async def channel(ctx: commands.Context):
    k = '```\n'
    n = '```\n'
    k += f'{len(list(bot.get_all_channels()))}\n'
    for i in bot.get_all_channels():
        k += f'{i.id} : {i}\n'

    for x in bot.get_all_members():
        n += f'{x.id} : {x}\n'

    await ctx.send(f'{k}\n```')
    await asyncio.sleep(2)
    await ctx.send(f'{n}\n```')


@bot.command()
async def msg(ctx: commands.context, ids, *, args):
    try:
        channelid = ids
        for channels in bot.get_all_channels():
            if channels.id == channelid:
                await channel.send(args)
    except:
        print('q')


@bot.command(name='g_id')
async def guild_id(ctx: commands.Context):
    await ctx.send(str(ctx.guild.id))


@bot.command(name='c_id')
async def channel_id(ctx: commands.Context):
    await ctx.send(str(ctx.channel.id))


@bot.command(aliases=['glist'])
async def guildlist(ctx: commands.context):
    i = 1
    embed = discord.Embed(title="Glist", color=discord.Colour.gold(), timestamp=now)
    async for guild in bot.fetch_guilds():
        embed.add_field(name=i, value=f'**`{guild.name}`**', inline=False)
        i += 1

    await ctx.send(embed=embed)


@bot.command(aliases=['?', 'h'])
async def help(ctx: commands.Context):
    embed = discord.Embed(title="コマンド一覧", color=discord.Colour.gold(), timestamp=now)
    embed.set_author(name=ctx.author.name)
    embed.add_field(name='ヘルプ', value='.help (aliases=[\'h\',\'?\']', inline=False)
    embed.add_field(
        name='ダメージ計算', value='.dmg [攻撃力] [OS] [魔法石(1~5, ただし4_5, 5, LEGは重複不可)]', inline=False)
    embed.add_field(
        name='職業込みでのダメージ計算', value='.job [攻撃力] [OS] [魔法石(1~5, ただし4_5と5は重複不可)]', inline=False)
    embed.add_field(
        name='キャスター', value='.cas [CT] [CTPerk] [魔法石(1 ~ 5)]', inline=False)
    embed.add_field(name='最低OSを求める場合', value='.ask [欲しい火力] [今の素ダメ] ? [魔法石]', inline=False)
    embed.add_field(name='最低火力を求める場合', value='.ask [欲しい火力] ? [OS] [魔法石]', inline=False)
    embed.add_field(name='おすすめ魔法石', value='.magicstone (又は\'ms\') 欲しいダメージ 素火力 OS スロット数', inline=False)
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
async def invite(ctx: commands.Context):
    inv_link = discord.utils.oauth_url(client_id=884986866221326347) + '&permissions=8'
    await ctx.send(f'招待リンク：{inv_link}\n\nスラッシュコマンド登録はdmください。')
    await ctx.message.delete()


# @bot.slash_command(guild_ids=[869729203778646046])
@bot.slash_command(guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def help(ctx: discord.ApplicationContext):
    embed = discord.Embed(title="コマンド一覧", description="`[]` は必須項目, `()` は無くても可", color=discord.Colour.gold(),
                          timestamp=now)
    embed.set_author(name=ctx.author.name)
    embed.add_field(name='ヘルプ', value='/help', inline=False)
    embed.add_field(
        name='ダメージ計算', value='/dmg raw=[攻撃力] os=[OS] magicstone=(魔法石(1~5, ただし4_5, 5, LEGは重複不可))', inline=False)
    embed.add_field(
        name='職業込みでのダメージ計算', value='/job raw=[攻撃力] os=[OS] magicstone=(魔法石(1~5, ただし4_5と5は重複不可))', inline=False)
    embed.add_field(
        name='キャスター', value='/ct ct=[CT] perk=[CTPerk] magicstone=(魔法石(1 ~ 5))', inline=False)
    embed.add_field(name='最低OSを求める場合', value='/ask need=[欲しい火力] raw=[今の素ダメ] magicstone=(魔法石)', inline=False)
    embed.add_field(name='最低火力を求める場合', value='/ask need=[欲しい火力] os=[OS] magicstone=(魔法石)', inline=False)
    embed.add_field(name='おすすめ魔法石', value='/magicstone need=[欲しいダメージ] raw=[素火力] os=[OS] slot=[スロット数]', inline=False)
    embed.add_field(name='招待リンク', value='/inv', inline=False)

    sent_message = await ctx.respond(embed=embed, ephemeral=True)


# @bot.slash_command(guild_ids=[869729203778646046])
@bot.slash_command(guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def invite(ctx: discord.ApplicationContext):
    link = discord.utils.oauth_url(client_id=bot.user.id) + '&permissions=8'

    await ctx.respond(f'{link}\nスラッシュコマンド登録を希望の場合、DMください。')


# 完了
# @bot.slash_command(name='dmg', guild_ids=[869729203778646046])
@bot.slash_command(name='dmg', guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def damage(
        ctx: discord.ApplicationContext,
        raw: Option(float, description='素ダメ'),
        os: Option(int, description='OS値'),
        slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
        slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
        slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
        slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
        slot5: Option(str, description='スロット5', choices=magicstonelist, required=False)
):
    x = list()
    r = list()
    x = [slot1, slot2, slot3, slot4, slot5]

    for i in x:
        if i in r:
            if i is None:
                pass
            else:
                await ctx.respond("error\n\n数値が重複しています。重複したものは1つとしてカウントします。", ephemeral=True)
                pass

        if i is None:
            pass
        else:
            r.append(i)

    osraw = osdict[os]
    dmg, alpha = await tokkou(ctx, raw, osraw, x)
    await ctx.respond(f'素ダメ: {raw}\nOS値: {os}\nOS倍率: {osraw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**__最終的な攻撃力: {dmg:.3f}__**')


# 完了
# @bot.slash_command(name='ask', description='', guild_ids=[869729203778646046])
@bot.slash_command(name='ask', guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def askdamage(
        ctx: discord.ApplicationContext,
        need: Option(float, description='欲しい火力'),
        raw: Option(float, description='素ダメ', required=False),
        os: Option(int, description='OS値', required=False),
        slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
        slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
        slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
        slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
        slot5: Option(str, description='スロット5', choices=magicstonelist, required=False),
):
    if (os is None) and (raw is None):
        await ctx.respond(f'どちらか1方は埋めてください', ephemeral=True)
        return

    if (raw is not None) and (os is not None):
        await ctx.respond('どちらか1方のみ埋めてください', ephemeral=True)
        return
    print("!!")
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    x = list()
    r = list()
    x = [slot1, slot2, slot3, slot4, slot5]
    if os:
        if os >= len(osdict):
            await ctx.respond(f'OSは{len(osdict)}までしか登録されていません。')

        else:
            print("?")
            for i in x:
                if i in r:
                    if i is None:
                        pass
                    else:
                        await ctx.respond("error\n\n数値が重複しています。重複したものは1つとしてカウントします。", ephemeral=True)
                        pass

                if i is None:
                    pass
                else:
                    r.append(i)

            osraw = osdict[os]
            n = 1.0
            dmg, alpha = await tokkou(ctx, n, osraw, x)
            times = need / dmg
            # 1000/ None/ 16 => 2.33856, 62.5
            await ctx.respond(
                f'欲しい火力: {need}\nOS値: {os}\nOS倍率: {osraw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**__必要な攻撃力: {times:.3f}__**')

            if os is None:
                osraw = osdict[0]
                dmg, alpha = await tokkou(ctx, raw, osraw, x)
                times = need / dmg

                for i in range(len(osdict)):
                    if osdict[i] > times:
                        await ctx.respond(
                            f'欲しい火力: {need}\n攻撃力: {raw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**__必要なOS: {i}__**  (OS倍率: {osdict[i]})')
                        break

                    if times >= osdict[74]:
                        await ctx.respond(
                            f'欲しい火力: {need}\n攻撃力: {raw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**この攻撃力では求める火力を出すことは不可能です。**')
                        break
    if raw:
        for i in x:
            if i in r:
                if i is None:
                    pass
                else:
                    await ctx.respond("error\n\n数値が重複しています。重複したものは1つとしてカウントします。", ephemeral=True)
                    pass

            if i is None:
                pass
            else:
                r.append(i)

        osraw = osdict[0]
        dmg, alpha = await tokkou(ctx, raw, osraw, x)

        times = need / dmg

        for i in range(len(osdict)):
            if osdict[0] >= times:
                await ctx.respond(
                    f'欲しい火力: {need}\n攻撃力: {raw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**__OSを積む必要はありません。__**'
                )
            if osdict[i] > times:
                await ctx.respond(
                    f'欲しい火力: {need}\n攻撃力: {raw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**__必要なOS: {i}__**  (OS倍率: {osdict[i]})')
                break

            if times >= osdict[74]:
                await ctx.respond(
                    f'欲しい火力: {need}\n攻撃力: {raw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**この攻撃力では求める火力を出すことは不可能です。**')
                break


# 完了
# @bot.slash_command(name='ct', guild_ids=[869729203778646046])
@bot.slash_command(name='ct', guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def cooltime(
        ctx: discord.ApplicationContext,
        ct: Option(float, description='All Cool Time'),
        perk: Option(int, description='Quick Talk Spell の値', choices=ctperk),
        slot1: Option(str, description='スロット1', choices=casmagiclist, required=False),
        slot2: Option(str, description='スロット2', choices=casmagiclist, required=False),
        slot3: Option(str, description='スロット3', choices=casmagiclist, required=False),
        slot4: Option(str, description='スロット4', choices=casmagiclist, required=False),
        slot5: Option(str, description='スロット5', choices=casmagiclist, required=False)
):
    if perk >= len(castimedict):
        await ctx.respond(f'Perkは{len(castimedict)}までしか登録されていません。')

    else:
        x = list()
        r = list()
        r_cp = list()
        x = [slot1, slot2, slot3, slot4, slot5]
        ctperk = castimedict[perk]

        for i in x:
            if i in r:
                if i is None:
                    pass
                else:
                    await ctx.respond("error\n\n数値が重複しています。重複したものは1つとしてカウントします。", ephemeral=True)
                    pass

            if i is None:
                pass
            else:
                r.append(i)
        finalct, a = await ctcalc(ctx, raw=ct, perkraw=ctperk, x=x)
        strings = f'元のCT: {ct}\nパーク値: {perk}\nパークで減少する割合: {ctperk}\n魔法石: {r}\n魔法石倍率: {a}\n\n**最終的なCT: {finalct: .3f}**'

        if ct == 220:
            strings += '\n恵みの泉は効果時間(20s)を含めて実際のctとなります。よって最速泉は36+20秒です。'
        await ctx.respond(strings)


# 完了
# @bot.slash_command(name='job', guild_ids=[869729203778646046])
@bot.slash_command(name='job', guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def job_damage(
        ctx: discord.ApplicationContext,
        raw: Option(float, description='素ダメ'),
        os: Option(int, description='OS値'),
        slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
        slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
        slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
        slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
        slot5: Option(str, description='スロット5', choices=magicstonelist, required=False)
):
    if os >= len(osdict):
        await ctx.respond(f'OSは{len(osdict)}までしか登録されていません。')

    else:
        x = list()
        r = list()
        r_cp = list()
        x = [slot1, slot2, slot3, slot4, slot5]
        osraw = osdict[os]
        for i in x:
            if i in r:
                if i is None:
                    pass
                else:
                    await ctx.respond("error", ephemeral=True)
                    pass

            if i is None:
                pass
            else:
                r.append(i)

        dmg, alpha = await tokkou(ctx, raw, osraw=1.0, x=x)

        embed_1_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
        embed_1_job.set_author(name=f"By {ctx.author}")

        embed_1_job.add_field(name='条件', value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n'
                                               f'魔法石： {r}\n魔法石倍率： {alpha}倍')
        embed_1_job.add_field(name='ソルジャー', value=f'__**攻撃力：剣：+5%: {float(dmg * (osraw + 0.05)):.3f},'
                                                  f' 弓：-2%: {float(dmg * (osraw - 0.02)):.3f},'
                                                  f' 魔法：-2%: {float(dmg * (osraw - 0.02)):.3f}**__',
                              inline=False)

        embed_1_job.add_field(name='アーチャー', value=f"__**攻撃力：剣：-2%: {float(dmg * (osraw - 0.02)):.3f},"
                                                  f" 弓：+5%: {float(dmg * (osraw + 0.05)):.3f},"
                                                  f" 魔法：-2%: {float(dmg * (osraw - 0.02)):.3f}**__",
                              inline=False)

        embed_1_job.add_field(name='マジシャン', value=f"__**攻撃力：剣：-2%: {float(dmg * (osraw - 0.02)):.3f},"
                                                  f" 弓：-2%: {float(dmg * (osraw - 0.02)):.3f},"
                                                  f" 魔法：+5%: {float(dmg * (osraw + 0.05)):.3f}**__",
                              inline=False)

        embed_1_job.set_footer(text='Page 1 of 4')

        embed_2_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

        embed_2_job.set_author(name=f"By {ctx.author}")
        embed_2_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}'
                                               f'\n魔法石倍率： {alpha}倍')

        embed_2_job.add_field(name='ウォーリア', value=f"__**攻撃力：剣：+10%: {float(dmg * (osraw + 0.10)):.3f},"
                                                  f" 弓： -5%: {float(dmg * (osraw - 0.05)):.3f},"
                                                  f" 魔法： -5%: {float(dmg * (osraw - 0.05)):.3f}**__",
                              inline=False)

        embed_2_job.add_field(name='ボウマン', value=f"__**攻撃力：剣： -5%: {float(dmg * (osraw - 0.05)):.3f},"
                                                 f" 弓：+10%: {float(dmg * (osraw + 0.10)):.3f},"
                                                 f" 魔法： -5%: {float(dmg * (osraw - 0.05)):.3f}**__",
                              inline=False)

        embed_2_job.add_field(name='メイジ', value=f"__**攻撃力：剣： -5%: {float(dmg * (osraw - 0.05)):.3f},"
                                                f" 弓： -5%: {float(dmg * (osraw - 0.05)):.3f},"
                                                f" 魔法：+10: {float(dmg * (osraw + 0.10)):.3f}**__",
                              inline=False)

        embed_2_job.set_footer(text='Page 2 of 4')

        embed_3_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

        embed_3_job.set_author(name=f"By {ctx.author}")
        embed_3_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n'
                                               f'魔法石倍率： {alpha}倍')

        embed_3_job.add_field(name='ロウニン', value=f"__**攻撃力：剣：-4%: {float(dmg * (osraw - 0.04)):.3f},"
                                                 f" 弓：-4%: {float(dmg * (osraw - 0.04)):.3f},"
                                                 f" 魔法：-4%: {float(dmg * (osraw - 0.04)):.3f}**__",
                              inline=False)

        embed_3_job.add_field(name='ドラゴンキラー', value=f"__**攻撃力：剣：-2%: {float(dmg * (osraw - 0.02)):.3f}, "
                                                    f" 弓：+5%: {float(dmg * (osraw + 0.05)):.3f},"
                                                    f" 魔法：-2%: {float(dmg * (osraw - 0.02)):.3f}**__",
                              inline=False)

        embed_3_job.add_field(name='プリースト', value=f"__**攻撃力：剣：-10%: {float(dmg * (osraw - 0.10)):.3f},"
                                                  f" 弓：-10%: {float(dmg * (osraw - 0.10)):.3f},"
                                                  f" 魔法：-10%: {float(dmg * (osraw - 0.10)):.3f}**__",
                              inline=False)

        embed_3_job.add_field(name='スカーミッシャー', value=f"__**攻撃力：剣：+5%: {float(dmg * (osraw + 0.05)):.3f},"
                                                     f" 弓：{float(dmg * osraw):.3f},"
                                                     f" 魔法：{float(dmg * osraw):.3f}**__", inline=False)

        embed_3_job.set_footer(text='Page 3 of 4')

        embed_4_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=now,
                                    url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

        embed_4_job.set_author(name=f"By {ctx.author}")
        embed_4_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n'
                                               f'魔法石倍率： {alpha}倍')

        embed_4_job.add_field(name='ハグレモノ', value=f"__**攻撃力：剣：-7%: {float(dmg * (osraw - 0.07)):.3f},"
                                                  f" 弓：-7%: {float(dmg * (osraw - 0.07)):.3f},"
                                                  f" 魔法：-7%: {float(dmg * (osraw - 0.07)):.3f}**__",
                              inline=False)

        embed_4_job.add_field(name='ルーンキャスター', value=f"__**攻撃力：剣：-7%: {float(dmg * (osraw - 0.07)):.3f},"
                                                     f" 弓：-7%: {float(dmg * (osraw - 0.07)):.3f},"
                                                     f" 魔法：+7%: {float(dmg * (osraw + 0.07)):.3f}**__",
                              inline=False)

        embed_4_job.add_field(name='スペランカー', value=f"__**攻撃力：剣：+10%: {float(dmg * (osraw + 0.10)):.3f},"
                                                   f"  弓：+10%: {float(dmg * (osraw + 0.10)):.3f},"
                                                   f" 魔法：+10%: {float(dmg * (osraw + 0.10)):.3f}**__",
                              inline=False)

        embed_4_job.add_field(name='アーサー', value=f"__**攻撃力：剣：+5%: {float(dmg * (osraw + 0.05)):.3f},"
                                                 f" 弓：{float(dmg * osraw):.3f},"
                                                 f" 魔法：{float(dmg * osraw):.3f}**__", inline=False)

        embed_4_job.add_field(name='シーカー', value=f"__**攻撃力：剣：-7%: {float(dmg * (osraw - 0.07)):.3f},"
                                                 f" 弓：+10%: {float(dmg * (osraw + 0.10)):.3f},"
                                                 f" 魔法：-7%: {float(dmg * (osraw - 0.07)):.3f}**__",
                              inline=False)

        embed_4_job.set_footer(text='Page 4 of 4')
        await ctx.respond(f'**{emoji_1} : ソルジャー, アーチャー, マジシャン\n\n'
                          f'{emoji_2} : ウォーリ, ボウマン, メイジ\n\n'
                          f'{emoji_3} : ロウニン , ドラゴンキラー, プリースト, スカーミッシャー\n\n'
                          f'{emoji_4} : ハグレモノ, ルーンキャスター, スペランカー, アーサー, シーカー**', ephemeral=True)
        sent_message = await ctx.send(embed=embed_1_job)

        emoji_list = [emoji_1, emoji_2, emoji_3, emoji_4]
        for i in emoji_list:
            await sent_message.add_reaction(i)

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
                if str(reaction.emoji) == emoji_1:
                    await sent_message.edit(embed=embed_1_job)

                if str(reaction.emoji) == emoji_2:
                    await sent_message.edit(embed=embed_2_job)

                if str(reaction.emoji) == emoji_3:
                    await sent_message.edit(embed=embed_3_job)

                if str(reaction.emoji) == emoji_4:
                    await sent_message.edit(embed=embed_4_job)

                await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)


# @bot.slash_command(name='skill', guild_ids=[869729203778646046])
@bot.slash_command(name='skill', guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def skilldamage(
        ctx: discord.ApplicationContext,
        raw: Option(float, description='素ダメ'),
        os: Option(int, description='OS値'),
        slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
        slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
        slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
        slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
        slot5: Option(str, description='スロット5', choices=magicstonelist, required=False)
):
    if os >= len(osdict):
        await ctx.respond(f'OSは{len(osdict)}までしか登録されていません。')

    else:
        x = list()
        r = list()
        r_cp = list()
        osraw = osdict[os]
        x = [slot1, slot2, slot3, slot4, slot5]
        if ('4_5' and '5') in x:
            print("SSSS")
        for i in x:
            if i in r:
                if i is None:
                    pass
                else:
                    await ctx.respond("error", ephemeral=True)
                    pass

            if i is None:
                pass
            else:
                r.append(i)
        await ctx.respond(
            f'\U0001f1e6 :  ノービス\n'
            f'\U0001f1e7 : ソルジャー , \U0001f1e8 : アーチャー , \U0001f1e9 : マジシャン\n'
            f'\U0001f1ea : ウォーリア , \U0001f1eb : ボウマン , 　\U0001f1ec : メイジ \n\n'
            f'\U0001f1ed : ロウニン , 　　　　\U0001f1ee : ドラゴンキラー , \U0001f1ef : プリースト\n'
            f'\U0001f1f0 : スカ―ミッシャー , \U0001f1f1 : ハグレモノ , 　　\U0001f1f2 : ルーンキャスター\n'
            f'\U0001f1f3 : スペランカー , 　　\U0001f1f4 : アーサー , 　　　\U0001f1f5 : シーカー', ephemeral=True)

        osrawpower = 1.0
        dmg, alpha = await tokkou(ctx, raw=raw, osraw=osrawpower, x=x)

        embed_lists = await embed_list(ctx, dmg, raw, os, osraw, r, alpha, now)

        sent_message = await ctx.send(embed=embed_lists[0])

        emoji_list = ['\U0001f1e6', '\U0001f1e7', '\U0001f1e8', '\U0001f1e9',
                      '\U0001f1ea', '\U0001f1eb', '\U0001f1ec', '\U0001f1ed',
                      '\U0001f1ee', '\U0001f1ef', '\U0001f1f0', '\U0001f1f1',
                      '\U0001f1f2', '\U0001f1f3', '\U0001f1f4', '\U0001f1f5']

        for i in emoji_list:
            await sent_message.add_reaction(emoji=i)

        # リアクションチェック用の関数
        def check(reaction, user):
            # botを呼び出した本人からのリアクションのみ受け付ける
            # reaction.message == msg を入れないと複数出したときに全て連動して動いてしまう
            return user == ctx.author and reaction.message == sent_message and str(
                reaction.emoji) in emoji_list

        while True:
            try:
                # リアクションが付けられるまで待機
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)

            except asyncio.TimeoutError:
                # 一定時間経ったら消す
                # for remove_emoji in emoji_list:
                # await sent_message.remove_reaction(emoji=remove_emoji, member=bot.user)
                await sent_message.clear_reactions()
                break

            else:
                if str(reaction.emoji) == emoji_list[0]:
                    await sent_message.edit(embed=embed_lists[0])

                if str(reaction.emoji) == emoji_list[1]:
                    await sent_message.edit(embed=embed_lists[1])

                if str(reaction.emoji) == emoji_list[2]:
                    await sent_message.edit(embed=embed_lists[2])

                if str(reaction.emoji) == emoji_list[3]:
                    await sent_message.edit(embed=embed_lists[3])

                if str(reaction.emoji) == emoji_list[4]:
                    await sent_message.edit(embed=embed_lists[4])

                if str(reaction.emoji) == emoji_list[5]:
                    await sent_message.edit(embed=embed_lists[5])

                if str(reaction.emoji) == emoji_list[6]:
                    await sent_message.edit(embed=embed_lists[6])

                if str(reaction.emoji) == emoji_list[7]:
                    await sent_message.edit(embed=embed_lists[7])

                if str(reaction.emoji) == emoji_list[8]:
                    await sent_message.edit(embed=embed_lists[8])

                if str(reaction.emoji) == emoji_list[9]:
                    await sent_message.edit(embed=embed_lists[9])

                if str(reaction.emoji) == emoji_list[10]:
                    await sent_message.edit(embed=embed_lists[10])

                if str(reaction.emoji) == emoji_list[11]:
                    await sent_message.edit(embed=embed_lists[11])

                if str(reaction.emoji) == emoji_list[12]:
                    await sent_message.edit(embed=embed_lists[12])

                if str(reaction.emoji) == emoji_list[13]:
                    await sent_message.edit(embed=embed_lists[13])

                if str(reaction.emoji) == emoji_list[14]:
                    await sent_message.edit(embed=embed_lists[14])

                if str(reaction.emoji) == emoji_list[15]:
                    await sent_message.edit(embed=embed_lists[15])

                await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)


# @bot.slash_command(aliases=['ms'], guild_ids=[869729203778646046])
@bot.slash_command(aliases=['ms'], guild_ids=[885757485871398985, 889120444068790292, 920561679266373642])
async def magicstone(
        ctx: discord.ApplicationContext,
        need: Option(float, description='欲しい火力'),
        raw: Option(float, description='素ダメ'),
        os: Option(int, description='OS値'),
        slot: Option(int, description='スロット数', choices=slotlist)
):
    if os >= len(osdict):
        await ctx.respond(f'OSは{len(osdict)}までしか登録されていません。')
    else:
        osraw = osdict[os]
        s = need / (raw * osraw)
        if slot == 1:
            if s > 1.55:
                await ctx.respond('Index out of range!\nスロットが足りません。', ephemeral=True)

            else:
                for i in dict_1:
                    if dict_1[i] > s:
                        await ctx.respond(
                            f'条件：\n魔法石付けた後の欲しいダメージ：{need}\n今の素火力：{raw}\nOS：{os}\nOS倍率：{osraw}\n魔法石スロット：1\n\n**結果：{i}**')
                        break

        if slot == 2:
            if s > (1.55 * 1.35):
                await ctx.respond('Index out of range!\nスロットが足りません。', ephemeral=True)

            else:
                for i in dict_2:
                    if dict_2[i] > s:
                        await ctx.respond(
                            f'条件：\n魔法石付けた後の欲しいダメージ：{need}\n今の素火力：{raw}\nOS：{os}\nOS倍率：{osraw}\n魔法石スロット：2\n\n**結果：{i}**')
                        break

        if slot == 3:
            if s > (1.55 * 1.35 * 1.23):
                await ctx.respond('Index out of range!\nスロットが足りません。', ephemeral=True)

            else:
                for i in dict_3:
                    if dict_3[i] > s:
                        await ctx.respond(
                            f'条件：\n魔法石付けた後の欲しいダメージ：{need}\n今の素火力：{raw}\nOS：{os}\nOS倍率：{osraw}\n魔法石スロット：3\n\n**結果：{i}**')
                        break

        if slot == 4:
            if s > (1.55 * 1.35 * 1.23 * 1.15):
                await ctx.respond('Index out of range!\nスロットが足りません。', ephemeral=True)

            else:
                for i in dict_4:
                    if dict_4[i] > s:
                        await ctx.respond(
                            f'条件：\n魔法石付けた後の欲しいダメージ：{need}\n今の素火力：{raw}\nOS：{os}\nOS倍率：{osraw}\n魔法石スロット：4\n\n**結果：{i}**')
                        break

        if slot == 5:
            if s > (1.55 * 1.35 * 1.23 * 1.15 * 1.10):
                await ctx.respond('Index out of range!\nスロットが足りません。', ephemeral=True)

            else:
                for i in dict_5:
                    if dict_5[i] > s:
                        await ctx.respond(
                            f'条件：\n魔法石付けた後の欲しいダメージ：{need}\n今の素火力：{raw}\nOS：{os}\nOS倍率：{osraw}\n魔法石スロット：5\n\n**結果：{i}**')
                        break


@bot.command()
async def dmg(ctx: commands.Context, *args):
    # ダメージ・OS・魔法石
    try:

        print(type(ctx), type(args))
        dmg = float(args[0])
        os = int(args[1])
        tokkou_dmg = args[2:]
        tokkou = args[2:]

        if os > len(osdict):
            await ctx.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
            os_power = 1

        else:
            os_power = osdict[os]

        attack, tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)
        sent_message = await ctx.send(f"**By：{ctx.author.name}**\n\n素火力 : {dmg}\nOS : {os}\n"
                                      f"OS倍率 : {os_power} 倍\n魔法石：{tokkou_dmg}\n魔法石倍率：{tokkou_add}倍\n"
                                      f"__**攻撃力 : {attack:.3f}\n**__")
        await sent_message.add_reaction('🚮')

        while True:
            try:
                await bot.wait_for(event='reaction_add', timeout=20)

            except asyncio.TimeoutError:
                await sent_message.clear_reactions()
                break

    except:
        await ctx.send(f':thinking: {ctx.author.name}\n'
                       f'`.dmg [攻撃力] [OS] (魔法石)`の順に入力してください。')


# 職業
@bot.command()
async def job(ctx, *args):
    try:

        args = list(args)
        dmg = float(args[0])
        os = int(args[1])
        raw_tokkou = args[2:]
        tokkou = args[2:]
        print(tokkou)
        os_power = 1.0
        os_raw_power = osdict[os]

        attack, tokkou_dmg = await tokkoulist(ctx, dmg, os_power, tokkou)

        raw_tokkou.append('0')
        tokkou.append('0')

        attack, tokkou_dmg = await tokkoulist(ctx, dmg, os_power, tokkou)
        if raw_tokkou[0] == '0':
            raw_tokkou.remove('0')

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

                await sent_message.edit(embed=embed_list[page])

                # リアクションをもう一度押せるように消しておく
                await sent_message.remove_reaction(reaction.emoji, ctx.author)

    except:
        await ctx.send(f':thinking: {ctx.author.name}\n'
                       f'`.job [攻撃力] [OS] (魔法石)`の順に入力してください。')


@bot.command()
async def ask(ctx: commands.Context, *args):
    try:

        want_dmg = float(args[0])
        now_dmg = args[1]
        str_os = args[2]
        tokkou = args[3:]

        if now_dmg == '?':
            dmg = 1.0
            os = int(str_os)
            os_power = osdict[os]
            attack, tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)
            ans_dmg = want_dmg / attack
            sent_message = await ctx.send(f"OS：{os}の時\n{want_dmg}を出すには最低でも火力が__**{ans_dmg:.3f}**__が必要です。")
            await sent_message.add_reaction('🚮')

            while True:
                try:
                    await bot.wait_for(event='reaction_add', timeout=20)

                except asyncio.TimeoutError:
                    await sent_message.clear_reactions()
                    break
            return sent_message

        if str_os == '?':
            dmg = float(args[1])
            os_power = 1.0
            attack, tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)

            xos = float(want_dmg / attack)
            i = 0

            if xos > osdict[len(osdict) - 1]:
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
            return sent_message

    except:
        await ctx.send(f":thinking: {ctx.author.name}, `.ask [欲しい火力] [今の素ダメ] '?' (魔法石)`\n"
                       f"又は　`.ask [欲しい火力] '?' [今のOS] (魔法石)`\n"
                       f"と入力してください。")


@bot.command(aliases=["ct"])
async def cas(ctx: commands.Context, *args):
    xct = 1.0
    try:
        cas_time = float(args[0])
        cas_perk = int(args[1])
        cas_stone_1 = str(args[2:])
        cas_stone_2 = list(set(cas_stone_1))

        ct_perk = castimedict[cas_perk]

        if 'leg' in cas_stone_1:
            await ctx.send(f'{ctx.author}、キャスター石に\'leg\'はありません。')

        if '4.5' in cas_stone_2:
            cas_stone_2.remove("4.5")
            cas_stone_2.append("4_5")

        if ('4_5' in cas_stone_1) and ('4.5' in cas_stone_1):
            await ctx.send(f":thinking: {ctx.author.name}, 魔法石`4_5 と 4.5` は同じです。")

        if '1' in cas_stone_1:
            xct *= 0.95

        if '2' in cas_stone_1:
            xct *= 0.90

        if '3' in cas_stone_1:
            xct *= 0.84

        if '4' in cas_stone_1:
            xct *= 0.77

        if '4_5' in cas_stone_1:
            xct *= 0.72

        if '5' in cas_stone_1:
            xct *= 0.60

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
        await ctx.send(f':thinking: {ctx.author.name}, `.cas [元のCT] [CTPerk (0~10)] (魔法石)`')


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


@bot.command()
async def skill(ctx: commands.Context):
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
async def skill1(ctx: commands.Context, *args):
    try:
        dmg = float(args[0])
        skill_dmg = float(args[0])

        os = int(args[1])
        skill_os = int(args[1])

        skill_tokkou = args[2:]
        tokkou = args[2:]

        skill_os_power = osdict[os]
        os_power = 1.0

        skill_attack, skill_tokkou_add = await tokkoulist(ctx, dmg, os_power, tokkou)

        embed_lists = await embed_list(ctx, dmg=skill_attack, raw=skill_dmg, os=skill_os, osraw=skill_os_power,
                                       r=skill_tokkou, alpha=skill_tokkou_add, now=now)

        sent_message = await ctx.send(embed=embed_lists[0])

        emoji_list_1 = [emoji_1, emoji_2, emoji_3, emoji_4, emoji_5, emoji_6, emoji_7]

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
                    await sent_message.edit(embed=embed_lists[0])

                if str(reaction.emoji) == (emoji_list_1[1]):
                    await sent_message.edit(embed=embed_lists[1])

                if str(reaction.emoji) == (emoji_list_1[2]):
                    await sent_message.edit(embed=embed_lists[2])

                if str(reaction.emoji) == (emoji_list_1[3]):
                    await sent_message.edit(embed=embed_lists[3])

                if str(reaction.emoji) == (emoji_list_1[4]):
                    await sent_message.edit(embed=embed_lists[4])

                if str(reaction.emoji) == (emoji_list_1[5]):
                    await sent_message.edit(embed=embed_lists[5])

                if str(reaction.emoji) == (emoji_list_1[6]):
                    await sent_message.edit(embed=embed_lists[6])

                # リアクションをもう一度押せるように消しておく
                await sent_message.remove_reaction(reaction.emoji, ctx.author)

    except:
        await ctx.send(f':thinking: {ctx.author.name},`.skill1 [総ダメージ] [OS] (魔法石)`')


@bot.command()
async def skill2(ctx: commands.Context, *args):
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

        embed_lists = await embed_list(ctx, dmg=skill_attack, raw=dmg, os=os, osraw=skill_os_power, r=skill_tokkou,
                                       alpha=skill_tokkou_add, now=now)

        sent_message = await ctx.send(embed=embed_lists[7])
        print(f'{embed_lists}\n\n{sent_message}')

        # embed_list_2 = [embed_8, embed_9, embed_10, embed_11, embed_12, embed_13, embed_14, embed_15, embed_16]
        emoji_list_2 = [emoji_1, emoji_2, emoji_3, emoji_4, emoji_5, emoji_6, emoji_7, emoji_8, emoji_9]

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
                    await sent_message.edit(embed=embed_lists[7])

                if str(reaction.emoji) == (emoji_list_2[1]):
                    await sent_message.edit(embed=embed_lists[8])

                if str(reaction.emoji) == (emoji_list_2[2]):
                    await sent_message.edit(embed=embed_lists[9])

                if str(reaction.emoji) == (emoji_list_2[3]):
                    await sent_message.edit(embed=embed_lists[10])

                if str(reaction.emoji) == (emoji_list_2[4]):
                    await sent_message.edit(embed=embed_lists[11])

                if str(reaction.emoji) == (emoji_list_2[5]):
                    await sent_message.edit(embed=embed_lists[12])

                if str(reaction.emoji) == (emoji_list_2[6]):
                    await sent_message.edit(embed=embed_lists[13])

                if str(reaction.emoji) == (emoji_list_2[7]):
                    await sent_message.edit(embed=embed_lists[14])

                if str(reaction.emoji) == (emoji_list_2[8]):
                    await sent_message.edit(embed=embed_lists[15])

                # リアクションをもう一度押せるように消しておく
                await sent_message.remove_reaction(reaction.emoji, ctx.author)
    except:
        await ctx.send(f':thinking: {ctx.author.name},`.skill2 [総ダメージ] [OS] (魔法石)`')

bot.run(token)
