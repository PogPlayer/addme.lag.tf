import config as c 
from functions import functions
import re, datetime, random

import nextcord as nc
from nextcord.ext import commands, application_checks
from nextcord.ext.application_checks import ApplicationMissingPermissions


Modbot = commands.Bot(command_prefix="p!",intents=nc.Intents.all())
@Modbot.event
async def ApplicationMissingPermissions(interaction,erorr):
    embed = nc.Embed(title="Missing Permissions", description=f"{erorr}")
    await interaction.response.send_message(embed=embed)


@Modbot.event
async def on_ready():
    print(c.header)

@Modbot.slash_command()
@application_checks.has_permissions(moderate_members=True)
async def mute(interaction: nc.Interaction,duration: str, member: nc.Member,reason: str):
    if re.search("m",duration):
        x = duration.replace("m","")
        p = int(x)
        x = p * 60
        timeout_duration = datetime.timedelta(minutes=p)
    if re.search("h",duration):
        x = duration.replace("h","")
        p = int(x)
        x = p * 3600
        timeout_duration = datetime.timedelta(hours=p)
    if re.search("d",duration):
        x = duration.replace("d","")
        p = int(x)
        x = p * 86400
        timeout_duration = datetime.timedelta(days=p)
    print(x)
    await member.timeout(timeout_duration,reason=reason)

@Modbot.slash_command()
@application_checks.has_permissions(kick_members=True)
async def kick(interaction: nc.Interaction, member: nc.Member,reason: str):
    servembed = nc.Embed(title="Kicked ",description=f"{member.name} has been kicked from {interaction.guild.name}\nReason: {reason}\nBy: <@{interaction.user.id}>")
    userembed = nc.Embed(title=f"You Have Been Kicked from {interaction.guild.name}",description=f"Reason: {reason}\nBy: <@{interaction.user.id}> [Profile Link](https://discord.com/users/{interaction.user.id})")
    await interaction.response.send_message(embed=servembed)
    await member.send(embed=userembed)
    await member.kick(reason=reason)

@Modbot.slash_command()
@application_checks.has_permissions(ban_members=True)
async def ban(interaction: nc.Interaction, member: nc.Member,reason: str):
    servembed = nc.Embed(title="Banning ",description=f"{member.name} is now banned from {interaction.guild.name}\nReason: {reason}\nBy: <@{interaction.user.id}>")
    userembed = nc.Embed(title=f"You Have Been Banned from {interaction.guild.name}",description=f"Reason: {reason}\nBy: <@{interaction.user.id}> [Profile Link](https://discord.com/users/{interaction.user.id})")
    await interaction.response.send_message(embed=servembed)
    await member.send(embed=userembed)
    await member.ban(reason=reason)
@Modbot.slash_command()
@application_checks.has_permissions(moderate_members=True)
async def delwarn(interaction: nc.Interaction, warnid: str):
    functions.delwarn(warnid)
    embed = nc.Embed(title="Warning Deleted",description="That warning was deleted")
    await interaction.response.send_message(embed=embed)
@Modbot.slash_command()
@application_checks.has_permissions(manage_messages=True)
async def say(interaction, thing):
    await interaction.channel.send(thing)
@Modbot.slash_command()
@application_checks.has_permissions(moderate_members=True)
async def warn(interaction: nc.Interaction, user: nc.Member, reason: str):
    functions.GiveWarns(user.id,reason,interaction.user.id)
    warned = nc.Embed(title=f"You Have Recieved a warning in {interaction.guild.name}",description=f"Reason: {reason}\nBy: <@{interaction.user.id}>")
    x = functions.getWarnings(user.id)
    embed = nc.Embed(title=f"Warned {user.name}",description=f"This user is now on {len(x)} Warns")
    await interaction.response.send_message(embed=embed)
    await user.send(embed=warned)
@Modbot.slash_command()
async def 8ball(interaction, question: str):
    responses = ["Yes", "No", "Maybe", "It is certain", "Ask again later", "Without a doubt"]
    x = random.choice(responses)
    embed = nc.Embed(title=f"Question: {question}",description=f":8ball: {x}")
    await interaction.response.send_message(embed=embed)
@Modbot.slash_command()
async def warns(interaction: nc.Interaction, user: nc.Member):
    x = functions.getWarnings(user.id)
    if x == "No Warns":
        embed = nc.Embed(title="This User Has No Warns.")
        await interaction.response.send_message(embed=embed)
        return
    warn = 1
    embed = nc.Embed(title=f"Warning`s For {user.name}",description=f"This User has {len(x)} Warns")
    for row in x:
        reason = row["reason"]
        by = row["by"]
        warnid = {row["warnid"]}
        embed.add_field(name=f"Warning {warn}",value=f"Reason: {reason}\nBy: <@{by}>\nWarning ID: {warnid}")
        warn = warn + 1
    await interaction.response.send_message(embed=embed)
@Modbot.slash_command()
async def avatar(interaction, member: nc.Member = None):
    member = member or interaction.user  # if no member is mentioned, use the author of the message
    embed = nc.Embed(title=f"{member.name}'s avatar")
    embed.set_image(url=member.avatar.url)
    await interaction.response.send_message(embed=embed)
@mute.error
async def kick_error(interaction, error):
    x = str(error)
    p = x.replace("You are missing ","")
    x = p.replace("permission(s) to run this command.","")
    embed = nc.Embed(title="Uh Oh Permission Error.",description=f"You Require {x} to run that command.")
    await interaction.response.send_message(embed=embed)
@ban.error
async def kick_error(interaction, error):
    x = str(error)
    p = x.replace("You are missing ","")
    x = p.replace("permission(s) to run this command.","")
    embed = nc.Embed(title="Uh Oh Permission Error.",description=f"You Require {x} to run that command.")
    await interaction.response.send_message(embed=embed)
@kick.error
async def kick_error(interaction, error):
    x = str(error)
    p = x.replace("You are missing ","")
    x = p.replace("permission(s) to run this command.","")
    embed = nc.Embed(title="Uh Oh Permission Error.",description=f"You Require {x} to run that command.")
    await interaction.response.send_message(embed=embed)
@warn.error
async def kick_error(interaction, error):
    x = str(error)
    p = x.replace("You are missing ","")
    x = p.replace("permission(s) to run this command.","")
    embed = nc.Embed(title="Uh Oh Permission Error.",description=f"You Require {x} to run that command.")
    await interaction.response.send_message(embed=embed)
@delwarn.error
async def kick_error(interaction, error):
    x = str(error)
    p = x.replace("You are missing ","")
    x = p.replace("permission(s) to run this command.","")
    embed = nc.Embed(title="Uh Oh Permission Error.",description=f"You Require {x} to run that command.")
    await interaction.response.send_message(embed=embed)

Modbot.run(c.token)