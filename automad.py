madPeople = []
madMessages = ["mad", "stop bein angry", "lol u mad", "cope", "cope harder", "thanks for listening and coping hard lol"]

@BetterGhost.command(name="addmad", description="Add a user to the auto mad list.", usage="addmad (@user/id)")
async def addmad(ctx, user: discord.User):
    global madPeople
    madPeople.append(user.id)
    print_info(f"Added {user} to the auto mad list.")
    await ctx.send(f"Added `{user}` to the auto mad list.")


@BetterGhost.command(name="removemad", description="Remove a user from the auto mad list.", usage="removemad (@user/id)", aliases=["remmad", "delmad", "deletmad"])
async def removemad(ctx, user: discord.User):
    global madPeople
    madPeople.remove(user.id)
    print_info(f"Removed {user} from the auto mad list.")
    await ctx.send(f"Removed `{user}` from the auto mad list.")

@BetterGhost.command(name="addmadmessage", description="Add a message to the mad message responses.", usage="addmadmessage [message]", aliases=["addmadmsg"])
async def addmadmessage(ctx, *, message):
    global madMessages
    madMessages.append(message)
    print_info(f"Added {message} to the mad message responses.")
    await ctx.send(f"Added `{message}` to the mad message responses.")

@BetterGhost.listen()
async def on_message(message):
    global madPeople, madMessages
    if message.author.id in madPeople:
        try:
            await message.reply(random.choice(madMessages))
        except:
            pass
        try:
            print_info(f"Replied to {message.author} in {message.guild} because hes mad.")
        except:
            print_info(f"Replied to {message.author} because hes mad.")