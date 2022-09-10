import hikari
import lightbulb

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

bot = hikari.GatewayBot(token='MTAxNzk5Njk2MjI2NTU3NTQ5NQ.GxrtRN.o-LJ-grUAAK-GikSyuHjd0vjkgwsN9C3OEvby8')
bot.run()
