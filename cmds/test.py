import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

class test(Cog_Extension):
    @commands.command()
    async def test(self,ctx,gid):
        guild = self.bot.get_guild(int(gid))
        msg = ''
        for test in self.bot.get_all_channels():
            if str(type(test)) == str(discord.channel.VoiceChannel) and test.guild == guild:
                print(str(test) +'('+ str(test.id)+')')
                msg = msg + str(test) +'('+ str(test.id)+')\n'
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(test(bot))