import datetime
from pyrogram import Client

api_id = 1212121  # insert you api_id value 
api_hash = "api_hash" # insert you api_hash value 
channel_id = -12121212121 # insert you Telegram channel_id value 


def main():
    with Client("my_account", api_id, api_hash) as app:

        message_parse_quant = int(input('Введите количство сообщений, которые будут обработаны: '))
    
        day = input('Введите день (int, ex - 01): ')
        month = input('Введите месяц (int, ex - 10): ')
        year = input('Введите год (int, ex - 2024): ') 

        required_date = f'{day}-{month}-{year}'

        required_date_dict = {}
        messages_list = list()
        messages_dict = {}
        device_down_dict = {}


        #заполнение массивов 
        for msg in app.get_chat_history(channel_id, message_parse_quant):
            messages_list.append(msg)
            messages_dict[msg.date.strftime('%d-%m-%Y')] = 0

            if "Alert for device " in msg.text and "UPS" not in msg.text and "Port utilisation" not in msg.text:
                device_name = msg.text.split("Alert for device ", 1)[1].split(" - Devices")[0]
                device_down_dict[device_name] = 0

            if msg.date.strftime('%d-%m-%Y') == required_date:
                if "Alert for device " in msg.text and "UPS" not in msg.text and "Port utilisation" not in msg.text:
                    device_name = msg.text.split("Alert for device ", 1)[1].split(" - Devices")[0]
                    required_date_dict[device_name] = 0

        #перебор массивов, поиск данных и заполнение счетчиков
        for message in messages_list:

            if message.date.strftime('%d-%m-%Y') in messages_dict:
                messages_dict[message.date.strftime('%d-%m-%Y')] += 1

            if "Alert for device " in message.text and "UPS" not in message.text and "Port utilisation" not in message.text:
                device_name = message.text.split("Alert for device ", 1)[1].split(" - Devices")[0]

                if message.text.split("Alert for device ", 1)[1].split(" - Devices")[0] == device_name:
                    device_down_dict[device_name] += 1

            if message.date.strftime('%d-%m-%Y') == required_date:
                if "Alert for device " in message.text and "UPS" not in message.text and "Port utilisation" not in message.text:
                    device_name = message.text.split("Alert for device ", 1)[1].split(" - Devices")[0]
                    required_date_dict[device_name] += 1

        #вывод данных 
        print(f"\nДата/общее количество сообщений (из последних {message_parse_quant}):")
        for date in messages_dict:
            print(f'{date}: {messages_dict[date]}')

        print(f"\nНазвание/количество падений за последние {message_parse_quant} сообщений в дату - {required_date}:")
        counter = 0
        for device_name in required_date_dict:
            print(f'{device_name}: {required_date_dict[device_name]}')
            counter += required_date_dict[device_name]
        print(f"\nОбщее кол-во: {counter}")

        print(f"\nНазвание/количество падений за последние {message_parse_quant} сообщений:")
        for device in device_down_dict:
            print(f'{device}: {device_down_dict[device]}')



if __name__ == "__main__":
    main()
