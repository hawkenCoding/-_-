from typing import Optional

from discord import Embed, Member, TextChannel, Role
from discord.ext.commands import command, Cog, Bot, Context


class Admin(Cog):
    """Administrative and utility functions."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(aliases=['server'])
    async def guild(self, ctx: Context):
        """Information about the current guild (server)."""
        guild = ctx.guild

        embed = Embed()
        if guild is None:
            embed.title = "No Guild Found"
            embed.description = "Are you sure you're invoking this command in a guild (server)?"
        else:
            embed.title = f"Guild: {guild.name}"
            embed.add_field(name="ID", value=guild.id)
            embed.add_field(name="Created", value=guild.created_at.strftime('%x %X') + " UTC")
            embed.add_field(name="Owner", value=(guild.owner.name if guild.owner is not None else "None"))
            embed.add_field(name="Region", value=guild.region)
            embed.add_field(name="# Channels", value=str(len(guild.channels) - len(guild.categories)))
            embed.add_field(name="# Members", value=guild.member_count)
            embed.add_field(name="# Roles", value=str(len(guild.roles)))
            embed.add_field(name="Description", value=guild.description)

        await ctx.send(embed=embed)

    @command()
    async def role(self, ctx: Context, role: Optional[Role] = None):
        """Information about your highest role or any given role."""

        if role is None:
            role = ctx.author.top_role

        embed = Embed()
        embed.title=f"Role: @{role.name}"
        embed.add_field(name='ID', value=role.id)
        embed.add_field(name='Separate', value=("Yes" if role.hoist else "No"))
        embed.add_field(name='Managed', value=("Yes" if role.managed else "No"))
        embed.add_field(name='Mentionable', value=("Yes" if role.mentionable else "No"))
        embed.add_field(name='Created', value=role.created_at.strftime('%x %X') + ' UTC')
        embed.add_field(name='# Members', value=str(len(role.members)))

        await ctx.send(embed=embed)

    @command()
    async def channel(self, ctx: Context, channel: TextChannel = None):
        """Information about this text channel or any other on the server."""
        # TODO: make it work for more than just TextChannel

        if channel is None:
            channel = ctx.channel

        embed = Embed()
        embed.title = f"Channel: #{channel}"
        embed.add_field(name='Category', value=channel.category)
        embed.add_field(name='Created', value=channel.created_at.strftime('%x %X') + ' UTC')
        embed.add_field(name='Changed Roles', value=str(len(channel.changed_roles)))
        embed.add_field(name='Permissions Synced', value=("Yes" if channel.permissions_synced else "No"))

        await ctx.send(embed=embed)

    @command(aliases=['user'])
    async def member(self, ctx: Context, member: Optional[Member] = None):
        """Information about yourself or any other server member."""

        if member is None:
            # default to self
            member = ctx.author

        embed = Embed()
        embed.title = f"{member} (@{member.display_name})"
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='User ID', value=member.id)
        embed.add_field(name='Status', value=member.status)
        embed.add_field(name='Activity', value=member.activity)
        embed.add_field(name='Top Role', value=member.top_role)
        embed.add_field(name='Voice', value=member.voice)
        embed.add_field(name='Created', value=member.created_at.strftime('%x %X') + ' UTC')
        embed.add_field(name='Joined', value=member.joined_at.strftime('%x %X') + ' UTC')
        embed.add_field(name='Bot', value=("Yes" if member.bot else "No"))
        embed.add_field(name='System Account', value=("Yes" if member.system else "No"))

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
