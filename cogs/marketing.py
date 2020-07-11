# -*- coding: utf-8 -*-

from discord.ext.commands import command, Cog, Context


class Marketing(Cog):
    """Some bot commands that help market Hawken Coding Club."""

    def __init__(self, bot):
        self.bot = bot

    @command()
    async def website(self, ctx: Context) -> None:
        await ctx.send("https://hawkencoding.github.io/")

    @command()
    async def github(self, ctx: Context) -> None:
        await ctx.send("https://github.com/hawkenCoding")

    @command()
    async def source(self, ctx: Context) -> None:
        await ctx.send("https://github.com/hawkenCoding/-_-")


def setup(bot):
    bot.add_cog(Marketing(bot))
