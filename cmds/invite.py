import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

luid = lchid = lstat = lmsgid = lmsg = 0

def new(a,b,c,d,e):
    global luid,lchid,lstat,lmsgid,lmsg
    luid = a
    lchid = b
    lmsgid = c
    lstat = d
    lmsg = e
    return luid,lchid,lstat,lmsgid,lmsg

class invite(Cog_Extension):
    @commands.command()
    async def invite(self,ctx,uuid):
        uid2 = uuid.split('>')
        uid = int((uid2[0])[-18:])
        await ctx.message.delete()
        member = ctx.guild.get_member(ctx.author.id)
        user = self.bot.get_user(int(uid))
        if str(type(member.voice.channel)) == str(discord.channel.VoiceChannel):
            if ctx.author in member.voice.channel.members:
                msg = await ctx.send('<@'+str(user.id) + '>是否願意進入' + str(member.voice.channel.name))
                new(uid, member.voice.channel.id, msg.id, int('1'),msg)
                await msg.add_reaction('✅')
                await msg.add_reaction('❎')
    
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
                        new(0,0,0,0,0)
                        await member.move_to(channel)
                else:
                    await lmsg.delete()
                    new(0,0,0,0,0)

def setup(bot):
    bot.add_cog(invite(bot))