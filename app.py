import pyautogui
import time
import datetime
import ftplib
import os
import random

time_sleep = random.randrange(15, 180, 2)

time.sleep(time_sleep)

cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
file_name = f"D:\\Programs\\autoscreenshot\\{cur_time}.jpg"
image = pyautogui.screenshot(file_name)


USER = ''
PASS = ''
HOST = ''
PORT = 21
ftp = ftplib.FTP(HOST)
ftp.login(USER, PASS)
ftp.cwd('screenshot')
upload_file = open(file_name, 'rb')
ftp.storbinary(f'STOR {cur_time}.jpg', upload_file)
upload_file.close()
ftp.quit()

os.remove(file_name)