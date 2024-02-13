from functions.cfx_finder import cfx_find
import disnake
from disnake.ext import commands

class Cfx_findCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def cfxfind(inter: disnake.ApplicationCommandInteraction, cfxkod: str):
        await inter.response.send_message(cfx_find(cfxkod), ephemeral=True)
def setup(bot: commands.Bot):
    bot.add_cog(Cfx_findCommand(bot))