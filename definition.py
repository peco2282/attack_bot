import random

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

