import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    def __init__(self,bot):
        self.bot = bot 

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)} 毫秒')

def setup(bot):
    bot.add_cog(Main(bot))