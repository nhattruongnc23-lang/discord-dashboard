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
