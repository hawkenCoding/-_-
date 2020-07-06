# -*- coding: utf-8 -*-

from discord.ext.commands import Cog, Context, command
from discord import Forbidden
from random import randint
from asyncio import sleep


class Roulette(Cog):
    """A fun game for the amusement of everyone on the server."""

    def __init__(self, bot):
        self.bot = bot

    @command()
    async def fire(self, ctx: Context) -> None:
        """Try your luck! 1/6 chance of being kicked from the server"""
        if randint(1, 6) == 6:
            # kick
            await ctx.send("You spin the chamber and pull the trigger. " 
            "BANG! Everything fades to nothingness.")
            await sleep(2)
            try: 
                await ctx.author.kick()
            except Forbidden:
                await ctx.send("Luckily, the weapon is faulty. (Missing permissions.)")
            await ctx.send("The chamber is reloaded...")
        else:
            # no kick
            await ctx.send("You spin the chamber and pull the trigger. "
            "Click! Nothing happens.")



def setup(bot):
    bot.add_cog(Roulette(bot))
