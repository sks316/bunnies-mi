import asyncio
import aiohttp
import aiofiles
import json
import time
import os

import config

from mi.ext import commands, tasks
from mi.framework import Note
from mi.framework.router import Router
from mi.wrapper.file import MiFile

async def connect_channel(ws):
    await Router(ws).connect_channel(['global', 'main'])

class bunnybot(commands.Bot):
    def __init__(self):
        super().__init__()

    async def on_ready(self, ws):
        await connect_channel(ws)
        self.checktime.start()
        print(f"Online! {self.user.name} {self.user.id}")

    async def on_reconnect(self, ws):
        await connect_channel(ws)

    

    @tasks.loop(3600)
    async def checktime(self):
        #--ensure an hour has actually passed since last post, if this isn't here then the bot will post a new bunny with every reboot, possibly causing more than one post per hour--#
        if os.path.exists("timestamp.txt"):
            with open('timestamp.txt', 'r') as f:
                timestamp = f.read()
            if float(time.time()) - float(timestamp) > 3599:
                newtimestamp = time.time()
                with open('timestamp.txt', 'w') as f:
                    f.write(str(newtimestamp))
                bot.postbunny()
            else:
                print("it hasn't been an hour - no bunny posted.")
        #--if no timestamp.txt exists in the current directory, make a new one and post a bunny--#
        else:
            timestamp = time.time()
            with open('timestamp.txt', 'w') as f:
                f.write(str(timestamp))
            print("a new timestamp.txt has been created in the bot directory. please don't delete this file, it's important and helps make sure a bunny is posted only every hour!")
            await bot.postbunny()
            
    

    async def postbunny(self):
        #--get info from bunnies.io--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.bunnies.io/v2/loop/random/?media=gif,png,mp4') as bunny:
                data = await bunny.json()
                image = data["media"]["mp4"]
                seen = data["thisServed"]
                total = data["totalServed"]
                id = data["id"]
        #--download the bunny--#
        async with aiohttp.ClientSession() as session:
            async with session.get(image) as mp4:
                assert mp4.status == 200
                data = await mp4.read()
        #--write it to a file in the same directory as the bot--#
        async with aiofiles.open("bunny.mp4", "wb") as outfile:
            await outfile.write(data)
        #--now collect the info into a string and upload the bunny--#
        text = f"This bunny has been seen {seen} times.\n\n{total} total bunnies served.\n\nhttps://www.bunnies.io/#{id}\n\n#bot #bunny #bnuy #rabbit #animals"
        await bot.client.note.send(content=text, files=[MiFile(path="bunny.mp4")])
        print("sent bunny!")



if __name__ == '__main__':
    bot = bunnybot()
    asyncio.run(bot.start(config.homeserver, config.token))