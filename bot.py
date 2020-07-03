#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
import logging

import discord
from discord.ext import commands

# get token as environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX') + ' '

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(
    PREFIX,
    status=discord.Status.online,
)


@bot.event
async def on_connect():
    logging.info('Connected to Discord.')


@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user}.')


if __name__ == '__main__':
    # cogs
    cogs = ['cogs.' + file[:-3] for file in list(os.walk('cogs'))[0][2]]
    logging.info(f"Attempting to add {len(cogs)} cogs:")
    for cog in cogs:
        bot.load_extension(cog)
        logging.info(f"Added cog: {cog}")

    # launch bot
    bot.run(TOKEN)
