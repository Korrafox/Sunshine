from yourghost_class import BotGhost
import requests
import datetime
greet_bot = BotGhost(token = "659194768:AAGtrFX0ldHml1UW48Swv0ZCdkzKwDzGuh4")
greetings = ('Hello','Hi','Greetings','Hello, Ghost','Hi, Ghost','Hello, ghost','Hi, ghost','Greetings, Ghost','Greetings, ghost','Regards','Regards, Ghost','Regards, ghost')
now = datetime.datetime.now()
def main():
    new_offset = None
    today = now.day
    hour = now.hour
    while True:
        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        if last_chat_text.lower() in greetings and today == now.day and 0 <= hour <6:
            greet_bot.send_message(last_chat_id,'Good night, Guardian, it is nice to see you,{}'.format(last_chat_name))
            today+=1
        elif last_chat_text.lower() in greetings and today == now.day and 6 <= hour <12:
            greet_bot.send_message(last_chat_id,'Good morning, Guardian, it is nice to see you,{}'.format(last_chat_name))
            today+=1
        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour <18:
            greet_bot.send_message(last_chat_id,'Good afternoon, Guardian, it is nice to see you,{}'.format(last_chat_name))
            today+=1
        elif last_chat_text.lower() in greetings and today == now.day and 18 <= hour <24:
            greet_bot.send_message(last_chat_id,'Good evening, Guardian, it is nice to see you,{}'.format(last_chat_name))
            today+=1
        new_offset = last_update_id+1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

             
