import pickle
from os import pipe
from sys import stdout
from typing import DefaultDict
from discord_components import component
from discord_components.component import Select, SelectOption
from discord import guild, message
import discord
from discord_components import ActionRow, Button, ButtonStyle, ComponentsBot
import time
import random
import requests
from bs4 import BeautifulSoup
import re
import subprocess
import psutil

bot = ComponentsBot(command_prefix = "$")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    



bot.run("ODg2MzE1NjI5NTQ2NzMzNTk5.YTzzwQ.q-rx7nBPo9xcgBSQ4piQwRXqwn0")
