import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

class cmds(Cog_Extension):
    @commands.command()
    async def cmds(self,ctx,msgid,*,remsg):
        if ctx.author.id == jdata['owner']:
            await ctx.message.delete()
            guild = self.bot.get_guild(ctx.message.guild.id)
            channel = guild.get_channel(ctx.message.channel.id)
            msg = await channel.fetch_message(msgid)
            await msg.edit(content=remsg)

def setup(bot):
    bot.add_cog(cmds(bot))