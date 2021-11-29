# +--------------------------------------------------------------------------+
# | Script made by Imf44#6363, If you have a problem or suggestion, tell me! |
# +--------------------------------------------------------------------------+
@BetterGhost.command(name="pdump", description="Dumps porn from the selected website", usage="pdump [website] (subreddit) [amount] (tags)")
async def porndumpharam(ctx):
    
    splitTxt = ctx.message.content.split(" ")

    if len(splitTxt) < 3:
        message = await ctx.send("[:red_circle:] Wrong args, usage: pdump [website] (subreddit) [amount] (tags)")
        await asyncio.sleep(2) 
        message.delete()
    else:
        supportedWebsites = ["e6", "r34", "reddit"]

        # This cookie makes it so the site doesnt age-check you.
        # first one is for e6, other is for reddit - idk if they serve a purpose anymore
        age_cookie = {'dw': "seen", 'over18': '1'}
        
        webisteToSearch = splitTxt[1].lower()
        # copy default request headers & update them
        new_headers = requests.utils.default_headers()
        # Some api's need API-Keys, the user agent fixes this :) (*CHANGE THIS IF IT DOESNT WORK*)
        new_headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'})

        if webisteToSearch in supportedWebsites:
            # real shit 
            if webisteToSearch == "e6":
                if not splitTxt[2].isdigit():
                    await ctx.send("[:red_circle:] Invalid Usage, specify a max amount (Integer).")
                    return

                reqUrl = ""
                if len(splitTxt) == 3:
                    # if no tags specified, just get all posts
                    reqUrl = "https://e621.net/posts.json?rating:e&limit="+str(splitTxt[2])
                    print_cmd(f"{fg.cWhite}[{fg.cBlue}PDUMP{fg.cWhite}] {fg.cBlue}Searching e621.net with no specified filter tags.")
                else:
                    # formatting the filter tags by separating them with +
                    tagFormatted = "+".join(splitTxt[3:])
                    reqUrl = f"https://e621.net/posts.json?tags={tagFormatted}+rating:e&limit="+str(splitTxt[2])
                    print_cmd(f"{fg.cWhite}[{fg.cBlue}PDUMP{fg.cWhite}] {fg.cBlue}Searching e621.net with the tags: {fg.cYellow}"+tagFormatted)

                response = requests.get(reqUrl, cookies=age_cookie, headers=new_headers).json()
                coloredE6 = f"{fg.cWhite}[e{fg.cYellow}6{fg.cOrange}2{fg.cBlue}1{fg.cWhite}]{fg.cBlue}"

                for post in response['posts']:
                    if post['sample']['url'] is not None:
                        await ctx.send(post['sample']['url'])
                        print_info(f"{coloredE6} Sent NSFW image {fg.cYellow}(SAMPLE-RES) {fg.cBlue}to {fg.cGrey}#"+ctx.message.channel.name)
                        await asyncio.sleep(0.5)
                    elif post['file']['url'] is not None:
                        await ctx.send(post['file']['url'])
                        print_info(f"{coloredE6} Sent NSFW image {fg.cOrange}(FULL-RES) {fg.cBlue}to {fg.cGrey}#"+ctx.message.channel.name)
                        await asyncio.sleep(0.5)
                    else:
                        print_info(f"{coloredE6} Skipped post because no links were avaliable.{fg.cOrange} ID: "+str(post['id']))
                        continue
            elif webisteToSearch == "r34":
                if not splitTxt[2].isdigit():
                    await ctx.send("[:red_circle:] Invalid Usage, specify a max amount (Integer).")
                    return

                reqUrl = ""
                # Thankfully this API is very similar to e621's API
                if len(splitTxt) == 3:
                    # if no tags specified, just get all posts
                    reqUrl = "https://r34-json-api.herokuapp.com/posts?limit="+str(splitTxt[2])
                    print_cmd(f"{fg.cWhite}[{fg.cGreen}PDUMP{fg.cWhite}] {fg.cGreen}Searching rule34.xxx with no specified filter tags.")
                else:
                    # formatting the filter tags by separating them with +
                    tagFormatted = "+".join(splitTxt[3:])
                    reqUrl = f"https://r34-json-api.herokuapp.com/posts?tags={tagFormatted}&limit="+str(splitTxt[2])

                    print_cmd(f"{fg.cWhite}[{fg.cGreen}PDUMP{fg.cWhite}] {fg.cGreen}Searching rule34.xxx with the tags: {fg.cGrey}"+tagFormatted)

                response = requests.get(reqUrl, cookies=age_cookie, headers=new_headers).json()
                coloredR34 = f"{fg.cWhite}[{fg.cGreen}RULE{fg.cYellow}34{fg.cWhite}]{fg.cGreen}"

                # If you input an invalid tag, the API will return nothing.
                if len(response) < 10:
                    await ctx.send("[:red_circle:] Didn't find any post, maybe tags are wrong")
                    return

                for post in response:
                    if post['sample_url'] is not None:
                        await ctx.send(post['sample_url'])
                        print_info(f"{coloredR34} Sent NSFW image {fg.cYellow}(SAMPLE-RES) {fg.cGreen}to {fg.cGrey}#"+ctx.message.channel.name)
                        await asyncio.sleep(0.5)
                    elif post['file_url'] is not None:
                        await ctx.send(post['file_url'])
                        print_info(f"{coloredR34} Sent NSFW image {fg.cOrange}(FULL-RES) {fg.cGreen}to {fg.cGrey}#"+ctx.message.channel.name)
                        await asyncio.sleep(0.5)
                    else:
                        print_info(f"{coloredR34} Skipped post because no links were avaliable. {fg.cOrange}ID: "+str(post['id']))
                        continue
            elif webisteToSearch == "reddit":
                reqUrl = f"https://reddit.com/r/{str(splitTxt[2])}/new.json"
                print_cmd(f"{fg.cWhite}[{fg.cRed}PDUMP{fg.cWhite}] {fg.cRed}Searching reddit.com in the subreddit: {fg.cOrange}r/"+str(splitTxt[2]))
               
                response = requests.get(reqUrl, cookies=age_cookie, headers=new_headers).json()
                
                json_data = response["data"]["children"]
                
                for index, post in enumerate(json_data):
                    if len(splitTxt) > 2 and splitTxt[3].isdigit():
                        if index >= int(splitTxt[3]):
                            return

                    await ctx.send(post["data"]["url"])
                    print_info(f"{fg.cWhite}[{fg.cRed}REDDIT{fg.cWhite}]{fg.cRed} Sent NSFW image from {fg.cOrange}r/{str(splitTxt[2])} {fg.cRed}to {fg.cGrey}#"+ctx.message.channel.name)
                    await asyncio.sleep(0.5)
        else:
            supported = ", ".join(supportedWebsites)
            await ctx.send("[:red_circle:] `"+webisteToSearch+"` is an invalid website, supported websites: " + supported)


        
