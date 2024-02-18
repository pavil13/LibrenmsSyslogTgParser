from pyrogram import Client

message_len = 500 # max message value
telegram_chat_id = -1001487535356 # insert Telegram Chat id value 

api_id = 1234567 # insert you api_id value 
api_hash = "api_hash" # insert you api_hash value 

def counter_message():
    with Client("my_account", api_id, api_hash) as app:

        date_message_dict = {}
        messages_list = app.get_chat_history(telegram_chat_id, message_len)
        messages_list2 = app.get_chat_history(telegram_chat_id, message_len)

        for message in messages_list:   
            msg_date = message.date.strftime("%d-%m-%Y")
            date_message_dict[msg_date] = 0

        for message2 in messages_list2:
            for key_date in date_message_dict:
                if message2.date.strftime("%d-%m-%Y") == key_date:
                    date_message_dict[key_date] += 1

        for key in date_message_dict:
            print(f'{key} : {date_message_dict[key]}')

def counter_down_name():
    with Client("my_account",api_id, api_hash) as app:

        down_device_dict = {}
        messages_list = app.get_chat_history(telegram_chat_id, message_len)
        messages_list2 = app.get_chat_history(telegram_chat_id, message_len)


        for message in messages_list:  
            if "Alert for device" in message.text:

                down_device_name = message.text.split("Alert for device ", 1)[1].split(" - Devices")[0]
                down_device_dict[down_device_name] = 0

        for message2 in messages_list2:
            for device in down_device_dict:
                try:
                    down_device_name = message2.text.split("Alert for device ", 1)[1].split(" - Devices")[0]
                except IndexError as err:
                    pass
                if down_device_name == device:
                    down_device_dict[device] += 1

        for key in down_device_dict:
            print(f'{key} : {down_device_dict[key]}')

counter_message()
counter_down_name()