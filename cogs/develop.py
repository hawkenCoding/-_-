# -*- coding: utf-8 -*-

from discord import Embed
from discord.ext.commands import command, Cog, Context

import time


class Develop(Cog):
    """Tools and utilites for bot developers."""

    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @property
    def latency(self):
        """Returns the latency in milliseconds"""
        return round(1000 * self.bot.latency, 3)

    @command()
    async def ping(self, ctx: Context):
        """Ping the bot for a response and latency."""
        await ctx.send(embed=Embed(
            title="Pong!",
            description=f"Latency: {self.latency} ms",
        ))

    @command()
    async def stats(self, ctx: Context):
        """Returns some stats about this bot."""
        time_delta = time.time() - self.start_time
        result = Embed(
            title="-_- Bot Stats",
            description=f"Up time: {round(time_delta, 3)} s\n"
                        f"Latency: {self.latency} ms"
        )
        await ctx.send(embed=result)


def setup(bot):
    bot.add_cog(Develop(bot))
