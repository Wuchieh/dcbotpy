import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

class test(Cog_Extension):
    @commands.command()
    async def test(self,ctx,gid):
        print(self.bot.id)

def setup(bot):
    bot.add_cog(test(bot))