"""
Constants loaded from a dotenv file or Heroku config vars
"""

import os
import dotenv

# get token as environment variable
dotenv.load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('COMMAND_PREFIX') + ' '
DEBUG_CHANNEL_ID = int(os.getenv('DEBUG_CHANNEL_ID'))
