# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

import pywhatkit as kit
import datetime
import time

# Replace these values with your own
phone_number = "+1234567890"  # Include the country code without '+' or '0'
message = "Hello, this is a test message!"

# Set the time to send the message (24-hour format)
hour = 12
minute = 0

# Get the current time
now = datetime.datetime.now()
current_hour = now.hour
current_minute = now.minute

# Calculate the delay in seconds until the specified time
delay_seconds = ((hour - current_hour) * 60 + (minute - current_minute)) * 60

# Wait until the specified time
if delay_seconds > 0:
    print(f"Waiting for {delay_seconds} seconds until {hour}:{minute}")
    time.sleep(delay_seconds)
    

# Send the WhatsApp message
kit.sendwhatmsg(phone_number, message, now.hour, now.minute + 1)  # Adding 1 minute to the current time

print("Message sent successfully!")