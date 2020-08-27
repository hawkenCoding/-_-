"""
Helper functions for the rest of the bot
"""


def get_id_from_mention(mention_str: str) -> str:
    # chop off <@! from beginning and > from end
    return mention_str[3:-1]
