import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

rolesid = [775585310951342082,775752050503843890,775585536462946325,778252768560939019,778252956586737674]

class color(Cog_Extension):
    @commands.group()
    async def color(self,ctx):
        #print(rolesid)
        pass

    @color.command(aliases=['Red','RED','紅色','紅'])
    async def red(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        adrole = guild.get_role(775585310951342082)
        member = guild.get_member(ctx.author.id)
        await member.add_roles(adrole)
        rolesid.remove(adrole.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        rolesid.append(adrole.id)
        await ctx.send(str(member) +' 已變更顏色')
        
    @color.command(aliases=['Green','GREEN','綠色','綠'])
    async def green(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        adrole = guild.get_role(775585536462946325)
        member = guild.get_member(ctx.author.id)
        await member.add_roles(adrole)
        rolesid.remove(adrole.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        rolesid.append(adrole.id)
        await ctx.send(str(member) +' 已變更顏色')
        
    @color.command(aliases=['Blue','BLUE','藍色','藍'])
    async def blue(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        adrole = guild.get_role(775752050503843890)
        member = guild.get_member(ctx.author.id)
        await member.add_roles(adrole)
        rolesid.remove(adrole.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        rolesid.append(adrole.id)
        await ctx.send(str(member) +' 已變更顏色')
    
        
    @color.command(aliases=['Yellow','YELLOW','黃色','黃'])
    async def yellow(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        adrole = guild.get_role(778252768560939019)
        member = guild.get_member(ctx.author.id)
        await member.add_roles(adrole)
        rolesid.remove(adrole.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        rolesid.append(adrole.id)
        await ctx.send(str(member) +' 已變更顏色')
    
        
    @color.command(aliases=['Purple','PURPLE','紫色','紫'])
    async def purple(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        adrole = guild.get_role(778252956586737674)
        member = guild.get_member(ctx.author.id)
        await member.add_roles(adrole)
        rolesid.remove(adrole.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        rolesid.append(adrole.id)
        await ctx.send(str(member) +' 已變更顏色')
    
    @color.command(aliases=['Clean','clear','Clear'])
    async def clean(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        member = guild.get_member(ctx.author.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        await ctx.send(str(member)+' 已清除顏色')
        
    @color.command()
    async def help(self,ctx):
        await ctx.send('```css\n'
        + jdata['command_prefix']+'color red 將名子改成紅色\n'
        + jdata['command_prefix']+'color blue 將名子改成藍色\n'
        + jdata['command_prefix']+'color green 將名子改成綠色\n'
        + jdata['command_prefix']+'color yellow 將名子改成黃色\n'
        + jdata['command_prefix']+'color purple 將名子改成紫色\n'
        + jdata['command_prefix']+'color clean 將名子顏色清除\n'
        +'```')

def setup(bot):
    bot.add_cog(color(bot))