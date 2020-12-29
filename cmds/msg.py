import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import os
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)
banmsguserid = []
onMessageUser = int()
def chonMessageUser(a):
    global onMessageUser
    onMessageUser = a
class Msg(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        try:
            if msg.author.id in banmsguserid:
                await msg.delete()
        except discord.errors.NotFound:
            pass
        if msg.content[:1] == jdata['command_prefix']:
            return
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and str(msg.author.id) != jdata['owner']:
            user2 = self.bot.get_user(int(jdata['owner']))
            print(msg.content)
            if msg.author.id == onMessageUser:
                await user2.send(str(msg.content))
            else:
                await user2.send(str(msg.author)+'('+str(msg.author.id)+')：\n'+str(msg.content))
                chonMessageUser(msg.author.id)
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and str(msg.author.id) == jdata['owner']:
            user = self.bot.get_user(int(onMessageUser))
            await user.send(msg.content)
        pass
    
    @commands.command()
    async def setuserid(self,ctx,userid:int=0):
        if ctx.author.id == int(jdata['owner']):
            if userid != 0 and len(str(userid)) == 18:
                user = self.bot.get_user(userid)
                if user != None:
                    chonMessageUser(int(userid))

    @commands.command()
    async def sayd(self,ctx,*,msg:str='/0'):
        await ctx.message.delete()
        if msg == '/0':
            pass
        else:
            await ctx.send(msg)
    
    @commands.command()
    async def edit(self,ctx,msgid,*,remsg):
        if ctx.author.id == int(jdata['owner']):
            await ctx.message.delete()
            guild = self.bot.get_guild(ctx.message.guild.id)
            channel = guild.get_channel(ctx.message.channel.id)
            msg = await channel.fetch_message(msgid)
            await msg.edit(content=remsg)
    
    @commands.command()
    async def tts(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg, tts=True)
        print('{}說:{}'.format(ctx.message.author,msg))
        #print(str(ctx.message.author) +'說:'+ msg)
        
    @commands.command()
    async def banmsg(self,ctx):
        if ctx.message.author.id == ctx.guild.owner_id or str(ctx.message.author.id) == jdata['owner']:
            await ctx.message.delete()
            a=0
            for i in ctx.message.mentions:
                if i.id in banmsguserid and a == 0:
                    await ctx.send('此人已被BanMsg')
                    a+=1
                else:
                    banmsguserid.append(i.id)
        else:
            await ctx.send('權限不足 本指令只提供給伺服器傭有者 \n本伺服器傭有者為 <@{}>'.format(ctx.guild.owner_id))

        
    @commands.command()
    async def banmsglist(self,ctx):
        guild = ctx.guild
        a=0
        message ='```css'
        for i in banmsguserid:
            member = guild.get_member(i)
            message+='\n{}'.format(member)
            a+=1
        message += '\n```'
        if a == 0:
            await ctx.send('```css\n尚未有人被BanMsg\n```')
        else:
            await ctx.send(message)

    @commands.command()
    async def unbanmsg(self,ctx):
        if ctx.message.author.id == ctx.guild.owner_id or str(ctx.message.author.id) == jdata['owner']:
            await ctx.message.delete()
            a=0
            for i in ctx.message.mentions:
                if i.id not in banmsguserid and a == 0:
                    await ctx.send('此人尚未被BanMsg')
                    a+=1
                else:
                    banmsguserid.remove(i.id)
        else:
            await ctx.send('權限不足 本指令只提供給伺服器傭有者 \n本伺服器傭有者為 <@{}>'.format(ctx.guild.owner_id))

    @commands.command(aliases=['su'])
    async def senduser(self,ctx,userid: int=0,*,msg:str='\0'):
        if ctx.author.id == int(jdata['owner']):
            if userid == 0:
                pass
            else:
                user = self.bot.get_user(int(userid))
                if user == None:
                    pass
                else:
                    if msg == '\0':
                        pass
                    else:
                        await user.send(msg)
        pass

    @commands.command()
    async def help(self,ctx):
        await ctx.send('```css\n'
        +str(jdata['command_prefix'])+'ping 顯示機器人延遲\n'
        +str(jdata['command_prefix'])+'ran 骰子遊戲1~10\n'
        +str(jdata['command_prefix'])+'clear [num] 刪除指定數量的聊天內容\n'
        +str(jdata['command_prefix'])+'sayd [msg] 使機器人說話\n'
        #+str(jdata['command_prefix'])+'member 顯示伺服器中所有人的狀態\n'
        #+str(jdata['command_prefix'])+'offline 顯示離線名單\n'
        #+str(jdata['command_prefix'])+'online 顯示上線名單\n'
        +str(jdata['command_prefix'])+'user 顯示個人訊息(管理員Debug用)\n'
        +str(jdata['command_prefix'])+'ms 開始踩地雷遊戲 請找管理員開啟\n'
        +str(jdata['command_prefix'])+'color help 顏色修改提示\n'
        +str(jdata['command_prefix'])+'math [整數20~50] 開始math遊戲\n'
        +str(jdata['command_prefix'])+'ooxx 開始OOXX遊戲\n'
        +str(jdata['command_prefix'])+'snake 貪吃蛇(分數上限：88)\n'
        +'=============AABB=============\n'
        +str(jdata['command_prefix'])+'aabb help 顯示AABB遊戲提示\n'
        +str(jdata['command_prefix'])+'aabb s 開始終極密碼\n'
        +str(jdata['command_prefix'])+'autoreset 終極密碼自動重啟\n'
        #+str(jdata['command_prefix'])+'invite [tag玩家] 邀請他人進入目前語音頻道'
        +'```')

    
    @commands.command()
    async def emmsg(self,ctx,msgid,em):
        msg = await ctx.message.channel.fetch_message(int(msgid))
        print(msg.content)
        await ctx.message.delete()
        if len(em)<18:
            await msg.add_reaction(em)
        else:
            emoji = self.bot.get_emoji(int(((em.split('>'))[0])[-18:]))
            await msg.add_reaction(emoji)

    @commands.command()
    async def clear(self,ctx,num:int):
        if ctx.message.author.id == ctx.guild.owner_id or str(ctx.message.author.id) == jdata['owner']:
            purge = await ctx.channel.purge(limit=num+1)
            if len(purge) >= 50 :
                await ctx.send('https://tenor.com/view/explode-blast-blow-nuclear-boom-gif-15025770')
            print('{} ---ID {}在 << {} >> 頻道使用了clear指令刪除了{}個對話'.format(ctx.message.author,ctx.message.author.id,ctx.channel.name,len(purge)-1))
        else:
            await ctx.send('權限不足 本指令只提供給伺服器傭有者 \n本伺服器傭有者為 <@{}>'.format(ctx.guild.owner_id))

def setup(bot):
    bot.add_cog(Msg(bot))