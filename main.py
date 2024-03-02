import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user}: Eu estou online!")

@bot.slash_command(name = "ola", description = "Imprima uma mensagem do bot")
async def ola(ctx):
    await ctx.respond(f"Olá {ctx.author.mention}!")

bot.run(os.getenv('TOKEN'))
