import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

class test(Cog_Extension):
    @commands.command()
    async def test(self,ctx,gid):
        guild = self.bot.get_guild(ctx.guild.id)
        print(guild)
        print(gid)
        print(type(gid))
        userid = int(gid)
        print(type(userid))
        user = guild.get_member(476422785833631749)
        print(user)

def setup(bot):
    bot.add_cog(test(bot))