#using lightbulb hikari
from asyncio import constants
import lightbulb
import hikari
import datetime




bot = lightbulb.BotApp(token='MTAwNjgzOTM5ODQ1NDc5NjM1OQ.Gw9jnc._vbyskUePnzrHgi23qZwghRb2vBZCLLnglCOZo', 
                        default_enabled_guilds=(986249371077193748))#guild is used to take server id and seprate it from other servers
@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print('bot started')

@bot.command
@lightbulb.command('ping', 'sayd pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('pong!')
 
@bot.command
@lightbulb.command('latency','this command will show the latency of the server connection')
@lightbulb.implements(lightbulb.SlashCommand)
async def Ping(ctx):
    if (ctx == 'latency'):
        await ctx.respond('server responce time is:\t', {round(bot.latency*1000)},'ms')

@bot.command()
@lightbulb.option("user", "User to greet", hikari.User)
@lightbulb.command("greet", "Greets the specified user")
@lightbulb.implements(lightbulb.PrefixCommand)
async def greet(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hello {ctx.options.user.mention}!")

@bot.command()
@lightbulb.option("num2", "Second number", type=int)
@lightbulb.option("num1", "First number", type=int)
@lightbulb.command("add", "Adds the two given numbers together")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx: lightbulb.Context) -> None:
    """Adds the two given numbers together"""
    num1, num2 = ctx.options.num1, ctx.options.num2
    await ctx.respond(f"{num1} + {num2} = {num1 + num2}")

@bot.command()
@lightbulb.option("reason", "Reason for the ban", required=False)
@lightbulb.option("user", "The user to ban.", type=hikari.User)
@lightbulb.command("ban", "Ban a user from the server.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.SlashContext) -> None:
    """Ban a user from the server with an optional reason."""
    if not ctx.guild_id:
        await ctx.respond("This command can only be used in a guild.")
        return

    # Create a deferred response as the ban may take longer than 3 seconds
    await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE)
    # Perform the ban
    await ctx.app.rest.ban_user(ctx.guild_id, ctx.options.user.id, reason=ctx.options.reason or hikari.UNDEFINED)
    # Provide feedback to the moderator
    await ctx.respond(f"Banned {ctx.options.user.mention}.\n**Reason:** {ctx.options.reason or 'No reason provided.'}")

@bot.command()
@lightbulb.option("user", "User to greet", hikari.User)
@lightbulb.command("greet", "Greets the specified user")
@lightbulb.implements(lightbulb.SlashCommand)
async def greet(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hello {ctx.options.user.mention}!")


bot.run()