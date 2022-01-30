import discord
from discord.ext import commands
from music_cog import music_cog

Bot=commands.Bot(command_prefix='/')
Bot.add_cog(music_cog(Bot))

Bot.run('')
