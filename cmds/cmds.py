import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

class cmds(Cog_Extension):
    @commands.command()
    async def system(self,ctx,*,cmd):
        if str(ctx.message.author.id) == jdata['owner']:
            os.system(cmd)

def setup(bot):
    bot.add_cog(cmds(bot))