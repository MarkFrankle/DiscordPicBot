import praw
import discord
from discord.ext import commands
import math
import random

# discord.py calls groups of commands cogs
# cogs can also be handlers for different types of events
# and respond to changes in data as they happen

# setup

usedLinks = []
class BasicCog:
    def __init__(self, bot):
        self.bot = bot

    # Get EyeBleach command
    @commands.command()
    async def eyebleach(self, ctx):
        await ctx.send(getSubmission('eyebleach'))

    # Get EyeBleach command
    @commands.command()
    async def subpic(self, ctx, subreddit):
        await ctx.send(getSubmission(subreddit))
    
    # Get EyeBleach command
    @commands.command()
    async def subrange(self, ctx, subreddit, endIdx):
        for i in range(1, (int)(endIdx) - 1):
            await ctx.send(getSubmissionIndex(subreddit,i))

# add this cog to the bot
def setup(bot):
    bot.add_cog(BasicCog(bot))

def getSubmissionIndex(subreddit, index):
    subreddit = getSubreddit(subreddit)
    hot_sub = subreddit.hot(limit = index)
    i = 0
    for submission in hot_sub:
        if i == index:
            return submission
        i += 1

def getSubmission(subreddit):
        cap = 100
        subreddit = getSubreddit(subreddit)
        hot_sub = subreddit.hot(limit = cap)
        for submission in hot_sub:
            if submission.url not in usedLinks and not submission.stickied and submission.url.endswith('.jpg'):
                usedLinks.append(submission.url)
                return submission.url
        return 'No more pics :('

def getSubreddit(subreddit):
        reddit = praw.Reddit(client_id = '',
                    client_secret = '',
                    username = '',
                    password = '',
                    user_agent = '')
        subreddit = reddit.subreddit(subreddit)
        return subreddit
