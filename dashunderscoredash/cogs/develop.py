# -*- coding: utf-8 -*-

from discord import Embed, Member
from discord.ext.commands import command, Cog, Context

import time
from dataclasses import dataclass


@dataclass
class Job:
    title: str
    salary: float
    responsibilites: str
    requirements: str


JOBS = [
    Job(
        "Backend Specialist",
        0.0,
        "Design, develop, and maintain a persistent data storage solution for the `-_-` bot. "
        "Also, seek a more reliable hosting platform on which to deploy the bot.",
        "Must have some experience with backend development, whether in a web development "
        "context or otherwise. Must have solid understanding of Python programming and "
        "working understanding of git and GitHub. Experience with discord.py and asynchronous "
        "programming is beneficial but not required; on-the-job training is available.",
    ),
    Job(
        "Discord Bot Developer",
        0.0,
        "Skip the tutorial - work right at the cutting edge! Develop the newest and coolest "
        "features for our very own `-_-` bot. Enjoy both an educational and rewarding work "
        "environment. Aditionally, perform a basic beta testing and quality assurance role. ",
        "Must have proficient level of Python understanding and basic level of git/GitHub "
        "experience. No experience with discord.py necessary. Significant on-the-job training "
        "is available. Specify additional qualifications upon application.",
    ),
    Job(
        "Senior Marketing Manager",
        0.0,
        "Encourage more server members to use the `-_-` bot on a regular basis. Coordinate with "
        "frequent users to gather and prioritize requested features. Recruit more developer to "
        "fill vacancies on the development team. Communicate results directly with the "
        "development team.",
        "Must have excellent communication and teamwork skills. No technical skills required. "
        "An excellent entry-level position for aspiring members.",
    ),
]


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
                        f"Latency: {self.latency} ms\n"
                        f"Guilds: {len(self.bot.guilds)}"
        )
        await ctx.send(embed=result)

    @command()
    async def demoji(self, ctx: Context, emoji: str):
        """Get the Unicode codepoint of an emoji (or any character)."""
        hexpoint = str(hex(ord(emoji)))[2:]
        codepoint = "\\U" + "0" * (8 - len(hexpoint)) + hexpoint
        await ctx.send(f"`{codepoint}`")

    @command()
    async def develop(self, ctx: Context, member: Member = None):
        # default to person who called the command
        if member is None:
            if not isinstance(ctx.author, Member):
                await ctx.send("That's a user but not a member. "
                               "Please try again or report a bug.")
                return
            member = ctx.author
        developer_role = ctx.guild.get_role(731262064391356487)

        # member already has role
        if developer_role in member.roles:
            await ctx.send(f"{member.mention}, you're already a {developer_role.mention}! "
                           f"Congratulations!")
            return

        await member.add_roles(developer_role)
        await ctx.send(f"Congratulations, {member.mention}, you are now an official "
                       f"{developer_role.mention} member! Please see `CONTRIBUTING.md` "
                       f"in `-_- source` to get started. Please also reach out to another "
                       f"developer at your earliest convenience. ")

    @command(aliases=['job'])
    async def jobs(self, ctx: Context):
        if JOBS:
            description = ("Exciting job offers are currently available!\n"
                           "To apply, do `-_- develop`, then contact any developer.\n\n")
            description += "\n\n".join([
                f"**{job.title}**\n"
                f"*Salary*: ${job.salary}/hr\n"
                f"*Responsibilities*: {job.responsibilites}\n"
                f"*Requirements*: {job.requirements}"
                for job in JOBS
            ])
        else:
            description = ("No jobs are available at this time.\n"
                           "Check back later for updates!")
        await ctx.send(embed=Embed(
            title="-_- Job Opportunities",
            description=description,
        ))


def setup(bot):
    bot.add_cog(Develop(bot))
