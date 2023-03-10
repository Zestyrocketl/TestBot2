import discord
from discord.ext import commands


class UserInfoCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='userinfo', description='Get info about a user')
    async def userinfo_command(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        embed = discord.Embed(title=f'User Info - {user}', color=user.top_role.color)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name='ID', value=user.id)
        embed.add_field(name='Nickname', value=user.display_name)
        embed.add_field(name='Account Created', value=discord.utils.styled_timestamp(user.created_at,
                                                                                     style=discord.TimestampStyle.relative))
        embed.add_field(name='Joined Server', value=discord.utils.styled_timestamp(user.created_at,
                                                                                   style=discord.TimestampStyle.relative))
        roles = [role.mention for role in user.roles if role != user.guild.default_role]
        roles_string = ', '.join(roles) if roles else 'None'
        embed.add_field(name='Roles', value=roles_string)
        embed.add_field(name='Top Role', value=user.top_role.mention)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.respond(embed=embed, hidden=True)


def setup(bot):
    bot.add_cog(UserInfoCommand(bot))
