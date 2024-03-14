import os
from discord.ext import commands
from dotenv import load_dotenv
import discord
from discord import Intents
from sentiment import SentimentBot

# Load discord_token from dotenv file
load_dotenv()
token: str = os.getenv('DISCORD_TOKEN')

# Initiate client
intents: Intents = Intents.default()
intents.message_content = True # NOQA
bot = commands.Bot(command_prefix="?pim ", intents=intents, ignore_whitespace=True)
sentiment_bot = SentimentBot()

# Basic catch-all for unknown/unimplemented commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send("Unknown command.")
    else:
        await ctx.channel.send("Something went wrong. Please refer to '?help' to check if the command is being used properly.")


# Prints to terminal when bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


# Allows users with manage_roles permissions to give a new role to a user
@bot.command(aliases=['giverole'])
@commands.has_permissions(manage_roles=True)
async def give_role(ctx: commands.Context, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.channel.send(f"{member.name} is now a {role.name}")


# Allows users with manage_roles permissions to remove a role from a user
@bot.command(aliases=['removerole'])
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx: commands.Context, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.channel.send(f"{member.name} is no longer a {role.name}")


# Allows users with sufficient permissions to kick members
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx: commands.Context, member: discord.Member, reason: str):
    await member.kick(reason=reason)
    await ctx.channel.send(f"Kicked [{member.name}] for {reason}")


# Allows users with sufficient permissions to ban members
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx: commands.Context, member: discord.Member, reason: str):
    await member.ban(reason=reason)
    await ctx.channel.send(f"Banned [{member.name}] for {reason}")


# This command reads through all messages from other users - this is where sentiment analysis will be used
@bot.event
async def on_message(message):
    # Process commands before analyzing message
    await bot.process_commands(message)
    # do not self-reply
    if message.author == bot.user:
        return
    print(sentiment_bot.polarity(message.content))


bot.run(token)
