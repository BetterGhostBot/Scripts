#Please check api.zeynox.red before to see the available animals list

import json
import urllib.request

@BetterGhost.command(name="animal", description="Shows you a random animal photo using zeynox.red api", usage="animal [type]")
async def animal(ctx,animal):
    url = "http://api.zeynox.red/api"
    response = urllib.request.urlopen(url)

    data = json.loads(response.read())
    if __embedmode__:

        message = discord.Embed(title=f"A random {animal.lower()} image",description = "powered by api.zeynox.red", color=__embedcolour__)
        message.set_image(url=data[animal.lower()])
        message.set_thumbnail(url = __embedimage__)
        
        await ctx.send(embed = message)
    else:
        await ctx.send(data[animal.lower()])