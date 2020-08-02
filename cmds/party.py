import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

class party(Cog_Extension):
    @commands.group()
    async def party(self,ctx):
        pass
    @party.command()
    async def invite(self,ctx):
        await ctx.send("邀請玩家加入隊伍")
    @party.command()
    async def leave(self,ctx):
        await ctx.send("離開隊伍")
    @party.command()
    async def list(self,ctx):
        await ctx.send("顯示隊伍清單")

def setup(bot):
    bot.add_cog(party(bot))