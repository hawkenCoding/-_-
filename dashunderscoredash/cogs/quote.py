# -*- coding: utf-8 -*-

from discord import TextChannel, Message, Member
from discord.ext.commands import command, Cog, Context, CommandError

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
    async def quote(self, ctx: Context, member: Member = None):
        """Sends one randomly-selected quote from the #quote-board"""
        channel: TextChannel = ctx.guild.get_channel(QUOTE_CHANNEL_ID)
        message: Message = await ctx.send(f"Getting quote from {channel.mention}...")

        # gather all matching quotes
        quotes = []
        if member is None:
            async for quote in channel.history():
                quotes.append(quote)
        else:
            async for quote in channel.history():
                quote_author = quote.content.rsplit(maxsplit=1)[-1]
                if str(member.id) in quote_author:
                    quotes.append(quote)

        if len(quotes) == 0:
            if member is None:
                await message.edit(content=f"No quotes found. This is probably a bug. "
                                           f"Please report it - thanks! ")
                raise CommandError("Bot didn't find any quotes at all, no user specified.")
            else:
                await message.edit(content=f"No quotes found by that person. "
                                           f"Please try again with a different person.\n"
                                           f"If you think this is a bug, please report it. ")
        else:
            # parse the quote
            quote: Message = choice(quotes)
            # this is such a hack
            quote_text, quote_author = quote.content.rsplit(maxsplit=1)

            await message.edit(content=f"\"{quote_text}\"\n"
                                       f"-{quote_author}, {quote.created_at} UTC")


def setup(bot):
    bot.add_cog(Quote(bot))
