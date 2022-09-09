
import discord
import json


with open("config.json", "r") as f:
    config = json.load(f)


def open_and_read_file(filename):
    with open(filename, "r", encoding="utf8") as f:
        data = f.read()
    return data


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.reply('你好! 🛂', mention_author=True)

        if message.content.startswith("!cring"):
            await message.channel.send(
                open_and_read_file("ccp.txt")
            )


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config["token"])
