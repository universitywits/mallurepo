#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, filters # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private & filters.joined, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            msg = await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = "<b>➠ᴏᴛᴛ ᴜᴘᴅᴀᴛᴇ : @Beast_tamil_movie_65\n\n➠Gʀᴏᴜᴘ : @Movie360group</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🌈ηεϖ ʍσѵίες🌈', url='http://t.me/joinchat/ME-pgJrySWg1ZDg1"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            msg = await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = "<b>➠ᴏᴛᴛ ᴜᴘᴅᴀᴛᴇ : @Beast_tamil_movie_65\n\n➠Gʀᴏᴜᴘ : @Movie360group</b>",
                parse_mode="html"
            )
            await msg.edit_caption(
                caption = f"<b>{msg.video.file_name}</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🌈ηεϖ ʍσѵίες🌈', url='http://t.me/joinchat/ME-pgJrySWg1ZDg1"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            msg = await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = '',
                parse_mode="html"
            )
            await msg.edit_caption(
                caption = f"<b>{msg.audio.file_name}</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '⭕ OUR CHANNEL LINKS ⭕', url="https://t.me/MalluMovies_Links"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('🌈Ɠɾσυρ🌈', url='https://t.me/movie360group'),
        InlineKeyboardButton('🌈Ƈԋαɳɳҽʅ🌈', url ='https://t.me/beast_tamil_movie_65')
    ],[
        InlineKeyboardButton('🌈360 հεʆԹ🌈', url='http://t.me/movies360help'),
        InlineKeyboardButton('🌈ηεϖ ʍσѵίες🌈', url='http://t.me/joinchat/ME-pgJrySWg1ZDg1')
    ],[

    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
    await db.add_user(update.from_user.id)


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🏘️ Home', callback_data='start'),
        InlineKeyboardButton('About 🛡️', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('🏘️ Home', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start_not_joined(bot, update):

    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    if file_uid:
        tryagain = f'https://t.me/{bot.username}?start={file_uid}'
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text = '♀️Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟ♀️',
                        url = bot.invitelink
                    )
                ],
                [
                    InlineKeyboardButton(
                        text = '🔥 Tʀʏ Aɢᴀɪɴ 🔥',
                        url = tryagain
                    )
                ]
            ]
        )
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FORCE_SUBTEXT.format(
                tryagain = tryagain,
                invitelink = bot.invitelink
            ),
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id,
            disable_web_page_preview=True
        )    
