import discord
from discord.ext import commands
from core.classes import Cog_Extension
from random import randint
import os
import json
with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)
    
class minesweeper(Cog_Extension):
    @commands.command(aliases=["ms"])
    async def minesweeper(self, ctx, width: int = 10, height: int = 10, difficulty: int = 30):
      guild = self.bot.get_guild(706889259692589077)
      role = guild.get_role(int(707436956740485121))
      member = guild.get_member(ctx.author.id)
      if role in member.roles or str(ctx.message.author.id) == jdata['owner'] or ctx.message.author.id == ctx.guild.owner_id:
        grid = tuple([['' for i in range(width)] for j in range(height)])
        num = ('0⃣','1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣')
        msg = ''

        if not (1 <= difficulty <= 100):
          await ctx.send("Please enter difficulty in terms of percentage (1-100).")
          return
        if width <= 0 or height <= 0:
          await ctx.send("Invalid width or height value.")
          return
        if width * height > 198:
          return await ctx.channel.send("Your grid size is too big.")
          return
        if width * height <= 4:
          await ctx.send("Your grid size is too small.")
          return
        
        # set bombs in random location
        for y in range(0, height):
          for x in range(0, width):
            if randint(0, 100) <= difficulty:
              grid[y][x] = '💣'

        # now set the number emojis
        for y in range(0, height):
          for x in range(0, width):
            if grid[y][x] != '💣':
              grid[y][x] = num[sum((
                grid[y-1][x-1]=='💣' if y-1>=0 and x-1>=0 else False,
                grid[y-1][x]=='💣' if y-1>=0 else False,
                grid[y-1][x+1]=='💣' if y-1>=0 and x+1<width else False,
                grid[y][x-1]=='💣' if x-1>=0 else False,
                grid[y][x+1]=='💣' if x+1<width else False,
                grid[y+1][x-1]=='💣' if y+1<height and x-1>=0 else False,
                grid[y+1][x]=='💣' if y+1<height else False,
                grid[y+1][x+1]=='💣' if y+1<height and x+1<width else False
              ))]
        await ctx.send(grid[y][x])

        # generate message
        for i in grid:
          for tile in i:
            msg += '||' + tile + '|| '
          msg += '\n'
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(minesweeper(bot))