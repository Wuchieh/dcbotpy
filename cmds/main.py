import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)} 毫秒')

    @commands.command()
    async def ran(self,ctx):
        rannum = random.randint(1,10)
        await ctx.send(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
        print(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
        

def setup(bot):
    bot.add_cog(Main(bot))