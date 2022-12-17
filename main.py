import discord
import os
import asyncio
import random
from discord import FFmpegPCMAudio
from discord import app_commands


class main(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}")


client = main()
tree = app_commands.CommandTree(client)


@client.event
async def on_voice_state_update(member, before, after):
    voice = discord.utils.get(client.voice_clients, guild=member.guild)
    if after.channel and after.channel != before.channel:
        if voice is None:
            voice_channel = member.voice.channel
            await asyncio.sleep(0.5)
            vc = await voice_channel.connect()
            vc.play(FFmpegPCMAudio('./fart.mp3'))
            await asyncio.sleep(6)
            await member.guild.voice_client.disconnect()


@tree.command(name="fart", description="fart :)")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("farting")
    voice = discord.utils.get(client.voice_clients, guild=interaction.user.guild)
    if voice is None:
        voice_channel = interaction.user.voice.channel
        await asyncio.sleep(0.5)
        vc = await voice_channel.connect()
        vc.play(FFmpegPCMAudio("./fart.mp3"))
        await asyncio.sleep(6)
        await interaction.guild.voice_client.disconnect()



client.run('token here')
