from pyrogram import Client, filters

bot_token = "6667859840:AAGRhtQ2KeQyQTuVxSHXWysd9noywr85GU0"

api_id = 20619105
api_hash = "4124fe31fea2535a682f0e174f3137c8"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()
