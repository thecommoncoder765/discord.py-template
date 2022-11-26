import disnake
from disnake.ext import commands
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward
import config
import configlvl

class level(commands.Cog):
    def __init__(self, bot):
    	self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Loaded Cog Levels')

    @commands.slash_command()
    async def rank(inter):
        data = await configlvl.lvl.get_data_for(inter.author)
        await inter.send(f"You are level {data.level} and your rank is {data.rank}")

def setup(bot):
    bot.add_cog(level(bot))