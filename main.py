# https://github.com/UWB-ACM/CSSBot_Py
# ACM Barebones CSSBot_Py

# Original source from
# https://github.com/Chris-Johnston/CSSBot_Py

# using the development version from the rewrite branch
# https://github.com/Rapptz/discord.py/tree/rewrite see the readme file for more information
# python3 -m pip install -r requirements.txt

# docs
# http://discordpy.readthedocs.io/en/rewrite/
# http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html

# if you are on linux;
# may need to install libffi-dev, python-dev/python3.6-dev with apt-get

import discord
from discord.ext import commands
import asyncio
# configuration files
import configparser
import sys, traceback

# load configuration to get around hard coded tokens
config = configparser.ConfigParser()
with open('config.ini') as config_file:
    config.read_file(config_file)

# startup stuff for debugging
print('using discordpy version', discord.__version__)

# the command prefix should be something unique, many bots already use !, ., and / for their prefixes
# you can do any string, 'hey you stupid bot ' would totally work
client = commands.Bot(command_prefix='>>', description='https://github.com/UWB-ACM/CSSBot_Py')

# this is where extensions are added by default
default_extensions = ['cogs.basic']


if __name__ == '__main__':
    for extension in default_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print('Failed to load extension ' + extension, file=sys.stderr)
            traceback.print_exc()


@client.event
async def on_ready():
    # print some stuff when the bot goes online
    print('Logged in ' + str(client.user.name) + ' - ' +
          str(client.user.id) + '\n' + 'Version ' + str(discord.__version__))
    # a good way to let users know how to use the bot is by providing them with a help method
    # only way this can do them any good is by letting them know what the help command is
    await client.change_presence(activity=discord.Game('Try >>help'))

# now actually connect the bot
client.run(config.get(section='Configuration', option='connection_token'),
           bot=True, reconnect=True)
