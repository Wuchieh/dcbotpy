import discord
from discord.ext import commands
import os
import json
from core.classes import Cog_Extension

testStatus = []

class test(Cog_Extension):
    #@commands.Cog.listener()
    
    @commands.command()
    async def test(self,ctx,uid):
        with open('levelmembers.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
            jdata['members'].append(uid)
        with open('levelmembers.json','w',encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent = 4)
            
def setup(bot):
    bot.add_cog(test(bot))