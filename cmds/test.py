import discord
from discord.ext import commands
from core.classes import Cog_Extension

class test(Cog_Extension):
    @commands.command()
    async def test(self,ctx):
        await ctx.send(str(ctx.message.author))



def setup(bot):
    bot.add_cog(test(bot))