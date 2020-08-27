#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog, Context, CommandError

from dashunderscoredash import constants

logger = logging.getLogger(__name__)

DEBUG_CHANNEL_ID = 731332649137995847


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_connect(self):
        logger.info('Connected to Discord.')

    async def on_ready(self):
        logger.info(f'Logged in as {self.user}.')

    def add_cog(self, cog: Cog) -> None:
        super().add_cog(cog)
        logger.info(f"Added cog: {cog.qualified_name}")

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
        debug_channel = ctx.guild.get_channel(constants.DEBUG_CHANNEL_ID)

        if debug_channel is not None:
            user = ctx.author
            description = f"""Bot: `{self.user}`
                Command: `{ctx.message.content}`
                User: `{user}` (`{user.display_name}`)
                Type: `{type(exception).__name__}`
                Exception: `{exception}`
            """
            await debug_channel.send(embed=Embed(
                title=f"Error: `{ctx.message.content}`",
                description=description,
            ))
