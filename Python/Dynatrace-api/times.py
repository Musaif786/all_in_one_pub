from datetime import datetime
from datetime import timedelta


time = datetime.now()
print(time)
#2023-12-07T03:20:00Z
time_format = time.strftime("%Y-%m-%dT%H:%M:%SZ")
print(time_format)