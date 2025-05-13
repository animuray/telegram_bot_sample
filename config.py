import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get("BOT_TOKEN")
admins_id = os.environ.get("admin_id")
