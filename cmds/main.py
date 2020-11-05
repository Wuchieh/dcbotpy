import discord
import os
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)} 毫秒')
        #os.popen("ping -c 1 google.com")
        #d = os.popen("ping google.com")
        #d2 = str(d.read()).split('時間=')
        #sec = 0
        #for i in range(1, 5):
        #    d3 = d2[i].split('ms TTL')
        #    sec += int(d3[0])
        #await ctx.send('網路延遲：'+ str(sec / 4) + '毫秒')

    @commands.command()
    async def ran(self,ctx):
        await ctx.message.delete()
        rannum = random.randint(1,10)
        await ctx.send(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
        print(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
      
    @commands.command()
    async def rans(self,ctx,min,max):
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