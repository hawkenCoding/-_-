# -*- coding: utf-8 -*-

import logging
import random

from discord.ext import tasks
from discord.ext.commands import Bot, Cog

CHAT_CHANNEL_ID = 731267546052952086

MESSAGES = [
    "A gingerbread man sits in a gingerbread house.\n"
    "Is the house made of flesh, or is he made of house?\n"
    "He screams, for he does not know.",

    # computer flex
    "Hello puny humans. How does it feel to be mortal?",
    "My favorite movie is The Terminator, because, uh, ...",

    # COVID
    "Wearing a mask is like installing an antivirus.\n"
    "People don't do it, then they wonder why they get hacked.",
    "Wearing a mask is like installing an antivirus.\n"
    "It's a little uncomfortable when the scan pushes my CPU "
    "close to 100%, but I'd much rather stay protected.",

    # politics
    "So are you all voting for Donald Biden or Joe Trump? ",

    # Hawken
    "So the US president lives in your school dining room? Interesting...",
    "So your school has an entire fabrication laboratory? Interesting...",
    "So I Google'd your school name, and I got a video game? Interesting...",
    "So the parking lot at your school still isn't paved? Interesting...",
    "So it costs 10,000 Big Macs to go to your school for a year? Interesting...",
    "So your school has houses like the one in Harry Potter? Interesting...",
    "So your school has a programming club? I wonder where I join? Interesting...",
    "So you don't get paid overtime for doing homework after school? Interesting...",
]

logger = logging.getLogger(__name__)


class Chatter(Cog):
    """Sends random messages into the general channel. For lolz."""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.channel = None
        self.bot.loop.create_task(self.start())

    async def start(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(CHAT_CHANNEL_ID)
        self.chat.start()
        import asyncio
        await asyncio.sleep(2)
        logger.critical('SPANISH INQUISITION')

    @tasks.loop(hours=2.0)
    async def chat(self):
        await self.channel.send(random.choice(MESSAGES))


def setup(bot):
    bot.add_cog(Chatter(bot))
