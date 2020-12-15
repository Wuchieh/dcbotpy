import discord
import os
import json
from discord.ext import commands
from core.classes import Cog_Extension
import random
from threading import Timer
a=0
def time(tim):
    global a
    a+=1
    t=Timer(tim,time,args=(tim,))
    t.start()
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        global a
        await ctx.send(F'{round(self.bot.latency*1000)} 毫秒\n{a}')
        '''os.popen("ping -c 1 google.com")
        d = os.popen("ping google.com")
        d2 = str(d.read()).split('時間=')
        sec = 0
        for i in range(1, 5):
            d3 = d2[i].split('ms TTL')
            sec += int(d3[0])
        await ctx.send('網路延遲：'+ str(sec / 4) + '毫秒')'''

    @commands.command()
    async def ran(self,ctx):
        await ctx.message.delete()
        rannum = random.randint(1,10)
        await ctx.send(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
        print(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
      
    @commands.command()
    async def rans(self,ctx,min:int=10,max:int=10):
        await ctx.message.delete()
        rannum = random.randint(int(min),int(max))
        await ctx.send(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
        print(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
        
    @commands.command()
    async def kick(self,ctx,id,r):
      if ctx.message.author.id == ctx.guild.owner_id or str(ctx.message.author.id) == jdata['owner']:
        member = ctx.guild.get_member(int(id))
        await member.kick(reason=r)

    @commands.command()
    async def avatar(self,ctx,userid:str='0'):
        if str(ctx.message.author.id) == jdata['owner']:
            uid2 = userid.split('>')
            uid = int((uid2[0])[-18:])
            user = self.bot.get_user(int(uid))
            if user == None:
                await ctx.send('找不到指定用戶')
            else:
                asset = user.avatar_url
                await ctx.send(str(asset))
        else:
          await ctx.send('權限不足')

    @commands.command()
    async def move(self,ctx,id):
        await ctx.message.delete()
        if ctx.message.author.id == ctx.guild.owner_id or str(ctx.message.author.id) == jdata['owner']:
            chid = self.bot.get_channel(int(id))
            member = ctx.message.guild.get_member(ctx.message.author.id)
            await member.move_to(chid)

    @commands.command()
    async def moveto(self,ctx,uid,cid):
        await ctx.message.delete()
        if ctx.message.author.id == ctx.guild.owner_id or str(ctx.message.author.id) == jdata['owner']:
            chid = self.bot.get_channel(int(cid))
            member = ctx.message.guild.get_member(int(uid))
            print(str(chid)+str(member))
            await member.move_to(chid)
        

def setup(bot):
    bot.add_cog(Main(bot))
    time(int(1))