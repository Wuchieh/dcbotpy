import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

class test(Cog_Extension):
    @commands.command()
    async def test(self,ctx,*msg):
        await ctx.message.delete()
        if msg == ():
            pass
        else:
            message = ''
            for i in msg:
                message += i+' '
            await ctx.send(message)
def setup(bot):
    bot.add_cog(test(bot))