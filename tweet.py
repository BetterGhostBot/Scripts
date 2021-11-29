@BetterGhost.command(name='tweet')
async def tweet(ctx, username, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}').json()
    embed = discord.Embed(color=0xFFFAFA,)
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed)