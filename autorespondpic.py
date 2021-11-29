pic_ext = ['.jpg', '.png', '.jpeg', '.gif']

@BetterGhost.listen()
async def on_message(message):
    for ext in pic_ext:
        if message.content.endswith(ext):
            await message.reply("get don't send that here men")