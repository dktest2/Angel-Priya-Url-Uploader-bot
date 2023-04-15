#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    if update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.HELP_USER,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    if update.from_user.id in (Config.AUTH_USERS & Config.LAZY_DEVELOPER):
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.LAZY_DEVELOPER_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/movie_on1"),
                        InlineKeyboardButton("✪ 𝚃𝙾𝙽𝚈 𝚂𝚃𝙰𝚁𝙺 ✪", url="https://t.me/Movie_search_V4_bot"),
                        InlineKeyboardButton("⚡️ 𝚄𝙿𝙳𝙰𝚃𝙴", url="https://t.me/movie_a1"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙼𝚈 𝙰𝙻𝙻 𝙱𝙾𝚃𝚂 💢⭑", url="https://t.me/movie_a1/162")],
                    [InlineKeyboardButton("🦋 ⭑┗━━┫⦀⦙ 𝙼𝙳𝙸𝚂𝙺 𝙲𝙷𝙰𝙽𝙽𝙻𝚂 ⦙⦀┣━━┛⭑ 🦋", url="https://t.me/+gtlaKqnF9rVlMWRl")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    elif update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/movie_on1"),
                        InlineKeyboardButton("✪ 𝚃𝙾𝙽𝚈 𝚂𝚃𝙰𝚁𝙺 ✪", url="https://t.me/Movie_search_V4_bot"),
                        InlineKeyboardButton("⚡️ 𝚄𝙿𝙳𝙰𝚃𝙴", url="https://t.me/movie_a1"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙼𝚈 𝙰𝙻𝙻 𝙱𝙾𝚃𝚂 💢⭑", url="https://t.me/movie_a1/162")],
                    [InlineKeyboardButton("🦋 ⭑┗━━┫⦀⦙ 𝙼𝙳𝙸𝚂𝙺 𝙲𝙷𝙰𝙽𝙽𝙻𝚂 ⦙⦀┣━━┛⭑ 🦋", url="https://t.me/+gtlaKqnF9rVlMWRl")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    else:
        # logger.info(update) ==         
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.LAZY_START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🦋 ⭑┗━━┫⦀⦙ O W N E R ⦙⦀┣━━┛⭑ 🦋", url="https://t.me/R_KOHLI")],
                    [
                        InlineKeyboardButton("▍║▍▏║ UPDATE ║▍▏║▍", url="https://t.me/movie_a1"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙼𝚈 𝙰𝙻𝙻 𝙱𝙾𝚃𝚂 💢⭑", url="https://t.me/movie_a1/162")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
         
