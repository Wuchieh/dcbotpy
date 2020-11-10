import discord
from discord.ext import commands
import os
import asyncio
from threading import Thread
from time import sleep
from core.classes import Cog_Extension

time = overtime= luid = lchid = lstat = lmsgid = lmsg = 0

#def time2(inc):
#        t = Timer(inc, printTime, (inc,))
#        t.start()

def file_write(file_input, num_lines):
    print('a')
    sleep(5)
    print('b')
    return 0

async def new(a,b,c,d,e):
    global luid,lchid,lstat,lmsgid,lmsg,time,overtime
    luid = a #使用者ID
    lchid = b #頻道ID
    lmsgid = c #訊息ID
    lstat = d #指令狀態
    lmsg = e #訊息
    if lstat == 1: #判斷狀態和開始計時
        #overtime = time + 3
        curr_thread = Thread(target=file_write, args=("Norah", range(5)))
        curr_thread.daemon = False
        print(curr_thread.start())
        print('123')
    else:
        overtime = 0 #設定結束時間
        pass
    
    return luid,lchid,lstat,lmsgid,lmsg,overtime,time

async def delmsg():
    await lmsg.delete()
    await new(0,0,0,0,0)

#async def timer():
#    print('times up')
#    await delmsg()

class invite(Cog_Extension):
    @commands.command()
    async def invite(self,ctx,uuid):
        await ctx.message.delete()
        if lstat == 0: #判斷是否有人已使用本命令
            uid2 = uuid.split('>')
            uid = int((uid2[0])[-18:])
            member = ctx.guild.get_member(ctx.author.id)
            user = self.bot.get_user(int(uid))
            if str(type(member.voice.channel)) == str(discord.channel.VoiceChannel):
                if ctx.author in member.voice.channel.members:
                    msg = await ctx.send('<@'+str(user.id) + '>是否願意進入' + str(member.voice.channel.name) +'\n請在30秒內按下')
                    await new(uid, member.voice.channel.id, msg.id, int('1'),msg)
                    await msg.add_reaction('✅')
                    await msg.add_reaction('❎')
            else:
                await ctx.send('你並不再本群組的任一語音頻道內！ ')
        else:
            await ctx.send('目前已有人正在使用本指令請稍等')
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,pl):
        if pl.user_id == luid :
            print('userID OK')
            if pl.message_id == lmsgid:
                print('messageID OK')
                if str(pl.emoji) == '✅':
                    print('emoji OK')
                    if lstat == 1:
                        print('stat OK')
                        guild = self.bot.get_guild(pl.guild_id)
                        member = guild.get_member(pl.user_id)
                        channel = self.bot.get_channel(lchid)
                        await lmsg.delete()
                        await new(0,0,0,0,0)
                        await member.move_to(channel)
                else:
                    if str(lstat) == '1':
                        await lmsg.delete()
                    await new(0,0,0,0,0)

def setup(bot):
    bot.add_cog(invite(bot))