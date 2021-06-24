import os
import datetime, sys

#print(os.getuid())
print(os.cpu_count())
#print(os.uname())
print(datetime.date.today())

import requests

requests_api = requests.get("https://www.bbc.co.uk/")

print(requests_api.status_code) #200 for success, 404 and above for failure
print(requests_api.headers)
print(requests_api.content)