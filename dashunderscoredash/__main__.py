import logging

from discord import Status

from dashunderscoredash import bot, constants

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

bot = bot.Bot(
    constants.PREFIX,
    status=Status.online,
)

EXTENSIONS = [
    'cogs.admin',
    'cogs.develop',
    'cogs.storage',
    'cogs.marketing',
    'cogs.quote',
    'cogs.roulette',
    'cogs.gabe_why'
]

logger.info(f"Attempting to load {len(EXTENSIONS)} extensions:")
for extension in EXTENSIONS:
    bot.load_extension(extension)

bot.run(constants.TOKEN)
