import disnake
from disnake.ext import commands
import dotenv
import os
import subprocess
try:
    subprocess.check_call(["pip", "install", "disnake", "dotenv", "requests"])
   
except:
    pass
dotenv.load_dotenv()
bot = commands.Bot()
intents = disnake.Intents.default()
intents.members = True
@bot.event
async def on_ready():
    print(f"{bot.user.name} LOGGED IN")

bot.load_extensions("commands")
bot.run("YOUR TOKEN")

