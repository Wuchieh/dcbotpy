import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

rolesid = [775585310951342082,775752050503843890,775585536462946325,778252768560939019,778252956586737674]
roles = []
def colorRole(a):
    color={
        'red' : 775585310951342082,
        'blue' : 775752050503843890,
        'green' : 775585536462946325,
        'yellow' : 778252768560939019,
        'purple' : 778252956586737674
    }
    return color.get(a,None)
class color(Cog_Extension):
    
    @commands.group()
    async def color(self,ctx,index:str="help"):
        if roles == []:
                for i in rolesid:
                    role = ctx.guild.get_role(i)
                    roles.append(role)
        if index == "help":
            await ctx.send('```css\n'
        + jdata['command_prefix']+'color red 將名子改成紅色\n'
        + jdata['command_prefix']+'color blue 將名子改成藍色\n'
        + jdata['command_prefix']+'color green 將名子改成綠色\n'
        + jdata['command_prefix']+'color yellow 將名子改成黃色\n'
        + jdata['command_prefix']+'color purple 將名子改成紫色\n'
        + jdata['command_prefix']+'color clean 將名子顏色清除\n'
        +'```')
        elif index == 'clear':
            await ctx.author.remove_roles(*roles)
        else:
            role = ctx.guild.get_role(colorRole(index))
            if role == None:
                await ctx.send('請檢查是否有錯字')
            else:
                await ctx.author.remove_roles(*roles)
                await ctx.author.add_roles(role)
                await ctx.send(str(ctx.author) +' 已變更顏色')
        pass

def setup(bot):
    bot.add_cog(color(bot))