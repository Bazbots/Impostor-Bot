import discord
import os
import threading
import unittest
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
import time
import asyncio
import dbl
from discord import utils, Client
from discord import Member as DiscordMember
from discord.ext.commands import BadArgument, CommandNotFound, MissingRequiredArgument
from colorama import Fore
from replit import db

now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

client = commands.Bot(command_prefix="$")
client.remove_command("help")


@client.event
async def on_guild_join(guild):
	print(Fore.GREEN + f"I have joined {guild}")
	print(Fore.RESET)
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			await channel.send(
			    ":mailbox:Hi there!:mailbox:\n\n:exclamation:I am the Impostor - a bot created by Baz!:exclamation:\n\n:incoming_envelope:You can join my support server by running $help! and you can view all of my commands here as well!:incoming_envelope:\n\n:partying_face:Have fun!:partying_face:"
			)
		break


@client.event
async def on_guild_remove(guild):
	print(Fore.GREEN + f"I have left {guild}")
	print(Fore.RESET)


status = cycle([
    "Among Us on Discord! | Run $help or $commands for help!",
    "https://bazbots.github.io/Impostor-Bot/ | Run $website to gain a link!",
    "Happy Mother's Day! | Run $help for help!", "Version 1.3.8!",
    "Vote for us here at https://top.gg/bot/759436027529265172",
    "The GitHub Repository | $github for a link!",
    "In MAXIMUM Servers | Join our Support Server For more Information",
    "What do you think? | Run $feedback"
])


@tasks.loop(seconds=600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))
	print(Fore.GREEN + "Successfully changed status!")


BOTVERSION = "1.3.9"


@client.event
async def on_ready():
	print(Fore.BLUE + 'Successfully booted {0.user}\nVersion 1.3.9'.format(client))
	time.sleep(2)
	print(Fore.BLUE + "Booted at", boot_time)
	time.sleep(2)
	change_status.start()


Basic_Tier = bool
Bot_Voter = bool
Gold_Tier = bool
Diamond_Tier = bool

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send(":x:Error:x:\n:information_source:Command is either in the command vault or does not exist")
    print(Fore.GREEN + f"Error: {error}")
    
  
@client.event
async def on_dbl_vote(data):
	print(data)



@client.command()
async def help(ctx):
	await ctx.send(
	    "Need help? Join my support server!\nhttps://discord.gg/Sun4mtFjwE\nOr you can view all the current commands below!\n\n\n:robot:Current Commands::robot:\nUse prefix `$`\nhelp\nabout\ninvite\nversion\nfeedback\nwebsite\nvote\nservers\ncreator\ngithub\ntier {current/basic/gold/diamond}\nping\neject {user} {role}\nreport {your username} {problem}\nsus {user}"
	)


@client.command()
async def invite(ctx):
	await ctx.send(
	    ":incoming_envelope:Invite me here!:incoming_envelope:\n https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=217579073&redirect_uri=https%3A%2F%2Fdiscord.gg%2FnzsyDWg&scope=bot"
	)


@client.command()
async def about(ctx):
	await ctx.send(
	    ":question:A bit about The Impostor:question:\n\n:lock:100% Safe and Secure:lock:\n:england:English:england:\n:white_check_mark:Sus:white_check_mark:\n:spy:Impossible for Data Breaching:spy:"
	)


@client.command()
async def version(ctx):
	await ctx.send(
	    ":rocket:Current Version::rocket:\n`1.3.9`\n\n\n:inbox_tray:What's new to this update::inbox_tray:\n:white_check_mark:Updated $tier\n:white_check_mark:Added $claim\n\n:clock3:What is still to come::clock3:\n:clock3:More Errors\n:clock3:Solo Mode Among Us\n:clock3:Fixing the guild status issue\n:clock3:The return of $changeprefix\n$play and $modes\n\n:outbox_tray:What we removed::outbox_tray:\n:x:The sus command"
	)


@client.command()
async def website(ctx):
	await ctx.send(
	    ":desktop:Here is my Website::desktop:\nhttps://bazbots.github.io/Impostor-Bot/"
	)


@client.command()
async def vote(ctx):
	await ctx.send(
	    ":arrow_up:The bot can been found here::arrow_up:\nhttps://top.gg/bot/759436027529265172"
	)


@client.command()
async def servers(ctx):
	await ctx.send(
	    f"Currently playing Among Us in **{len(client.guilds)}** servers!")


@client.command()
async def creator(ctx):
	await ctx.send(
	    ":placard:The Impostor was a bot created by Baz!:placard:\n:one:This is actually his first ever coded bot!:one:\n:snake:It is a discord.py bot!:snake:\n:warning:The bot is not complete yet!:warning:\n:sparkling_heart:Show some love and join his server!:sparkling_heart:\n:calling: https://discord.gg/5jKA9kj :calling:"
	)


@client.command()
async def github(ctx):
	await ctx.send(
	    ":file_folder:Oke doke!:file_folder:\n:open_file_folder:Here is my GitHub Repo!:open_file_folder:\nhttps://github.com/Bazbots/Impostor-Bot"
	)


@client.command()
async def tier(ctx, tier):
  if tier == "current":
    await ctx.send(":free:You are in `Basic` Tier!:free:\nThis is Tier `1` out of 3!\n:free:Basic:free:\n:coin:Gold:coin:\n:gem:Diamond:gem:")
  else:
    pass
  if tier == "basic":
    await ctx.send(":question:What you can do at `Basic` Tier::question:\n:white_check_mark:Use all Basic commands (all under basic in $commands)\n:white_check_mark:You have access to certain modes (Standard and Crazy Colours)")
  else:
    pass
  if tier == "gold":
    await ctx.send(":coin:What you get when you reach `Gold` Tier::coin:\n:coin:Access to most modes(To be added soon)\n:coin:Multiplayer Mode\n:coin:A 10% higher chance of being Impostor")
  else:
    pass
  if tier == "diamond":
    await ctx.send(":gem:What you get at `Diamond` Tier::gem:\n:gem:Access to all modes, even before they are released!\n:gem:25% higher chance of being Impostor\n:gem:Able to suggest modes for the bot!")
  else:
    pass


@client.command()
async def feedback(ctx):
	await ctx.send(
	    ":pencil:Please answer this short survey to let us know how you feel about the bot::pencil:\nhttps://docs.google.com/forms/d/e/1FAIpQLSeS_fcVh5_GRBmYCFw5qkxU29lSLU1zsTkioePy7Kp8roTVig/viewform?usp=sf_link"
	)


@client.command()
async def ping(ctx):
	await ctx.send(f"Pong!\nYour ping is {round(client.latency * 1000)}ms!")

@client.command()
async def eject(ctx, name, role):
  if role == "crew":
    await ctx.send(f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•\n　ﾟ　　 {name} was not The Impostor.　 。　\n'　　。 . 　•　  1 Impostor remains 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •")
  else:
    pass
  if role == "imp":
    await ctx.send(f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•\n　ﾟ　　 {name} was The Impostor.　 。　\n'　　。 . 　•　  0 Impostors remain 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •")
  else:
    pass

@eject.error
async def no_role(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f":x:Error:x:\n:information_source:{error}")
    print(Fore.GREEN + f"Error: {error}")

  

@client.command()
async def report(ctx, username, problem):
  print(Fore.GREEN + f"{username} has a problem: {problem}")
  await ctx.send("Done!\nThanks for reporting this issue, we will look into it!")

@report.error
async def no_prob_or_user(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send(f":x:Error:x:\n:information_source:{error}")
    print(Fore.GREEN + f"Error: {error}")


@client.command()
async def claim(ctx):
  await ctx.send("Soon, you will get voter exclusive perks if you vote for us on top.gg! Run $vote to get the link!")




keep_alive()
client.run(os.getenv("TOKEN"))
