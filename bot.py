import hikari
import lightbulb
import requests
import ip_info
import link_malware_checker
import pass_generator
import phone_number_validator
import email_validator
import get_hash
import url_shortener
import base_encode_decode

bot = lightbulb.BotApp(token='MTAxNzk5Njk2MjI2NTU3NTQ5NQ.GxrtRN.o-LJ-grUAAK-GikSyuHjd0vjkgwsN9C3OEvby8', default_enabled_guilds=(1017526173061881946))

#.\env\Scripts\activate
#python bot.py

"""@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    #print(event.message.attachments[0].url)
    print(str(event.author) + " " + event.content)"""

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

"""@bot.command
@lightbulb.command('ping', 'Say pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')"""

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
@lightbulb.option('email', 'Enter in a email.')
@lightbulb.command('emailchecker', 'Checks if an email is legitimate and non-malicious.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def emailchecker(ctx):
    await ctx.respond(email_validator.determine_malicious_email(ctx.options.email))


@bot.command
@lightbulb.option('hash', 'Input to get hash.')
@lightbulb.command('gethash', 'Get hash code from input.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def gethash(ctx):
    await ctx.respond(get_hash.get_hash(ctx.options.hash))

@bot.command
@lightbulb.option('attachment', 'Input url of file. Use /getfileurl command to get file url.', type = hikari.OptionType.ATTACHMENT)
@lightbulb.command('checkfile', 'Scans file for protentional threats.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def checkfile(ctx):
    print(ctx.options.attachment.url)
    await ctx.respond(get_hash.file_info(ctx.options.attachment.url))

@bot.command
@lightbulb.option('url', 'Enter in url of website', type = str)
@lightbulb.command('linkshortener', 'Shorten long links to shorter ones.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def linkshortener(ctx):
    await ctx.respond(url_shortener.file_info(ctx.options.url))

@bot.command
@lightbulb.option('message', 'Type in a message.', type = str)
@lightbulb.command('encode32', 'Encodes a message in base32.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def encode32(ctx):
    await ctx.respond(base_encode_decode.encode_32(ctx.options.message))

@bot.command
@lightbulb.option('message', 'Type in a message.', type = str)
@lightbulb.command('decode32', 'Decodes a message in base32.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def decode32(ctx):
    await ctx.respond(base_encode_decode.decode_32(ctx.options.message))

@bot.command
@lightbulb.option('message', 'Type in a message.', type = str)
@lightbulb.command('encode64', 'Encodes a message in base64.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def encode64(ctx):
    await ctx.respond(base_encode_decode.encode_64(ctx.options.message))

@bot.command
@lightbulb.option('message', 'Type in a message.', type = str)
@lightbulb.command('decode64', 'Decodes a message in base64.', ephemeral = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def decode64(ctx):
    await ctx.respond(base_encode_decode.decode_64(ctx.options.message))

bot.run()