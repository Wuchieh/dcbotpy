import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

testStatus = []

class test(Cog_Extension):
    @commands.command()
    async def test(self,ctx):
        embed=discord.Embed()
        embed.set_footer(text='||測試||')
        await ctx.send('||測試||',embed=embed)
            
def setup(bot):
    bot.add_cog(test(bot))