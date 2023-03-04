import requests
import json
import datetime

url = "http://localhost:6969/availabilities"

# data = {
#     'startTime': datetime.datetime(2023, 2, 24, 10, 30, 0).strftime("%Y-%m-%d %H:%M:%S"),
#     'endTime': datetime.datetime(2023, 2, 24, 11, 30 , 0).strftime("%Y-%m-%d %H:%M:%S")
# }
#
# headers = {
#     'Content-Type': 'application/json'
# }

r = requests.get(url)

print(r.text)