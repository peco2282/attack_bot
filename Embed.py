# import nextcord as discord

embed_1_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
embed_1_job.set_author(name=f"By {message.author}")

embed_1_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n魔法石： {raw_tokkou}')
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

embed_2_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

embed_2_job.set_author(name=f"By {message.author}")
embed_2_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n魔法石： {raw_tokkou}')

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

embed_3_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

embed_3_job.set_author(name=f"By {message.author}")
embed_3_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n魔法石： {raw_tokkou}')
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

embed_4_job = discord.Embed(title='職業', color=discord.Color.dark_green(), timestamp=datetime.utcnow(),
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

embed_4_job.set_author(name=f"By {message.author}")
embed_4_job.add_field(name='条件', value=f'素火力： {dmg}\nOS： {os}\nOS倍率： {os_raw_power}\n魔法石： {raw_tokkou}')

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
