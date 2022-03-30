import json
from datetime import datetime

import requests


my_json = requests.post(
    "http://econ.vsu.ru/js/schedule/callapi.php?url=schedule/000000008&data=groupID:000000000009410"
).text
ready_json = json.loads(my_json)


weeklist = []
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []

for element in ready_json:
    if element["НомерДня"] == 1:
        monday.append(element["НомерДня"])
        monday.append(element["ВременноеОкно"])
        monday.append(element["Дисциплина"])
        monday.append(element["Помещение"])
    if element["НомерДня"] == 2:
        tuesday.append(element["ВременноеОкно"])
        tuesday.append(element["Дисциплина"])
        tuesday.append(element["Помещение"])
    if element["НомерДня"] == 3:
        wednesday.append(element["ВременноеОкно"])
        wednesday.append(element["Дисциплина"])
        wednesday.append(element["Помещение"])
    if element["НомерДня"] == 4:
        thursday.append(element["ВременноеОкно"])
        thursday.append(element["Дисциплина"])
        thursday.append(element["Помещение"])
    if element["НомерДня"] == 5:
        friday.append(element["ВременноеОкно"])
        friday.append(element["Дисциплина"])
        friday.append(element["Помещение"])
    if element["НомерДня"] == 6:
        saturday.append(element["ВременноеОкно"])
        saturday.append(element["Дисциплина"])
        saturday.append(element["Помещение"])
weeklist.append(monday)
weeklist.append(tuesday)
weeklist.append(wednesday)
weeklist.append(thursday)
weeklist.append(friday)
weeklist.append(saturday)


def ScheduleToday():
    while True:
        if datetime.today().strftime("%A") == "Monday":
            return(" \n ".join(weeklist[0]))
        if datetime.today().strftime("%A") == "Tuesday":
            return(" \n ".join(weeklist[1]))
        if datetime.today().strftime("%A") == "Wednesday":
            return(" \n ".join(weeklist[2]))
        if datetime.today().strftime("%A") == "Thursday":
            return(" \n ".join(weeklist[3]))
        if datetime.today().strftime("%A") == "Friday":
            return(" \n ".join(weeklist[4]))
        if datetime.today().strftime("%A") == "Saturday":
            return(" \n ".join(weeklist[5]))
