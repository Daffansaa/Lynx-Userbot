

import asyncio
import os
from faker import Faker
import datetime
from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from userbot.utils import edit_or_reply
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.gencc(?: |$)(.*)")
async def _(lynxevent):
    if hellevent.fwd_from:
        return
    lynxcc = Faker()
    lynxname = lynxcc.name()
    lynxadre = lynxcc.address()
    lynxcard = lynxcc.credit_card_full()
    
    await edit_or_reply(lynxevent, f"__**👤 NAME :- **__\n`{lynxname}`\n\n__**🏡 ADDRESS :- **__\n`{lynxadre}`\n\n__**💸 CARD :- **__\n`{lynxcard}`")
    

@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1448477501))
              await event.client.send_message(chat, f"/bin {lynx_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.vbv(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1448477501))
              await event.client.send_message(chat, f"/vbv {lynx_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
    
    
@register(outgoing=True, pattern=r"^\.key(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1448477501))
              await event.client.send_message(chat, f"/key {lynx_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
 
  
@register(outgoing=True, pattern=r"^\.iban(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1448477501))
              await event.client.send_message(chat, f"/iban {lynx_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

    
@register(outgoing=True, pattern=r"^\.ccheck(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1448477501))
              await event.client.send_message(chat, f"/ss {lynx_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
             
             
@register(outgoing=True, pattern=r"^\.ccbin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    lynx_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{lynx_input}`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1448477501))
              await event.client.send_message(chat, f"/gen {lynx_input}")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Please Unblock @carol5_bot")
              return
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

    
CMD_HELP.update:({
    "ccarder": "\
    ⚡𝘾𝙈𝘿⚡: `.gencc`\
   \n↳ : Generates Fake CC.\
\n\n⚡𝘾𝙈𝘿⚡: `.ccheck` <query>\
   \n↳ : Checks That The Given CC is Live or Not.\
\n\n⚡𝘾𝙈𝘿⚡: `.iban` <query>\
   \n↳ : Checks That The Given IBAN ID is Live or Not.\
\n\n⚡𝘾𝙈𝘿⚡: `.key` <query>\
   \n↳ : Checks the status of probided key.\
\n\n⚡𝘾𝙈𝘿⚡: `.vbv` <query>\
   \n↳ : Checks the vbv status of given card.\
\n\n⚡𝘾𝙈𝘿⚡: `.bin` <query>\ 
   \n↳ : Checks that the given bin is valid or not.\
\n\n⚡𝘾𝙈𝘿⚡: `.ccbin` <bin>\
   \n↳ : Generates CC from the given bin."
})
