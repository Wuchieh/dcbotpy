import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import os

#intents = discord.Intents.all()

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
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user:
            user = self.bot.get_user(int(490201803661508630))
            user2 = self.bot.get_user(int(jdata['owner']))
            print(msg.content)
            await user2.send(str(msg.author)+':\n'+str(msg.content))
            await user.send(str(msg.author)+':\n'+str(msg.content))
        if '<@!656761631224758282>' in str(msg.content):
            await msg.add_reaction(self.bot.get_emoji(int(710157216057131028)))
        if '<@656761631224758282>' in str(msg.content):
            await msg.add_reaction(self.bot.get_emoji(int(710157216057131028)))
        if '<@&656761631224758282>' in str(msg.content):
            await msg.add_reaction(self.bot.get_emoji(int(710157216057131028)))
        if '早安' in str(msg.content) and msg.author != self.bot.user:
            await msg.channel.send(str(msg.author)+'早安')
        #if msg.author.id == 462698977331249172:
        #    await msg.delete()
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
                user = guild.get_member(int(pl.user_id))
                role = guild.get_role(int(roledata[releadd+1]))
                await pl.member.add_roles(role)
                print('已給予身分組')
            if str(pl.message_id) == jdata['msgid2'] and str(pl.emoji) == roledata[releadd]:
                role = guild.get_role(int(roledata[releadd+1]))
                await pl.member.add_roles(role)
                print('已給予身分組')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,pl):
        guild = self.bot.get_guild(pl.guild_id)
        for releadd in range(num):
            if str(pl.message_id) == jdata['msgid'] and str(pl.emoji) == roledata[releadd]:
                role = guild.get_role(int(roledata[releadd+1]))
                memb = guild.get_member(pl.user_id)
                await memb.remove_roles(role)
                print('已移除身分組')
            if str(pl.message_id) == jdata['msgid2'] and str(pl.emoji) == roledata[releadd]:
                memb = guild.get_member(pl.user_id)
                role = guild.get_role(int(roledata[releadd+1]))
                await memb.remove_roles(role)
                print('已移除身分組')
    

def setup(bot):
    bot.add_cog(even(bot))