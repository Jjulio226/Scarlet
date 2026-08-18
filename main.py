import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intens.all()
bot = Commands.Bot("/", intents=intents)

load_dotenv()

api_key = os.getenv("API_KEY")
db_password = os.getenv("DATABASE_PASSWORD")