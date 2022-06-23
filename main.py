#Bot for Discord

import random
from discord.ext import commands
import requests
import html2text
import re

#Symbol for start command
bot = commands.Bot(command_prefix='!')
range_add = 4
@bot.command()
async def coub(ctx):
    global range_add
    merker = 1
    while merker:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        figures = '1234567890'
        result_end = ''
        list = []
        for i in range(range_add):
            random_figur = random.randint(1, 2)
            if random_figur == 1:
                end = random.choice(letters)
                result_end += end
            else:
                end = random.choice(figures)
                result_end += end
        message = 'https://coub.com/view/' + result_end

        #Checking the video page
        x = requests.get(message)
        d = html2text.HTML2Text()
        d.ignore_links = True

        # Text without HTML-tags
        c = d.handle(x.text)
        pattern = r"Sorry, that page doesn't exist."
        string = c
        result = re.search(pattern, string)
        itog = result != None
        merker = 0

        if itog == True:
            merker = 1
        else:
            await ctx.send(message)
            range_add += 1
            if range_add == 7:
                range_add = 4

#Checking bot connection
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#Running
bot.run('Your token') #Команда для работы бота (токен)