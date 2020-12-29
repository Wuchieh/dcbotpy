import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

class cmds(Cog_Extension):
    @commands.command()
    async def guilds(self,ctx):
        guilds = self.bot.guilds
        message = '```py\n'
        for i in guilds:
            message += 'name = {}, ID = {}\n'.format(i.name,i.id)
            print('name = {}, ID = {}'.format(i.name,i.id))
        message+='```'
        await ctx.send(message)
    
    @commands.command()
    async def channels(self,ctx,guildid:str='/0'):
        if guildid == '/0':
            guild = ctx.guild
        else:
            guild = self.bot.get_guild(int(guildid))
        if guild == None:
            await ctx.send('Guild Id Error')
            return
        message = '```py\n'
        channels = guild.channels
        for i in channels:
            message += 'name = {}, ID = {}\n'.format(i.name,i.id)
            if len(message)>2000:
                num = len('name = {}, ID = {}\n'.format(i.name,i.id))
                message = message[:-num]
                message += '```'
                await ctx.send(message)
                message = '```py\n'
                message += 'name = {}, ID = {}\n'.format(i.name,i.id)
            print('name = {}, ID = {}'.format(i.name,i.id))
        message += '```'
        await ctx.send(message)

    @commands.command()
    async def members(self,ctx,guildid:str='/0'):
        if guildid == '/0':
            guild = ctx.guild
        else:
            guild = self.bot.get_guild(int(guildid))
        if guild == None:
            await ctx.send('Guild Id Error')
            return
        members = guild.members
        message = '```css\n'
        for i in members:
            message += 'name = {}, ID = {}\n'.format(i.name,i.id)
            if len(message)>2000:
                num = len('name = {}, ID = {}\n'.format(i.name,i.id))
                message = message[:-num]
                message += '```'
                await ctx.send(message)
                message = '```py\n'
                message += 'name = {}, ID = {}\n'.format(i.name,i.id)
            print('name = {}, ID = {}'.format(i.name,i.id))
        message += '```'
        await ctx.send(message)

def setup(bot):
    bot.add_cog(cmds(bot))