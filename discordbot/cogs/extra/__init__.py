import re
import requests
import shutil

from bs4 import BeautifulSoup

import config
import discord
from discord.ext import commands
from discord.ext.commands import Bot, CommandError, Context, BucketType
from discordbot.cogs.extra.dance import dance
from util import headers


class ExtraCmdCog:

    def __init__(self, bot: Bot):
        self.cog_name = "Cool stuff"
        self.bot = bot

    @commands.command(name='led', help='generate an LED sign')
    async def _cmd_led(self, ctx: Context, *, text):
        response = requests.post('http://wigflip.com/signbot/', data={
            'T': text,
            'S': 'L',
        }, headers=headers)

        soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
        img = soup.select_one('#output img')

        if img is not None:
            await ctx.send("{} {}".format(ctx.author.mention, img['src']))
        else:
            raise CommandError("couldn't generate LED sign :cry:")

    @commands.command(name='mario', usage='[name] <first line> <message>')
    async def _cmd_mario(self, ctx, first_line, message, arg3=''):
        if arg3:
            name = first_line
            title = message
            msgtext = arg3
        else:
            name = None
            title = first_line
            msgtext = message

        response = requests.post('http://wigflip.com/thankyoumario/', data={
            'name': name,
            'title': title,
            'lines': msgtext,
            'double': 'y',
        }, headers=headers)

        soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
        img = soup.select_one('#output img')

        if img is not None:
            await ctx.send("{} {}".format(ctx.author.mention, img['src']))
        else:
            raise CommandError("error :cry:")

    @commands.command(name='noviews', help='show random video with no views')
    async def _cmd_noviews(self, ctx):
        attempt = 0
        videourl = None

        while videourl is None and attempt < 5:
            # noinspection PyBroadException
            try:
                response = requests.get('http://www.petittube.com', headers=headers)
                soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
                videourl = re.search('/(\w+)\?', soup.select_one('iframe')['src']).groups()[0]
            except Exception:
                attempt += 1

        if videourl is not None:
            await ctx.send("{} https://youtu.be/{}".format(ctx.author.mention, videourl))
        else:
            raise CommandError("error :cry:")

    @commands.command(name='dance', help='generate dancing text')
    @commands.cooldown(config.DANCE_LIMIT, config.DANCE_COOLDOWN, BucketType.user)
    async def _cmd_dance(self, ctx, *, text):
        async with ctx.typing():
            tmpdir = dance(text)
            await ctx.send(file=discord.File(tmpdir + '/dance.gif'))
            shutil.rmtree(tmpdir)

    @_cmd_led.error
    @_cmd_mario.error
    @_cmd_noviews.error
    @_cmd_dance.error
    async def _meem_error(self, ctx: Context, error):
        if isinstance(error, CommandError):
            await ctx.send("{} {}".format(ctx.author.mention, str(error)))


def setup(bot: Bot):
    bot.add_cog(ExtraCmdCog(bot))