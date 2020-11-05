import discord
from discord.ext import commands
from core.classes import Cog_Extension

class onoff(Cog_Extension):
    @commands.command()
    async def member(self,ctx):
        memberlist = ctx.guild.members
        onlinelist = []
        onlineidlist = []
        offlineidlist = []
        offlinelist = []
        msg = "========online========\n"
        for i in memberlist:
            if str(i.status) == "online":
                onlineidlist.append(i.id)
                onlinelist.append(i)
            else:
                offlinelist.append(i)
                offlineidlist.append(i.id)
        for onid in onlineidlist:
            msg = msg + '<@' + str(onid) + '>\n'
        msg = msg + '========offline========\n'
        for offid in offlineidlist:
            msg = msg + '<@' + str(offid) + '>\n'

        await ctx.send(msg)
        print('\n========online========\n')
        for i2 in onlinelist:
            print(i2)
        print('\n========offline========\n')
        for i3 in offlinelist:
            print(i3)
    @commands.command()
    async def online(self,ctx):
        memberlist = ctx.guild.members
        onlineidlist = []
        for i in memberlist:
            if str(i.status) == "online":
                onlineidlist.append(i.id)
        msg = '在線名單:\n'
        for i2 in onlineidlist:
            msg = msg + '<@' + str(i2) + '>\n'
        await ctx.send(msg)
    @commands.command()
    async def offline(self,ctx):
        memberlist = ctx.guild.members
        offlineidlist = []
        print(memberlist)
        for i in memberlist:
            if str(i.status) == "offline":
                offlineidlist.append(i.id)
        msg = '離線名單:\n'
        for i2 in offlineidlist:
            msg = msg + '<@' + str(i2) + '>\n'
        await ctx.send(msg)
        

def setup(bot):
    bot.add_cog(onoff(bot))