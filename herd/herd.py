from redbot.core import commands


class Herd(commands.Cog):
    """Move people to a different channel."""

    @commands.command()
    async def herd(self, ctx):
        await ctx.send("Hello world.")
