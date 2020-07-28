import discord
from discord.ext import commands
from core.classes import Cog_Extension

class test(Cog_Extension):
    @commands.command()
    async def test(self,ctx):
        mes = str("")
        memberlist = ctx.guild.members
        onlinelist = []
        for i in memberlist:
            if str(i.status) == "online":
                mes = str(mes) + str(i) +' 在線\n'
                onlinelist.append(i.name)
            else:
                mes = str(mes) + str(i) +' 離線\n'
            #print(mes)
        await ctx.send(mes)
        for i2 in onlinelist:
            print(i2)

def setup(bot):
    bot.add_cog(test(bot))