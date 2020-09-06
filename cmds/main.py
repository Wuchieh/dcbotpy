import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)} 毫秒')

    @commands.command()
    async def ran(self,ctx):
        rannum = random.randint(1,10)
        await ctx.send(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')
        print(str(ctx.message.author)+' 骰出了 '+str(rannum)+'點')

    @commands.command()
    async def move(self,ctx,id):
        await ctx.message.delete()
        chid = self.bot.get_channel(int(id))
        member = ctx.message.guild.get_member(ctx.message.author.id)
        await member.move_to(chid)

    @commands.command()
    async def moveto(self,ctx,uid,cid):
        await ctx.message.delete()
        chid = self.bot.get_channel(int(cid))
        member = ctx.message.guild.get_member(int(uid))
        print(str(chid)+str(member))
        await member.move_to(chid)
        

def setup(bot):
    bot.add_cog(Main(bot))