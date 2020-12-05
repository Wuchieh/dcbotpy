import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import os
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)
messageId = int()
message = discord.message.Message
bingoStatus = 0
gameIng = []
bingoPan = [*range(1,26)]
class bingo(Cog_Extension):
    @commands.command(aliases=['b'])
    async def bingogamestart(self,ctx):
        #print(bingoPan)
        global bingoStatus,message,messageId
        if bingoStatus == 0:
            global messageId
            msg = await ctx.send('Bingo遊戲準備開始 按下🖐️參與')
            await msg.add_reaction('🖐️')
            await msg.add_reaction('✅')
            message = msg
            messageId = msg.id
            bingoStatus = 1
        else:
            await ctx.send('遊戲已開始')
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,pl):
        if pl.message_id == messageId and str(pl.emoji) ==  '✅' and pl.member.bot == False:
            global gameIng
            print('success')
            members= []
            channel = self.bot.get_channel(pl.channel_id)
            msg = await channel.fetch_message(messageId)
            for i in msg.reactions:
                if i.emoji == '🖐️':
                    async for user in i.users():
                        members.append(user.id)
            members.remove(self.bot.user.id)
            print(members)
            for i in members:
                game = []
                game.append(i)
                random.shuffle(bingoPan)
                for i in bingoPan:
                    game.append(i)
                gameIng.append(game)
            print(gameIng)
            for i in gameIng:
                runTime = 0
                msg = ''
                user = self.bot.get_user(i[0])
                for i2 in range(1,26):
                    if runTime == 0 :
                        msg = msg + str(i[i2])+' ,'
                        runTime += 1
                    elif runTime == 4:
                        msg = msg + str(i[i2])+'\n'
                        runTime =  0
                    else :#runTime > 0 or runTime<4
                        msg = msg  + str(i[i2])+' ,'
                        runTime += 1
                    print(str(msg))
                await user.send(str(msg))
            await message.delete()
            await message.channel.send('遊戲開始 請輸入'+jdata['command_prefix']+'bingo [數字]進行遊戲')

def setup(bot):
    bot.add_cog(bingo(bot))