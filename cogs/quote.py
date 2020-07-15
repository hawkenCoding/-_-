# -*- coding: utf-8 -*-

from discord import TextChannel, Message, Embed
from discord.ext.commands import command, Cog, Context

from random import choice

from os import getenv
from dotenv import load_dotenv

load_dotenv()
QUOTE_CHANNEL_ID = int(getenv('QUOTE_CHANNEL_ID'))


class Quote(Cog):
    """Processes messages from the #quote-board channel."""

    def __init__(self, bot):
        self.bot = bot

    @command()
    async def quote(self, ctx: Context):
        """Sends one randomly-selected quote from the #quote-board"""
        channel: TextChannel = ctx.guild.get_channel(QUOTE_CHANNEL_ID)
        message: Message = await ctx.send(f"Getting quote from {channel.mention}...")

        # gather all quotes into a list
        quotes = []
        async for quote in channel.history():
            quotes.append(quote)

        # parse the quote
        quote: Message = choice(quotes)
        # this is such a hack
        quote_text, quote_author = quote.content.rsplit(maxsplit=1)

        await message.edit(content=f"\"{quote_text}\"\n"
                                   f"-{quote_author}, {quote.created_at} UTC")


def setup(bot):
    bot.add_cog(Quote(bot))
