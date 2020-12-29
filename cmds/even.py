import discord
import time
from discord.ext import commands
from core.classes import Cog_Extension
import json
import os

#intents = discord.Intents.all()
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)
roledata =[]
num = 0
for i in jdata['role']:
    num+=1
    roledata.append(i)
num2 = num//2
class even(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.author.id == 528227414678044672 and msg.content == 'Boo':
            await msg.channel.send('boom')
        if self.bot.user in msg.mentions:
            await msg.add_reaction(self.bot.get_emoji(int(710157216057131028)))
        if '早安' in str(msg.content) and msg.author != self.bot.user:
            await msg.channel.send(str(msg.author)+' 早安！')
        if '晚安' in str(msg.content) and msg.author != self.bot.user:
            await msg.channel.send(str(msg.author)+' 晚安！')
        if str(msg.content) == '安安' and msg.author != self.bot.user:
            await msg.channel.send(str(msg.author)+' 安安')
        if str(msg.content) == '早' and msg.author != self.bot.user:
            await msg.add_reaction('👍')
            await msg.channel.send(str(msg.author)+' 早呀')
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user:
            print(str(msg.author) + '說:' + msg.content)
        else:
            if str(msg.channel.type) == 'text' and msg.guild.id == 706889259692589077 and msg.author != self.bot.user:
                print(str(msg.author) + '說:' + msg.content)
                a = str(msg.guild)
                b = str(msg.channel)
                fp = open('./log/'+a+'-'+b+'.txt', 'a',encoding='utf8')
                fp.write(str(msg.author) + '說:' + msg.content+'\n')
                fp.close()
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,pl):
        guild = self.bot.get_guild(pl.guild_id)
        for releadd in range(num):
            if str(pl.message_id) == jdata['msgid'] and str(pl.emoji) == roledata[releadd]:
                role = guild.get_role(int(roledata[releadd+1]))
                await pl.member.add_roles(role)
                print('已給予'+str(pl.member)+' 的 '+str(role)+'身分組')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,pl):
        guild = self.bot.get_guild(pl.guild_id)
        for releadd in range(num):
            if str(pl.message_id) == jdata['msgid'] and str(pl.emoji) == roledata[releadd]:
                role = guild.get_role(int(roledata[releadd+1]))
                memb = guild.get_member(pl.user_id)
                await memb.remove_roles(role)
                print('已移除'+str(memb)+' 的 '+str(role)+'身分組')
#"""
    @commands.Cog.listener()
    async def on_member_join(self,member):
        with open('levelmembers.json','r',encoding='utf8') as jfile2:
            jdata2 = json.load(jfile2)
        if member.guild.id == int(706889259692589077):
            guild = self.bot.get_guild(706889259692589077)
            role = guild.get_role(int(707439119176826880))
            await member.add_roles(role)
            print(str(member)+'已加入server 並且給予了'+role.name+'身分組')
            if member.id in jdata2['members']:
                channel = member.guild.get_channel(775054378540859434)
                await channel.send('小拉基回歸{}'.format(member.id))
  
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        if member.guild.id == int(706889259692589077):
            with open('levelmembers.json','r',encoding='utf8') as jfile2:
                jdata2 = json.load(jfile2)
                jdata2['members'].append(member.id)
            with open('levelmembers.json','w',encoding='utf8') as jfile2:
                json.dump(jdata2,jfile2,indent = 4)
            channel = member.guild.get_channel(775302781320822805)
            await channel.send('小拉基退出{}'.format(member.id))


def setup(bot):
    bot.add_cog(even(bot))