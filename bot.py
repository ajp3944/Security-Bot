import hikari
import lightbulb
import ip_info

bot = lightbulb.BotApp(
    token='', default_enabled_guilds=(1017526173061881946))

#.\env\Scripts\activate
#python bot.py

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.author.username + " " + event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

@bot.command
@lightbulb.command('ping', 'Say pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.option('num1', 'The first number', type = int)
@lightbulb.option('num2', 'The second number', type = int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

@bot.command
@lightbulb.option('ip', 'Enter the IP address', type = str)
@lightbulb.command('iptoloc', 'Gives locations based on an IP address', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def iptoloc(ctx):
    await ctx.respond(ip_info.get_location(ctx.options.ip))

bot.run()