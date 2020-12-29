import discord
from discord.ext import commands
import json
import requests
import asyncio
import random
import os
import keep_alive

keeptime = 10
keepstatus = 1

os.system("pip install --upgrade discord.py")

intents = discord.Intents.all()

with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

bot = commands.Bot(command_prefix=jdata['command_prefix'],intents=intents)
cmdpy = []
bot.remove_command('help')


@bot.event
async def on_ready():
    bot.unload_extension(F'cmds.cmds')
    bot.unload_extension(F'cmds.test')
    print('>>bot is online')
    while(1):
        await asyncio.sleep(keeptime)
        if keepstatus == 1:
            requests.get("https://invite.q20001116.repl.co")
        

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == int(jdata['owner']):
        bot.load_extension(F'cmds.{extension}')
        await ctx.send(F'已加載 {extension}')
        print(F'\n---------------------------------\n已加載 {extension}\n---------------------------------\n')

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == int(jdata['owner']):
        bot.unload_extension(F'cmds.{extension}')
        await ctx.send(F'已卸載 {extension}')
        print(F'\n---------------------------------\n已卸載 {extension}\n---------------------------------\n')

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == int(jdata['owner']):
        bot.reload_extension(F'cmds.{extension}')
        await ctx.send(F'已重新加載 {extension}')
        print(F'\n---------------------------------\n已重新加載 {extension}\n---------------------------------\n')

@bot.command()
async def keep(ctx,type,index):
    global keepstatus,keeptime
    if type == 'status':
        if index == '1':
            print('已啟用保持連線')
        elif index == '0':
            print('已關閉保持連線')
        else:
            print('請輸入1或0')
            return
        keepstatus = int(index)
    if type == 'time':
        if index.isdigit():
            keeptime = int(index)
        else:
            print('請輸入數字')

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
    if ctx.author.id == int(jdata['owner']):
        await ctx.send('機器人已關閉')
        await bot.close()

@bot.event
async def on_disconnect():
    requests.get("http://127.0.0.1:8080/")
    print('機器人已關閉')


for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        print(Filename)
        cmdpy.append(Filename)
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])