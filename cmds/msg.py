import discord
from discord.ext import commands
from core.classes import Cog_Extension
channelid ='695926882792767539'

class Msg(Cog_Extension):

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def setchannelid(self,ctx,msg):
        if str.isdigit(msg) and len(msg) == 18:
            channelid = commands.get_channel(msg)
            await ctx.send('頻道ID以修改為：' + str(channelid) + '\n'+ str(ctx.message.channel))
            print('ok')
        else:
            print('no')
        #ctx.message.channel.id = channelid
        #await ctx.send('ChannelID已設為 : ' + msg)
    
    @commands.command()
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        print(str(ctx.message.author)+' ---ID '+str(ctx.message.author.id)+
        '在 << '+str(ctx.channel.name)+' >> 頻道使用了clear指令刪除了'+str(int(num))+'個對話')

def setup(bot):
    bot.add_cog(Msg(bot))