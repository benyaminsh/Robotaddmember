from pyrogram import Client,filters
from pyrogram.raw import functions

bot = Client("my_account",api_hash="46ca33383a60eeaa827f1a83e981c1e01",api_id="19491381")


owner = 2041864184
@bot.on_message(filters.text)
def main(client,message):
    userText = message.text
    if "az" in userText and message.chat.id==owner:
        chat_id = message.chat.id
        try:
            text = str(userText).split(" ")
            az = str(text[1])
            be = str(text[3])

            try:
                bot.join_chat(az)
                bot.send_message(chat_id,f"Join To {az}")
            except:
                pass

            try:
                bot.join_chat(be)
                bot.send_message(chat_id, f"Join To {be}")
            except:
                pass

            userList = []
            for user in bot.iter_chat_members(az):
                userList.append(user.user.id)


            bot.send(functions.channels.InviteToChannel(channel= bot.resolve_peer(f"{be}"),users = [bot.resolve_peer(i) for i in userList]))
            bot.send_message(chat_id, 'Done ✅')
        except:
            bot.send_message(chat_id,'Error There is a problem ⛔️')

    elif userText == "bot" and message.chat.id==owner:
        bot.send_message(message.chat.id, 'Online ✅️')

    elif message.text == "id" and message.from_user.id == owner:
        bot.send_message(message.from_user.id,f"{message.chat.id}")








bot.run()