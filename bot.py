#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
import logging

from discord import Embed, Status
from discord.ext import commands
from discord.ext.commands import Cog, Context, CommandError

# get token as environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX') + ' '
DEBUG_CHANNEL_ID = int(os.getenv('DEBUG_CHANNEL_ID'))

logging.basicConfig(level=logging.INFO)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_connect(self):
        logging.info('Connected to Discord.')

    async def on_ready(self):
        logging.info(f'Logged in as {bot.user}.')

    def add_cog(self, cog: Cog) -> None:
        super().add_cog(cog)
        logging.info(f"Added cog: {cog.qualified_name}")

    async def on_command_error(self, ctx: Context, exception: CommandError):
        # send help to the user
        await ctx.send(embed=Embed(
            title=f"A wild `{type(exception).__name__}` appeared! Programmer, I choose you!",
            description=f"You've triggered a(n) `{type(exception).__name__}` error: `{exception}`.\n"
                        f"Please review your command and try again. If you do not know how to use this "
                        f"command, enter `-_- help <command>`, where `<command>` is the command name.\n"
                        f"If you think this is a bug, contact the developers in the bot suggestions "
                        f"channel or file an issue on our GitHub (`-_- source`)."
        ))

        # report the error to the debug channel
        debug_channel = ctx.guild.get_channel(DEBUG_CHANNEL_ID)

        if debug_channel is not None:
            user = ctx.author

            description = f"""Command: `{ctx.message.content}`
                User: {user.name}#{user.discriminator} ({user.display_name})
                Type: `{type(exception).__name__}`
                Exception: `{exception}`
            """

            embed = Embed(
                title=f"Error: `{ctx.message.content}`",
                description=description,
            )

            await debug_channel.send(embed=embed)


bot = Bot(
    PREFIX,
    status=Status.online,
)

if __name__ == '__main__':
    EXTENSIONS = [
        'cogs.admin',
        'cogs.storage',
        'cogs.roulette',
        'cogs.marketing',
    ]

    logging.info(f"Attempting to load {len(EXTENSIONS)} extensions:")
    for extension in EXTENSIONS:
        bot.load_extension(extension)

    bot.run(TOKEN)
