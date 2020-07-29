import discord
from discord.ext import commands
from core.classes import Cog_Extension

class cmds(Cog_Extension):
    @commands.command()
    async def example(self,ctx):
        pass

def setup(bot):
    bot.add_cog(cmds(bot))