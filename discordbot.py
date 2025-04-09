import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)
intents.voice_states = True
intents.messages = True
queue = {}



@bot.command()
async def ping(ctx):
    await ctx.reply('pong')

@bot.command()
async def hug(ctx, member: discord.Member = None):
    if member == None:
        await ctx.send(f'{ctx.author.mention} *hugs me*')
    await ctx.channel.send(f"{ctx.author.mention} *hugs* {member.mention}")


@bot.command()
async def uwu(ctx):
    await ctx.send('***UwU***')


@bot.command()
async def hello(ctx):
    await ctx.reply('hey there')


@bot.command()
async def r(ctx):
    await ctx.reply(random.randint(0, 100))


bot.run('')
