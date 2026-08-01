import discord
import asyncio

from config import TOKEN

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

bot_loop = None


@client.event
async def on_ready():
    global bot_loop

    bot_loop = asyncio.get_running_loop()

    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🐱 MEOW MEOW CONTROL PANEL")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🤖 Bot        : {client.user}")
    print(f"🖥 Máy chủ    : {len(client.guilds)}")
    print("🌐 Dashboard  : Đã khởi động")
    print("⚡ Trạng thái : Hoạt động")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()


def start_bot():
    client.run(TOKEN)


def get_guilds():
    guilds = []

    for guild in client.guilds:
        guilds.append({
            "id": str(guild.id),
            "name": guild.name
        })

    return guilds


def get_channels(guild_id):
    guild = client.get_guild(int(guild_id))

    if guild is None:
        return []

    channels = []

    for channel in guild.text_channels:
        channels.append({
            "id": str(channel.id),
            "name": channel.name
        })

    return channels


async def _send_message(channel_id, message):
    channel = client.get_channel(int(channel_id))

    if channel is None:
        return False

    await channel.send(message)
    return True


def send_message(channel_id, message):
    future = asyncio.run_coroutine_threadsafe(
        _send_message(channel_id, message),
        bot_loop
    )

    return future.result()
