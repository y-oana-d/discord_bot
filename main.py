from discord.ext import commands

#Sets the prefix for the bot commands
client = commands.Bot(command_prefix="!")

TOKEN = 'NzczNjA0MzcyOTg1ODA2ODc5.X6LpNw.HJcbwwbhDePD7QVsBYnqsGp43b0'


@client.event
async def on_ready():
    print('Bot online')

@client.command()
async def hello(context):
    print(context.channel)
    if str(context.channel) == 'reception':
        await context.send(f'hello {context.author.mention}, welcome to our hotel')
    else:
        await context.send(f'hello {context.author.mention}')




#This is the last line in the bot, it stats the bot
client.run(TOKEN)