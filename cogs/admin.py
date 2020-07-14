from discord import Embed, Member, TextChannel
from discord.ext.commands import command, Cog, Bot, Context

import time


class Admin(Cog):
    """Administrative and utility functions."""
    def __init__(self, bot: Bot):
        self.bot = bot
        self.start_time = time.time()

    @command()
    async def stats(self, ctx: Context):
        """Returns some stats about this bot."""
        time_delta = time.time() - self.start_time
        result = Embed(
            title="-_- Bot Stats",
            description=f"Up time: {round(time_delta, 3)} s\n"
                        f"Latency: {round(1000 * self.bot.latency, 3)} ms"
        )
        await ctx.send(embed=result)

    @command(aliases=['server'])
    async def guild(self, ctx: Context):
        guild = ctx.guild
        if guild is None:
            await ctx.send(embed=Embed(
                title="No Guild Found",
                description="Are you sure you're invoking this command in the context of a guild?",
            ))
        else:
            await ctx.send(embed=Embed(
                title=f"Guild: {guild.name}",
                description=f"ID: {guild.id}\n"
                            f"Owner: {guild.owner.name if guild.owner is not None else 'None'}\n"
                            f"Region: {guild.region}\n"
                            f"Channels: {len(guild.channels) - len(guild.categories)}\n"
                            f"Members: {len(guild.members)}\n"
                            f"Roles: {len(guild.roles)}\n"
                            f"Description: {guild.description}\n"
            ))

    @command()
    async def channel(self, ctx: Context, channel: TextChannel = None):
        # TODO: make it work for more than just TextChannel
        if channel is None:
            channel = ctx.channel
        await ctx.send(embed=Embed(
            title=f"Channel: {channel}",
            description=f"Category: {channel.category}\n"
                        f"Created at: {channel.created_at} UTC\n"
                        f"Changed roles: {[role.name for role in channel.changed_roles]}\n"
                        f"Permissions synced: {channel.permissions_synced}\n",
        ))

    @command()
    async def member(self, ctx: Context, member: Member):
        await ctx.send(embed=Embed(
            title=f"Member: {member} ({member.display_name})",
            description=f"ID: {member.id}\n"
                        f"Created at: {member.created_at} UTC\n"
                        f"Joined at: {member.joined_at} UTC\n"
                        f"Bot account: {member.bot}\n"
                        f"System account: {member.system}\n"
        ))


def setup(bot):
    bot.add_cog(Admin(bot))
