import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('>>bot is online')
@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} 毫秒')

bot.run(jdata['TOKEN'])