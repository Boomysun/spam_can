import pickle
from os import pipe
from sys import stdout
from typing import DefaultDict
from discord_components import component
from discord_components.component import Select, SelectOption
from discord import guild, message
from discord_components import ActionRow, Button, ButtonStyle, ComponentsBot
import pygame

def main():
    bot = ComponentsBot(command_prefix = "?")

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}!")
        
    @bot.command()
    async def t (ctx):
        await ctx.channel.send("bonk")


    bot.run("ODg2MzE1NjI5NTQ2NzMzNTk5.YTzzwQ.q-rx7nBPo9xcgBSQ4piQwRXqwn0")

main()