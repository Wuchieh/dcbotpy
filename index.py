import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

bot = commands.Bot(command_prefix=jdata['command_prefix'])

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

@bot.command()
async def user(ctx):
    await ctx.send('Author:'+str(ctx.message.author)+'\nAuthor ID:'+ str(ctx.message.author.id)+
    '\nChannel:'+str(ctx.message.channel)+'\nChannel ID:'+str(ctx.message.channel.id))

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])