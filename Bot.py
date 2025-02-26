# -*- coding: utf-8 -*-
# Coded By @zero0sec
from pyrogram import Client
from threading import Thread  
import Shell
import platform
import getpass
import subprocess
import os
import json

ADMIN_USER_ID = 56  # ur User ID
BOT_API_TOKEN = ""  # Ur Token

if BOT_API_TOKEN is not None and ADMIN_USER_ID is not None:
    try:
        ADMIN_USER_ID = int(ADMIN_USER_ID)
    except Exception:
        print("\nError : ADMIN_USER_ID Is Not Integer .\n")
    else:
        Bot = Client(
            "Bot",
            api_id=25957940,  # ur Api ID
            api_hash="53e75cad496e7419d50e809289ce6009",  # ur Api Hash
            bot_token=BOT_API_TOKEN
        )

        @Bot.on_message()
        async def main(client, message):
            if message.from_user.id == ADMIN_USER_ID:
                if message.text == "/start":
                    await Bot.send_message(
                        message.chat.id,
                        "**Ubuntu Server Remote v1.0**\n**==============================**\n**Welcome, Now I'm online!!!  ->\nChannel: @zero0sec\nFor help => /help **"
                    )
                elif message.text == "/help":
                    await Bot.send_message(
                        message.chat.id,
                        "**Help :**\n\n[+] **Run Shell** :\n\n/run_shell <**command**>\n\n**===================================**\n\n[+] **Get Information Of Server** :\n\n/info\n\n[+] **Save File To Server** :\n\n/save_file (**Reply To File**)"
                    )
                elif message.text == "/info":
                    await Bot.send_message(
                        message.chat.id,
                        f"Information Of **Server**:\n\n**OS : {platform.uname()[0]}**\n**Kernel : {platform.uname()[2]}**\n**Processor : {platform.uname()[4]}**\n**Username : {getpass.getuser()}**\n**Uptime : {subprocess.getoutput('uptime -p')}**"
                    )
                elif message.text.startswith("/run_shell"):
                    code = message.text[10:].strip()
                    if code:
                        Thread(target=Shell.Shell, args=("Shell", code, Bot, message.chat.id)).start()
                    else:
                        await Bot.send_message(message.chat.id, "Please Enter Shell Command !!!")
                elif message.text == "/save_file":
                    if not message.reply_to_message or not message.reply_to_message.document:
                        await Bot.send_message(message.chat.id, "**Please Reply To Document File !!!**")
                    else:
                        msg_id = await Bot.send_message(message.chat.id, "**Downloading File ...**")
                        await message.reply_to_message.download(f"./{message.reply_to_message.document.file_name}")
                        await Bot.edit_message_text(message.chat.id, msg_id.id, "**File Saved !!!**")

        Bot.run()
else:
    print("\nError : BOT_API_TOKEN Or ADMIN_USER_ID Is NULL .\n")
# Coded By @zero0sec
