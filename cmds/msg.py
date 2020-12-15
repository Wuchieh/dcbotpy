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
        if ',setuserid' in msg.content:
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
    async def sayd(self,ctx,*msg):
        await ctx.message.delete()
        if msg == ():
            pass
        else:
            message = ''
            for i in msg:
                message += i+' '
            await ctx.send(message)
    
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
    async def 身分組(self,ctx):
        await ctx.message.delete()
        emoji=['750374968864276570','750374967786471466','750374968113496123','750374968407097384','750374968105238630','752561204186054686','752363837260562472','752543133988028469','752529033006153778','752543133706748036','773559447954915338','773559314169593896','775051504968400957']
        msg = await ctx.send("<:lol:750374968864276570> ： <@&775041162645864481>\n<:GTA:750374967786471466> ： <@&775049972663451650>\n<:R6:750374968113496123> ： <@&775050130360893500>\n<:pubg:750374968407097384> ： <@&775050314885365840>\n<:VALORANT:750374968105238630> ： <@&775050478400176178>\n<:L4D2:752561204186054686> ： <@&775050635497963530>\n<:TheDivision2:752363837260562472> ： <@&775050758608388097>\n<:Warframe:752543133988028469> ： <@&775050821641044038>\n<:Minecraft:752529033006153778> ： <@&775050825659711499>\n<:Fallguys:752543133706748036> ： <@&775050954755014729>\n<:ArenaOfValor:773559447954915338> ： <@&775050955347066891>\n<:ApexLegend:773559314169593896> ： <@&775050956056428595>\n<:among:775051504968400957> ： <@&775051174020644885>")
        print(msg.id)
        for i in emoji:
            bemoji = self.bot.get_emoji(int(i))
            await msg.add_reaction(bemoji)

    
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