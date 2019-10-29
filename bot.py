import discord
from tokens import dtoken

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        await message.channel.send(f'Hello {message.author}.')

        if message.content == 'foo':
            await message.channel.send('bar')

client = Client()
client.run(dtoken['bot_token'])
