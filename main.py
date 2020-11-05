import discord
from discord.ext import commands
import json
import random
import os
import keep_alive

os.system("pip install --upgrade discord.py")

intents = discord.Intents.all()

with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

bot = commands.Bot(command_prefix=jdata['command_prefix'],intents=intents)
cmdpy = []
bot.remove_command('help')

@bot.group()
async def help(ctx):
    await ctx.send('```css\n'+str(jdata['command_prefix'])+'ping 顯示機器人延遲\n'
    +str(jdata['command_prefix'])+'ran 骰子遊戲1~10\n'
    +str(jdata['command_prefix'])+'clear [num] 刪除指定數量的聊天內容\n'
    +str(jdata['command_prefix'])+'sayd [msg] 使機器人說話\n'
    +str(jdata['command_prefix'])+'member 顯示伺服器中所有人的狀態\n'
    +str(jdata['command_prefix'])+'offline 顯示離線名單\n'
    +str(jdata['command_prefix'])+'online 顯示上線名單\n'
    +str(jdata['command_prefix'])+'user 顯示個人訊息\n'
    +str(jdata['command_prefix'])+'invite [tag玩家] 邀請他人進入目前語音頻道```')

@bot.event
async def on_ready():
    bot.unload_extension(F'cmds.cmds')
    bot.unload_extension(F'cmds.test')
    print('>>bot is online')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'已加載 {extension}')
    print(F'\n---------------------------------\n已加載 {extension}\n---------------------------------\n')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'已卸載 {extension}')
    print(F'\n---------------------------------\n已卸載 {extension}\n---------------------------------\n')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'已重新加載 {extension}')
    print(F'\n---------------------------------\n已重新加載 {extension}\n---------------------------------\n')

@bot.group()
async def user(ctx):
    arg = ctx.message.channel
    args = str(arg).split(' ')
    CMD = 'Direct Message with'
    CMDs = CMD.split(' ')
    msg = 'Author:'+str(ctx.message.author)+'\nAuthor ID:'+ str(ctx.message.author.id)+'\nChannel:'+str(ctx.message.channel)+'\nChannel ID:'+str(ctx.message.channel.id)
    if CMDs[0] == args[0] and CMDs[1] == args[1] and CMDs[2] == args[2]:
        print('私人訊息')
        await ctx.send(msg)
    else:
        print('群組訊息')
        msg = msg +'\nGuild.owner:'+str(ctx.guild.owner) +'\nGuild.owner_id:' +str(ctx.guild.owner_id)+'\nGuild.name:' +str(ctx.guild.name)
        await ctx.send(msg)

@user.command()
async def showpy(ctx):
    await ctx.channel.purge(limit=2)
    msg = '========MenuList========\n'
    for py in cmdpy:
        print(py)
        msg = str(msg) + str(py) +'\n'
    await ctx.send(msg)


@bot.command()
async def disconnect(ctx):
    await ctx.send('機器人已關閉')
    await bot.close()

@bot.event
async def on_disconnect():
    print('機器人已關閉')


for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        print(Filename)
        cmdpy.append(Filename)
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])