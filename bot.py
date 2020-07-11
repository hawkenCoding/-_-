#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
import logging

import discord
from discord.ext import commands

from types import ModuleType

# get token as environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX') + ' '

logging.basicConfig(level=logging.INFO)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_cog(self, cog: commands.Cog) -> None:
        super().add_cog(cog)
        logging.info(f"Added cog: {cog.qualified_name}")


bot = Bot(
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
    EXTENSIONS = [
        'cogs.admin',
        'cogs.roulette',
        'cogs.storage',
    ]
    logging.info(f"Attempting to load {len(EXTENSIONS)} extensions:")
    for extension in EXTENSIONS:
        bot.load_extension(extension)

    bot.run(TOKEN)
