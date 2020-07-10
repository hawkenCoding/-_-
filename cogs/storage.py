# -*- coding: utf-8 -*-

from discord.ext import commands

_text = ''
_author = ''


class Storage(commands.Cog):
    """
    Stores and retrieves an arbitrary string.
    Also stores and retrieves author to prevent abuse.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def store(self, ctx, *, text):
        global _text, _author
        _text = text
        _author = ctx.author.name
        await ctx.send("Got it.")

    @commands.command()
    async def retrieve(self, ctx):
        await ctx.send(_author + ":")
        await ctx.send(_text)


def setup(bot):
    bot.add_cog(Storage(bot))
