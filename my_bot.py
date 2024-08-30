import os
import discord
import numpy as np
from discord.ext import commands

file_path = os.path.join("D:\\GitHub_etc\\dc機器人token\\", "周防有C.txt")
buffer = []
with open(file_path, 'r', encoding = 'utf-8') as f:
    for line in f:
        buffer.append(line.strip())

token = buffer[1] 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents = intents)


'''使用slash命令再使用'''
# @bot.command()
# @commands.has_permissions(administrator = True)
# async def synccommands(context):
#     await bot.tree.sync()
#     await context.send("sync ready")


@bot.command()
async def ping(context):
    await context.send("pong")

@bot.command()
async def add(context, a: int, b: int):
    gif_0 = "https://tenor.com/gU5yYvLy0s9.gif"
    gif_00 = "https://tenor.com/h7LgLc7VClK.gif"
    await context.send(f'我猜{a+b+1}')
    await context.send(gif_0)
    await context.send(f'艾莉:你哥怎麼教的?')
    await context.send(gif_00)

@bot.command()
async def 有希(context):
    gif_1 = "https://tenor.com/ch2CPP6Pp9o.gif"
    gif_11 = "https://tenor.com/n4fBjcNkMY0.gif"
    await context.send(gif_1)
    await context.send(gif_11)

@bot.command()
async def 艾莉(context):
    gifs = ["https://tenor.com/eAdzN5R2QLs.gif", "https://tenor.com/txtutN3UZKC.gif", "https://tenor.com/duIgjeZ29Ca.gif"]
    for gif in gifs:
        await context.send(gif)

@bot.command()
async def 起床(context):
    gif_3 = "https://tenor.com/pAVlohjBrsi.gif"
    await context.send(gif_3)

@bot.command()
async def baka(context):
    gif_4 = "https://tenor.com/n5ysUignIeV.gif"
    await context.send(gif_4)

bot.run(token)


