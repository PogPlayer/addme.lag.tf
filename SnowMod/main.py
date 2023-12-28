import nextcord
import config as c
from functions.checkbannedlist import isbanned
from nextcord.ext import commands
automod = ["a"]

snowmod = commands.Bot(command_prefix="snow.",intents=nextcord.Intents.all())
@snowmod.event
async def on_ready():
    print(c.header)
@snowmod.event
async def on_message(message):
    x = ""
    x = isbanned(automod, message.content)
    reason = f"SnowMOD"
    if x != False:
        embed = nextcord.Embed(title="Uh Oh.",description="That is a blacklisted word.")
        await message.delete()
        guild = message.guild # Fetch the guild from the message
        user = await guild.fetch_member(message.author.id) # Fetch the member from the guild
        user2 = snowmod.get_user(message.author.id)
        print(user)
        await user2.send(embed=embed)
        await user.timeout(600,reason)
    

@snowmod.slash_command()
async def add(interaction, word: str):
    print(f"{word} Added to Automod")
    automod.append(word)

snowmod.run(c.token)