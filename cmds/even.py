import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import os
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)
roledata =[]
roledata2 =[]
num = 0
for i in jdata['role']:
    num+=1
    roledata.append(i)
num2 = num//2
for roleadd in range(num2):
    roledata2.append(roledata[roleadd*2])
class even(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        arg = msg.channel
        CMD = 'Direct Message with'
        CMDs = CMD.split(' ')
        args = str(arg).split(' ')
        if msg.author.id == 656761631224758282 and msg.content == '<:lol:750374968864276570>  : 英雄聯盟（League of Legends）\n\n<:GTA:750374967786471466>  : 俠盜獵車手系列（Grand Theft Auto 1~5）\n\n<:R6:750374968113496123>  : 虹彩六號（Rainbow Six Siege）\n\n<:pubg:750374968407097384>  : 絕地求生（PlayerUnknown'+jdata['ss']+'s Battlegrounds）\n\n<:VALORANT:750374968105238630>  : 特戰英豪／瓦羅蘭（VALORANT）':
            for om in roledata2:
                u1,u2,u3 = om.split(':')
                print(om,u1,u2,u3)
                u4,u5 = u3.split('>')
                print(u4,u5)
                await msg.add_reaction(self.bot.get_emoji(int(u4)))
        if CMDs[0] == args[0] and CMDs[1] == args[1] and CMDs[2] == args[2] and msg.author != self.bot.user:
            user = self.bot.get_user(int(jdata['owner']))
            print(msg.content)
            await user.send(str(msg.author)+':\n'+str(msg.content))
        if '<@!656761631224758282>' in str(msg.content):
            await msg.add_reaction(self.bot.get_emoji(int(710157216057131028)))
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,pl):
        guild = self.bot.get_guild(pl.guild_id)
        for releadd in range(num):
            if str(pl.message_id) == jdata['msgid'] and str(pl.emoji) == roledata[releadd]:
                print('已給予身分組')
                role = guild.get_role(int(roledata[releadd+1]))
                await pl.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,pl):
        guild = self.bot.get_guild(pl.guild_id)
        for releadd in range(num):
            if str(pl.message_id) == jdata['msgid'] and str(pl.emoji) == roledata[releadd]:
                print('已移除身分組')
                user = guild.get_member(pl.user_id)
                role = guild.get_role(int(roledata[releadd+1]))
                await user.remove_roles(role)

def setup(bot):
    bot.add_cog(even(bot))