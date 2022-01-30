import discord
from discord.ext import commands
from music_cog import music_cog

Bot=commands.Bot(command_prefix='/')
Bot.add_cog(music_cog(Bot))

Bot.run('ODk2Mzc1NzQyMDM4OTQxNzQ3.YWGM9g.qE_uknna2low5gjopCkqzjQS2F8')
