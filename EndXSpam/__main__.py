from pyrogram import Client, idle
from EndXSpam import BOT_TOKEN2, API_HASH, APP_ID, BOT_TOKEN1


if __name__ == "__main__" :
    plugins = dict(root="EndXSpam/plugins")
    end1 = Client(
        "Client1",
        bot_token=Config.BOT_TOKEN1,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    end2 = Client( # This is 2nd client. add much as you wish. but remember to edit starting process
        "Client2",
        bot_token=Config.BOT_TOKEN2,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    print("Waking Up Client 1")
    end1.start() # Starting Client 1
    print("Waking Up Client 2")
    end2.start() # Starting Client 2
    print("Everything Ok! Enjoy Multi Client! Lol!") # Remove this shit if you like lmao
    idle()
