from os import closerange
import discord
from discord.ext import commands

from image_cog import image_cog

Bot = commands.Bot(command_prefix='f!')

Bot.add_cog(image_cog(Bot))

@Bot.command()
async def echo(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)
token = ""
with open("token.txt") as file:
    token = file.read()
Bot.run(token)
