# coding=utf-8
import discord
from discord.ext import commands


async def tokkou(ctx: discord.ApplicationContext, raw: float, osraw: float, x: list):  # x: 魔法石
    a = 1.0
    alpha = 0
    if len(x) == 0:
        d_all = raw * osraw
        return d_all, a

    if ('4_5' and '5') in x:
        print("SSSS")
        await ctx.respond('`4_5` と `5` は同時に装着できません。魔法石を除いて計算します。', ephemeral=True)
        return raw * osraw, a

    elif ('5' and 'legend') in x:
        print("XXXX")
        await ctx.respond('`5` と `LEGEND` は同時に装着できません。魔法石を除いて計算します。', ephemeral=True)
        return raw * osraw, a

    elif ('4_5' and 'legend') in x:
        print("ZZZZ")
        await ctx.respond('`4_5` と `LEGEND` は同時に装着できません。魔法石を除いて計算します。', ephemeral=True)
        return raw * osraw, a

    else:
        if '4.5' in x:
            x.remove('4.5')
            x.append('4_5')

        if '1' in x:
            a *= 1.10
            x.remove('1')

        if '2' in x:
            a *= 1.15
            x.remove('2')

        if '3' in x:
            a *= 1.23
            x.remove('3')

        if '4' in x:
            a *= 1.35
            x.remove('4')

        if '4_5' in x:
            a *= 1.40
            x.remove('4_5')

        if '5' in x:
            a *= 1.55
            x.remove('5')

        if 'leg' in x:
            a *= 1.55
            alpha = raw * 0.06
            x.remove('leg')

        if 'legend' in x:
            a *= 1.55
            alpha = raw * 0.06
            x.remove('legend')

        alldmg = raw * osraw * a + alpha
        return alldmg, a


async def ctcalc(ctx: discord.ApplicationContext, raw: float, perkraw: float, x: list):
    a = 1.0
    if '1' in x:
        a *= 0.95
        x.remove('1')

    if '2' in x:
        a *= 0.90
        x.remove('2')

    if '3' in x:
        a *= 0.84
        x.remove('3')

    if '4' in x:
        a *= 0.77
        x.remove('4')

    if '4_5' in x:
        a *= 0.72
        x.remove('4_5')

    if '5' in x:
        a *= 0.60
        x.remove('5')

    ct = raw * perkraw * a
    return ct, a


async def tokkoulist(ctx, dmg, os_power, tokkou):
    tokkou = list(tokkou)
    tokkou_list = list(tokkou)
    tokkou_add = 1.0
    alpha = 0
    if len(tokkou) == 0:
        dmg_all = dmg * os_power
        return dmg_all, tokkou_add

    elif 1 <= len(tokkou) <= 5:
        if '4.5' in tokkou:
            tokkou.remove('4.5')
            tokkou.append('4_5')
            print(tokkou)



        if len(tokkou) != len(tokkou_list):
            print("$")
            await ctx.send(f"{ctx.author.mention}, 重複しています。")

        elif (str("4_5") in tokkou) and (str("5") in tokkou):
            await ctx.send(f"{ctx.author.mention}, 4_5と5は同時に装着できません")

        elif (str('4_5') in tokkou) and (str('leg') in tokkou):
            await ctx.send(f"{ctx.author.mention}, 4_5とLEGEND石は同時に装着できません")

        elif (str('leg') in tokkou) and (str('5') in tokkou):
            await ctx.send(f"{ctx.author.mention}, 5とLEGEND石は同時に装着できません")

        else:
            if str('1') in tokkou:
                tokkou_add *= 1.1
                tokkou.remove("1")

            if str('2') in tokkou:
                tokkou_add *= 1.15
                tokkou.remove("2")

            if str('3') in tokkou:
                tokkou_add *= 1.23
                tokkou.remove("3")

            if str('4') in tokkou:
                tokkou_add *= 1.35
                tokkou.remove('4')

            if str('4_5') in tokkou:
                tokkou_add *= 1.40
                tokkou.remove("4_5")

            if str('5') in tokkou:
                tokkou_add *= 1.55
                tokkou.remove("5")

            if str('leg') in tokkou:
                alpha = (dmg * 0.06)
                tokkou_add *= 1.55
                tokkou.remove("leg")

                #####
            alldmg = dmg * os_power * tokkou_add + alpha
            return alldmg, tokkou_add


async def embed_list(ctx, dmg, raw, os, osraw, r, alpha, now):  # dmg: 魔法石込み
    embed_1 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ノービス**")

    embed_1.set_author(name=ctx.author.name)

    embed_1.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_1.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * osraw:.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * osraw:.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * osraw:.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * osraw:.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_1.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osraw:.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_1.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * osraw:.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_1.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * osraw:.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * osraw:.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * osraw:.3f}__**',
                      inline=False)

    embed_1.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osraw:.3f}__**', inline=False)

    embed_1.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * osraw:.3f}**__')

    embed_1.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * osraw:.3f} / 通常mob {dmg * 0.7 * osraw:.3f}__**',
                      inline=False)

    # ソルジャー
    embed_2 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ソルジャー**")

    embed_2.set_author(name=ctx.author.name)

    embed_2.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_2.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * 0.98 * (osraw - 0.02):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.02):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.02):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * 0.98 * (osraw - 0.02):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_2.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.02):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.02):.3f}**__')

    embed_2.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw + 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.05):.3f}__**',
                      inline=False)

    # アーチャー
    embed_3 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：アーチャー**")

    embed_3.set_author(name=ctx.author.name)

    embed_3.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_3.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.02):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.02):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.02):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.02):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_3.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.05):.3f}**__')

    embed_3.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.02):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.02):.3f}__**',
                      inline=False)

    # マジシャン
    embed_4 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：マジシャン**")

    embed_4.set_author(name=ctx.author.name)

    embed_4.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_4.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.05):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.05):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw + 0.05):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.05):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_4.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.02):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.02):.3f}**__')

    embed_4.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.02):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.02):.3f}__**',
                      inline=False)

    # ウォーリア
    embed_5 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ウォーリア**")

    embed_5.set_author(name=ctx.author.name)

    embed_5.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_5.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.05):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.05):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.05):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.05):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_5.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.10):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.05):.3f}**__')

    embed_5.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw + 0.10):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.10):.3f}__**',
                      inline=False)

    # ボウマン
    embed_6 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ボウマン**")

    embed_6.set_author(name=ctx.author.name)

    embed_6.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}魔法石倍率：{alpha}倍')

    embed_6.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.05):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.05):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.05):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.05):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_6.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.05):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw + 0.10):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.10):.3f}__, パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.10):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.10):.3f}**__')

    embed_6.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.05):.3f}__**',
                      inline=False)

    # メイジ
    embed_7 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：メイジ**")

    embed_7.set_author(name=ctx.author.name)

    embed_7.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_7.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.10):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.10):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw + 0.10):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.10):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_7.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.05):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.05):.3f}**__')

    embed_7.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_8 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ロウニン**")

    embed_8.set_author(name=ctx.author.name)

    embed_8.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_8.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.04):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.04):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.04):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * osraw:.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_8.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.04):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.04):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.04):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.04):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.04):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.04):.3f}**__')

    embed_8.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.04):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.04):.3f}__**',
                      inline=False)

    # ドラゴンキラー
    embed_9 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ドラゴンキラー**")

    embed_9.set_author(name=ctx.author.name)

    embed_9.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_9.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.02):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.02):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.02):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.02):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_9.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_9.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_9.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_9.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_9.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.05):.3f}**__')

    embed_9.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.02):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.02):.3f}__**',
                      inline=False)

    # プリースト
    embed_10 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：プリースト**")

    embed_10.set_author(name=ctx.author.name)

    embed_10.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_10.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.10):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.10):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw - 0.10):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.10):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_10.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.10):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.10):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.10):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.10):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.10):.3f}**__')

    embed_10.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.10):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.10):.3f}__**',
                       inline=False)

    # スカ―ミッシャー
    embed_11 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：スカ―ミッシャー**")

    embed_11.set_author(name=ctx.author.name)

    embed_11.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_11.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * osraw:.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * osraw:.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * osraw:.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * osraw:.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_11.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_11.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * osraw:.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_11.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * osraw:.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * osraw:.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * osraw:.3f}__**',
                       inline=False)

    embed_11.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_11.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * osraw:.3f}**__')

    embed_11.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw + 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.05):.3f}__**',
                       inline=False)

    # ハグレモノ
    embed_12 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：ハグレモノ**")

    embed_12.set_author(name=ctx.author.name)

    embed_12.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_12.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.07):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.07):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * osraw:.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.07):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_12.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw - 0.07:.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.07):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.07):.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.07):.3f}**__')

    embed_12.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.07):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.07):.3f}__**',
                       inline=False)

    # ルーンキャスター
    embed_13 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：ルーンキャスター**")

    embed_13.set_author(name=ctx.author.name)

    embed_13.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_13.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.07):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.07):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw + 0.07):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.07):.3f}__**\n'
                             f'ファイヤ・ボルケーノ (ノーマル)**：__{dmg * 22 * (osraw + 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.07):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.07):.3f}**__')

    embed_13.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.07):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.07):.3f}__**',
                       inline=False)

    # スペランカー
    embed_14 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：スペランカー**")

    embed_14.set_author(name=ctx.author.name)

    embed_14.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_14.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.10) :.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.10):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw + 0.10):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.10):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_14.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.10):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw + 0.10):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.10):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.10):.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.10):.3f}**__')

    embed_14.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw + 0.10):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.10):.3f}__**',
                       inline=False)

    # アーサー
    embed_15 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：アーサー**")

    embed_15.set_author(name=ctx.author.name)

    embed_15.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_15.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * osraw :.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * osraw :.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * osraw :.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * osraw :.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_15.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * osraw :.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw :.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * osraw :.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw :.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * osraw :.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * osraw :.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * osraw :.3f}**__')

    embed_15.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw + 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.05):.3f}__**',
                       inline=False)

    # シーカー
    embed_16 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(), timestamp=now,
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：シーカー**")

    embed_16.set_author(name=ctx.author.name)

    embed_16.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_16.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.07):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.07):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw - 0.07):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.07):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_16.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * (osraw + 0.07):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.07):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.07):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.07):.3f}**__')

    embed_16.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.2 * (osraw - 0.07):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.07):.3f}__**',
                       inline=False)
    embed_lists = [
        embed_1, embed_2, embed_3, embed_4, embed_5, embed_6, embed_7, embed_8,
        embed_9, embed_10, embed_11, embed_12, embed_13, embed_14, embed_15, embed_16
    ]
    return embed_lists
