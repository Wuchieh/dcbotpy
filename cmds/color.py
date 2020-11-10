import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json

rolesid = [775585310951342082,775585420968460288,775585536462946325]

class color(Cog_Extension):
    @commands.group()
    async def color(self,ctx):
        #print(rolesid)
        pass

    @color.command()
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
        
    @color.command()
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
        
    @color.command()
    async def blue(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        adrole = guild.get_role(775585420968460288)
        member = guild.get_member(ctx.author.id)
        await member.add_roles(adrole)
        rolesid.remove(adrole.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        rolesid.append(adrole.id)
        await ctx.send(str(member) +' 已變更顏色')
    
    @color.command()
    async def clean(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        member = guild.get_member(ctx.author.id)
        for i in rolesid:
            rerole = guild.get_role(i)
            await member.remove_roles(rerole)
        await ctx.send(str(member)+' 已清除顏色')

def setup(bot):
    bot.add_cog(color(bot))