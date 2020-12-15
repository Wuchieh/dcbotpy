import discord
from discord.ext import commands
import os
from core.classes import Cog_Extension

testStatus = []

class test(Cog_Extension):
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,pl):
        if pl.message_id == testStatus[1].id:
            if str(pl.emoji) == '👍':
                guild = self.bot.get_guild(pl.guild_id)
                role = guild.get_role(testStatus[0].id)
                await pl.member.remove_roles(role)
    
    @commands.command()
    async def test(self,ctx):
        role = await ctx.guild.create_role(name='test')
        message = await ctx.send('測試用')
        await message.add_reaction('👍')
        members = ctx.channel.members
        for i in members:
            await i.add_roles(role)
        for i in [role,message,members]:
            testStatus.append(i)
    
    @commands.command()
    async def test2(self,ctx):
        print(testStatus)
        print(type(testStatus[0]))

    @commands.command()
    async def test3(self,ctx):
        role = testStatus[0]
        rolec = ctx.guild.get_role(role.id)
        await rolec.delete()
            
def setup(bot):
    bot.add_cog(test(bot))