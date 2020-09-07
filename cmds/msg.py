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
num = num//2
for roleadd in range(num):
    roledata2.append(roledata[roleadd*2])
class Msg(Cog_Extension):

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
        print(str(ctx.message.author) +'說:'+ msg)
    
    @commands.command()
    async def tts(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg, tts=True)
        print(str(ctx.message.author) +'說:'+ msg)
        
    @commands.command()
    async def send(self,ctx,userid,*,msg):
        user = self.bot.get_user(int(userid))
        await user.send(msg)

    @commands.command()
    async def sendch(self,ctx,chid,*,msg):
        ch = self.bot.get_channel(int(chid))
        await ch.send(msg)
    
    @commands.command()
    async def 身分組(self,ctx):
        await ctx.message.delete()
        await ctx.send('<:lol:750374968864276570>  : 英雄聯盟（League of Legends）\n\n'
        '<:GTA:750374967786471466>  : 俠盜獵車手系列（Grand Theft Auto 1~5）\n\n'
        '<:R6:750374968113496123>  : 虹彩六號（Rainbow Six Siege）\n\n'
        '<:pubg:750374968407097384>  : 絕地求生（PlayerUnknown'+jdata['ss']+'s Battlegrounds）\n\n'
        '<:VALORANT:750374968105238630>  : 特戰英豪／瓦羅蘭（VALORANT）')

    @commands.command()
    async def 身分組2(self,ctx):
        await ctx.message.delete()
        await ctx.send('<:Warframe:752543133988028469>  : 戰甲神兵（Warframe）\n\n'
        '<:TheDivision:752363812329488384>  : 全境封鎖（The Division ™）\n\n'
        '<:TheDivision2:752363837260562472>   : 全境封鎖2（The Division 2®）\n\n'
        '<:Minecraft:752529033006153778>   : 當個創世神（Minecraft）\n\n'
        '<:Fallguys:752543133706748036>   : 糖豆人（Fall Guys）\n\n'
        '<:L4D2:752561204186054686> : 惡靈勢力2（Left 4 Dead 2）')

    @commands.command()
    async def clear(self,ctx,num:int):
        if ctx.message.author.id == ctx.guild.owner_id or str(ctx.message.author.id) == jdata['owner']:
            await ctx.channel.purge(limit=num+1)
            #await ctx.send('https://tenor.com/view/explode-blast-blow-nuclear-boom-gif-15025770')
            print(str(ctx.message.author)+' ---ID '+str(ctx.message.author.id)+
            '在 << '+str(ctx.channel.name)+' >> 頻道使用了clear指令刪除了'+str(int(num))+'個對話')
        else:
            await ctx.send('權限不足 本指令只提供給伺服器傭有者 \n本伺服器傭有者為 <@' + str(ctx.guild.owner_id) + '>')

def setup(bot):
    bot.add_cog(Msg(bot))