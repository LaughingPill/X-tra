""".admin Plugin for @XtraTgBot"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`Good News! I am alive ψ(｀∇´)ψ`**\n\n"
                     "`Database Status: Databases functioning normally!\n`"
                     "**◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆**\n"
                     "\nAlways with you, my master!\n`"
                     f"`My demonic owner`: {DEFAULTUSER} ( •̀ᴗ•́ )و \n"
                     "**◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆**\n"
                     "**When the devil walks the earth, the evil shall be released**")

