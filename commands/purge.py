import disnake
from disnake.ext import commands
import dotenv
import os
dotenv.load_dotenv()
class PurgeCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def purge(self, inter: disnake.ApplicationCommandInteraction):
        channel = inter.channel
        # Skriv in vilken roll som ska ha perms
        role_id = 2232323
        
        required_role = disnake.utils.get(inter.guild.roles, id=int(role_id))
        if required_role not in inter.author.roles:
            await inter.response.send_message("Insufficient permissions to run this command.", ephemeral=True)
        else:

            await channel.clone(name=f"{channel.name}")
            await channel.delete()
def setup(bot: commands.Bot):
    bot.add_cog(PurgeCommand(bot))
    
    