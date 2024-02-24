import datetime

your_today = datetime.datetime.now()

tomorrow = your_today + datetime.timedelta(days=1)

yesterday = your_today - datetime.timedelta(days=1)

print("Yesterday: ", yesterday, "Today: ", your_today, "Tomorrow: ", tomorrow) 
