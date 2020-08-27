import logging

from discord import Status

from dashunderscoredash import constants
from dashunderscoredash.bot import Bot

logging.basicConfig(level=logging.INFO)

bot = Bot(constants.PREFIX, status=Status.online,)

bot.load_extension('dashunderscoredash.cogs.admin')
bot.load_extension('dashunderscoredash.cogs.chatter')
bot.load_extension('dashunderscoredash.cogs.develop')
bot.load_extension('dashunderscoredash.cogs.gabe_why')
bot.load_extension('dashunderscoredash.cogs.marketing')
bot.load_extension('dashunderscoredash.cogs.quoter')
bot.load_extension('dashunderscoredash.cogs.roulette')
bot.load_extension('dashunderscoredash.cogs.storage')

bot.run(constants.TOKEN)
