
import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "KINGBOTOFFICIAL")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/796626d1106726dbfd061.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DaisyXhelper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "KINGBOTOFFICIALCHAT")
PROJECT_NAME = getenv("PROJECT_NAME", "**⭐ MUSIC BOT ⭐ 2.0**")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Kartikrajofficial/MUSICBOT-2.0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
