# coding=utf-8
import discord


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

