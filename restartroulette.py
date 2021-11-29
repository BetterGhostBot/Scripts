@BetterGhost.command(name="restartroulette", description="yesyes", usage="restartroulette")
async def restarttoulette(BetterGhost):
    if random.randint(0, 6) == 1: 
        if is_windows():
            os.system("shutdown /r")
        elif is_linux():
            os.system("sudo reboot")
    else:
        await BetterGhost.send("Not restarting today <:sweat_smile:878034698289438720>.")