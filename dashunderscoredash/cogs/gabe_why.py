# -*- coding: utf-8 -*-

from discord import Message
from discord.ext.commands import Cog, Bot

import random

TARGET_USER_IDS = [
    432180657796546590,  # Gabe
    761034498686713936, # Divij S
]

WHY_EMOJIS = [
    '\U0001F62C',   # :grimacing:
    '\U0001F644',   # :rolling_eyes:
]


class Gabe_Why(Cog):
    """Replies 'why' to images Gabe sends (and maybe others)."""

    def __init__(self, bot):
        self.bot: Bot = bot

    @staticmethod
    def get_why(min_ys=1, max_ys=6):
        why = "wh" + "y" * random.randint(min_ys, max_ys)
        if random.random() > 0.75:
            why = why.upper()
        return why

    @Cog.listener()
    async def on_message(self, message: Message):
        # ignore all messages from bot to avoid recursion
        if message.author == self.bot.user:
            return
        # send a funny message to the image sender lolz
        # TODO: only react to images, not any attachment
        if message.author.id in TARGET_USER_IDS and message.attachments:
            await message.add_reaction(random.choice(WHY_EMOJIS))
            ctx = await self.bot.get_context(message)
            await ctx.send(f"{message.author.mention} {self.get_why()}")


def setup(bot):
    bot.add_cog(Gabe_Why(bot))
