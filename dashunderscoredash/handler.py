import logging
import time

import discord


class DiscordHandler(logging.Handler):
    """
    Handler for Python's built-in logging module that emits records to a Discord channel
    """

    COLOR_FROM_LEVEL = {
        'DEBUG': discord.Colour.blue(),
        'INFO': discord.Colour.green(),
        'WARNING': discord.Colour.gold(),
        'ERROR': discord.Colour.orange(),
        'CRITICAL': discord.Colour.red(),
    }

    def __init__(self, client: discord.Client, channel: discord.TextChannel):
        logging.Handler.__init__(self)
        self.client = client
        self.channel = channel

    def emit(self, record: logging.LogRecord) -> None:
        try:
            embed = discord.Embed()
            embed.title = record.name
            embed.description = record.getMessage()
            embed.colour = self.COLOR_FROM_LEVEL[record.levelname]
            embed.add_field(name="Level", value=record.levelname)
            embed.add_field(name="Time", value=time.strftime('%x %X', time.gmtime(record.created)))
            embed.add_field(name="Function", value=record.funcName)
            self.client.loop.create_task(self.channel.send(embed=embed))
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
