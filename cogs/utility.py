from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #decorator "Everything contained in the function beneath below~"
    async def on_ready(self):
        print('┌────────────────────────────────────┐')
        print(f'   Logged in as {self.bot.user.name}')
        print(f'    Client ID: {self.bot.user.id}')
        print('└────────────────────────────────────┘')

def setup(bot):
    bot.add_cog(Utility(bot))