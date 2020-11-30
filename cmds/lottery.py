import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
import random
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)


class lottery(Cog_Extension):
    @commands.command()
    async def lottery(self,ctx):
        await ctx.message.delete()
        if str(ctx.author.id) == jdata['owner']:
            embed=discord.Embed(title="抽獎", color=0xf54242)
            embed.add_field(name="一月抽獎活動", value="獎品 ： discord classic 一個月", inline=False)
            embed.set_footer(text="點擊下方圖標參加")
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('💰')
    

    @commands.command()
    async def lotend(self,ctx,msgid):
        if str(ctx.author.id) == jdata['owner']:
            member = ['581794418764415020','416213146408189952','225605610022895616','631823065067552769','667984215282941962','457924239627124736'] #中獎率加倍
            msg = await ctx.message.channel.fetch_message(msgid)
            msgreaction = msg.reactions
            for i in msgreaction:
                if i.emoji == '💰':
                    async for user in i.users():
                        member.append(str(user.id))
                    member.remove(str(self.bot.user.id))
                    print(member)
            winer = random.choice(member)
            overmsg = '@everyone \n 獲獎者為 <@' + winer + '>'
            await msg.edit(content=overmsg)
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(lottery(bot))