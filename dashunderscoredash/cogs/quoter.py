# -*- coding: utf-8 -*-

from dataclasses import dataclass
import logging
import random
from typing import Optional

from discord import Embed, Member, Message
from discord.ext.commands import command, Bot, Cog, Context

from dashunderscoredash.helpers import get_id_from_mention

QUOTE_CHANNEL_ID = 732792588507152395

logger = logging.getLogger(__name__)

@dataclass
class Quote:
    text: str
    author: Member


class Quoter(Cog):
    """Processes messages from the #quote-board channel."""

    def __init__(self, bot: Bot):
        self.bot = bot

    def process_quote(self, message: Message) -> Quote:
        """
        Processes a raw Discord message into a quote, if the author mention is at the end
        """
        text, author_mention = message.content.rsplit(maxsplit=1)

        # TODO: except ValueError:

        author = self.bot.get_user(get_id_from_mention(author_mention))
        return Quote(text, author)

    async def get_quote(self, member: Optional[Member] = None) -> Quote:
        """Retrieves one randomly-selected quote from the #quote-board"""
        channel = self.bot.get_channel(QUOTE_CHANNEL_ID)

        # gather all matching quotes
        quotes = []
        if member is None:
            # get quotes from all members
            async for message in channel.history():
                quotes.append(self.process_quote(message))
        else:
            # get quotes that match member parameter
            async for message in channel.history():
                quote = self.process_quote(message)
                if quote.author == member:
                    quotes.append(quotes)

        if len(quotes) == 0:
            return None
        return random.choice(quotes)

    @command()
    async def quote(self, ctx: Context, member: Optional[Member] = None):
        """Sends one randomly-selected quote from the #quote-board"""
        channel = ctx.guild.get_channel(QUOTE_CHANNEL_ID)
        message = await ctx.send(f"Getting quote from {channel.mention}...")
        quote: Quote = await self.get_quote(member)

        if quote is None:
            if member is None:
                await message.edit(content=f"No quotes found. This is probably a bug. "
                                           f"Please report it - thanks! ")
                logger.warn("Bot didn't find any quotes at all, no user specified.")
            else:
                await message.edit(content=f"No quotes found by that person. "
                                           f"Please try again with a different person.\n"
                                           f"If you think this is a bug, please report it. ")
        else:
            embed = Embed()
            embed.title = quote.text
            embed.set_author(name=quote.author.nick, icon_url=quote.author.avatar_url)
            await message.edit(embed=embed)


def setup(bot):
    bot.add_cog(Quoter(bot))
