import disnake
from disnake.ext import commands
from functions.find_user import *

class FindCommand(commands.Cog):
    

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def find(self, inter: disnake.ApplicationCommandInteraction, id: str):
       
        await inter.response.send_message(find_user(id), ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(FindCommand(bot))