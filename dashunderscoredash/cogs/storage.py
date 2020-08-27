# -*- coding: utf-8 -*-

import logging

from discord import Embed, Message
from discord.ext.commands import command, Cog, Context

logger = logging.getLogger(__name__)


class Storage(Cog):
    """
    Stores and retrieves an arbitrary string.
    Also stores and retrieves author to prevent abuse.
    """

    def __init__(self, bot):
        self.bot = bot
        self._storage = {}

    @command()
    async def store(self, ctx: Context, *, text):
        """Stores a piece of text and returns a secret key for later access"""
        key = abs(hash(text))
        if key in self._storage:
            # hash collision
            embed = Embed(
                title="Error",
                description="An error occurred. "
                            "Maybe you have already stored this text. "
                            "Please try again. ",
            )
        else:
            self._storage[key] = (ctx.message, text)
            embed = Embed(
                title=key,
                description="Your text has been stored in my memory.\n"
                            "This storage is ephemeral, meaning that "
                            "it will be lost whenever the bot restarts.\n"
                            "Any text you store is potentially visible "
                            "to anyone in the entire server.\n"
                            "Please copy down the secret key shown above. "
                            "You will need it to retrieve your text. ",
            )
        await ctx.send(embed=embed)

    @command()
    async def retrieve(self, ctx, key):
        """Retrieves a stored piece of text given its secret key"""
        key = int(key)
        embed = Embed()
        try:
            message: Message = self._storage[key][0]
            text = self._storage[key][1]

            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.description = text
        except KeyError:
            embed.title = "Error"
            embed.description = "No text with the given secret key was stored. Please try again."
            logger.warn("Request hash not found in storage (may be user error)")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Storage(bot))
