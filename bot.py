import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5966564904:AAG9sbcErdLRUMynBxdGAJLXAjzwPLuKc1I")

API_ID = int(os.environ.get("API_ID", "11319890"))

API_HASH = os.environ.get("API_HASH", "4965e574411647c42ffbd8b46040f0a5")

STRING = os.environ.get("STRING", "1BVtsOKMBu5D2LbgvFDQ8cAsSAqnCXB19-C5BCLdkt8YlfC1m_dN11Jenu7-kYhGkW3vivcy7UrR920m91PzDxlbCBvfcEDmpop1kydiEopFFCkemy7rOX2kNM1Sd219Y7hTepJt9IbS2VxYKvyQYZkGbr07NkGpuJTFVPPPpyDh4cmhJvEie0YY7GU78JjYgiKtmxVbV0_nKgTRCulR8mRzShEPo5YRlQ5OMeLxHK06oGw_RiBe9rDtvIfvf64iRBoDDcgzNS4QXGfhXAaUVlUIaWAAwqni4sZSBX2VvL8EgnNj4wTilEAwLtt_np4ZgqUvsvbyEXrNXFcTPdrtZT9ayQDpvDKc=")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
