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
                # TODO: use Guild.member_count instead of len(guild.members)
                            f"Members: {len(guild.members)}\n"
                            f"Roles: {len(guild.roles)}\n"
                            f"Description: {guild.description}\n"
            ))

    @command()
    async def role(self, ctx: Context, role: Role):
        """Information about the given role."""
        await ctx.send(embed=Embed(
            title=f"Role: @{role.name}",
            description=f"ID: {role.id}\n"
                        f"Separate: {role.hoist}\n"
                        f"Managed: {role.managed}\n"
                        f"Mentionable: {role.mentionable}\n"
                        f"Created at: {role.created_at} UTC\n"
                        f"Members: {len(role.members)}\n",
        ))

    @command()
    async def channel(self, ctx: Context, channel: TextChannel = None):
        """Information about this text channel or any other on the server."""
        # TODO: make it work for more than just TextChannel
        if channel is None:
            channel = ctx.channel
        await ctx.send(embed=Embed(
            title=f"Channel: #{channel}",
            description=f"Category: {channel.category}\n"
                        f"Created at: {channel.created_at} UTC\n"
                        f"Changed roles: {[role.name for role in channel.changed_roles]}\n"
                        f"Permissions synced: {channel.permissions_synced}\n",
        ))

    @command()
    async def member(self, ctx: Context, member: Member = None):
        """Information about yourself or any other server member."""
        if member is None:
            member = ctx.author
        await ctx.send(embed=Embed(
            title=f"Member: {member} (@{member.display_name})",
            description=f"ID: {member.id}\n"
                        f"Status: {member.status}\n"
                        f"Activity: {member.activity}\n"
                        f"Top role: {member.top_role}\n"
                        f"Voice state: {member.voice}\n"
                        f"Created at: {member.created_at} UTC\n"
                        f"Joined at: {member.joined_at} UTC\n"
                        f"Bot account: {member.bot}\n"
                        f"System account: {member.system}\n",
        ))


def setup(bot):
    bot.add_cog(Admin(bot))
