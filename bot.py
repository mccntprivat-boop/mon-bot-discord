import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")

@bot.command()
async def bonjour(ctx):
    await ctx.send("👋 Bonjour ! Je suis prêt à modérer le serveur.")

bot.run(os.environ["DISCORD_TOKEN"])
