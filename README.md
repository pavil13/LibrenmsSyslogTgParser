# LibrenmsSyslogTgParser
## ENG
Collection and systematization of data, information about dates and the number of equipment turned up/down based on system logs in Telegram from the alert system in LibreNMS

For the program to work, before starting it is necessary to change the values of some variables in the **main.py** file:

**api_id** and **api_hash** - you can get these values in your personal account on the website [my.telegram.org](https://my.telegram.org)

**channel_id** - the value of this variable is equal to the unique identifier of the Telegram channel to which LibreNMS sends notifications.

When parsing data, notifications received from devices such as UPS, as well as notifications of the "Port utilisation" type are not processed.

When starting the program, the user is asked for data (day, month, year) by which filtering will be carried out. Data verification is not provided (no foolproof). Incorrect data will cause the program to crash.

## RUS
Сбор и систематизация данных, информации о датах и ​​количестве up/down оборудования на основе SysLogs в Telegram из системы оповещений в LibreNMS

Для работы программы, перед запуском необходимо изменить значения некоторых переменных в файле **main.py**: 

**api_id** и **api_hash** - эти значения вы можете получить в личном кабинете на сайте [my.telegram.org](https://my.telegram.org)

**channel_id**  - значение этой переменной равно уникальному идентификатору канала в Телеграмм, в который LibreNMS отправляет уведомления.

При парсинге данных не обрабатываются уведомления, полученные от устройств типа UPS, а также уведомления типа "Port utilisation"

При запуске программы у пользователя запрашиваются данные (день, месяц, год), по которым будет осуществляться фильтрация. Нет защиты от дурака. Неправильные данные приведут к сбою программы.
