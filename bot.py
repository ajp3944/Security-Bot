import hikari
import lightbulb
import requests
import ip_info
import link_malware_checker
import pass_generator
import phone_number_validator
import get_hash

bot = lightbulb.BotApp(
    token='', default_enabled_guilds=(1017526173061881946))

#.\env\Scripts\activate
#python bot.py

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.message.attachments[0].url)
    #print(event.author.username + " " + event.content)

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
@lightbulb.option('ip', 'Enter the IP address.', type = str)
@lightbulb.command('iptoloc', 'Gives locations based on an IP address.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def iptoloc(ctx):
    await ctx.respond(ip_info.get_location(ctx.options.ip))

@bot.command
@lightbulb.option('url', 'Enter the url of a website you want to check.', type = str)
@lightbulb.command('linkchecker', 'Checks if a link is safe to use. Risk Score: 0 = No Risk, 100 = High Risk.')
@lightbulb.implements(lightbulb.SlashCommand)
async def linkchecker(ctx):
    await ctx.respond(link_malware_checker.determine_malicious_link(ctx.options.url))

@bot.command
@lightbulb.option('length', 'Enter the length password.', type = int)
@lightbulb.command('passwordgen', 'Generates a password you can use from scratch.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def passwordgen(ctx):
    await ctx.respond(pass_generator.generate_random_password(ctx.options.length))

@bot.command
@lightbulb.option('phonenum', 'Enter in a phone number.')
@lightbulb.command('phonenumchecker', 'Checks if a phone number is legitimate.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def phonenumchecker(ctx):
    await ctx.respond(phone_number_validator.determine_malicious_phone_num(ctx.options.phonenum))

@bot.command
@lightbulb.option('file', 'Upload file.')
@lightbulb.command('uploadfile','Upload File')
@lightbulb.implements(lightbulb.SlashCommand)
async def uploadfile(ctx):
    attachment_url = ctx.message.attachments[0].url
    file_request = requests.get(attachment_url)
    print(file_request.content)

@bot.command
@lightbulb.option('hash', 'Input to get hash.')
@lightbulb.command('gethash', 'Get hash code from input.')
@lightbulb.implements(lightbulb.SlashCommand)
async def gethash(ctx):
    await ctx.respond(get_hash.get_hash(ctx.options.hash))

bot.run()