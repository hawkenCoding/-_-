# -*- coding: utf-8 -*-

from discord.ext.commands import command, Cog, Context

from bot import Bot


class TEMPLATE(Cog):
    """The description for TEMPLATE goes here."""

    def __init__(self, bot: Bot):
        self.bot = bot

    # @COMMAND()
    # async defND COMMAND(self, ctx: Context):
    #     """The description for COMMAND goes here."""
    #     pass


def setup(bot):
    bot.add_cog(TEMPLATE(bot))
