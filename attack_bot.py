from typing import AsyncContextManager
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    damage_add = 1
    # '.damage' と入力を受け取ったとき
    if message.content.startswith('.damage'):
        tokkou = str(message.content)
        tokkou_value = tokkou[7:]

        # メッセージの中に '特攻' が含まれているとき
        if 1 in tokkou_value:
            int(damage_add) *= 1.1

        if 2 in tokkou_value:
            int(damage_add) *= 1.15
        
        if 3 in tokkou_value:
            int(damage_add) *= 1.23
        
        if 4 in tokkou_value:
            int(damage_add) *= 1.35
        
        if 4_5 in tokkou_value:
            int(damage_add) *= 1.4
        
        if 5 in tokkou_value:
            int(damage_add) *= 1.55
    
    print(int(damage_add))
    await message.channel.send(f"{message.author.mention} 、{int(damage_add)}")

client.run('ODg0OTg2ODY2MjIxMzI2MzQ3.YTgePw.jvxLNGUcSseqwjKRcssHSM8SooY')
