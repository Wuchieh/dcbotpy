import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
import asyncio
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

loglist = []
logindex = 0
for logname in os.listdir('./log'):
    if logname.endswith('.txt'):
        loglist.append(logindex)
        loglist.append(logname)
        logindex += 1
logindex = 0

class logup(Cog_Extension):
    @commands.command()
    async def loglist(self,ctx):
        if str(ctx.author.id) == jdata['owner']:
            msg = ''
            dou = 0
            for i in loglist:
                if dou == 0:
                    msg = msg + str(i)+' , '
                    dou+=1
                else:
                    msg = msg + str(i)[:-4] +'\n'
                    dou = 0
            print(msg)
            await ctx.send(msg)
    
    @commands.command()
    async def reloadlog(self,ctx):
        if str(ctx.author.id) == jdata['owner']:
            global loglist,logindex
            loglist = []
            for logname in os.listdir('./log'):
                if logname.endswith('.txt'):
                    loglist.append(logindex)
                    loglist.append(logname)
                    logindex += 1
            await ctx.send('已重新加載')
            logindex = 0

    @commands.command()
    async def downloadlog(self,ctx,index):
        if str(ctx.author.id) == jdata['owner']:
            a = 0
            for i in loglist:
                if i == int(index):
                    print(loglist[a+1]+'\n')
                    fileurl = 'log/'+loglist[a+1]
                    #fileurl = 'D:\VS code\dcbotpy\log\❦⋟天上✰仙境⋞❦-機器人設定.txt'
                    print(fileurl+'\n')
                    await asyncio. sleep(1)
                    upfile = discord.File(F'{fileurl}')
                    await ctx.send(file = upfile)
                a+=1

def setup(bot):
    bot.add_cog(logup(bot))