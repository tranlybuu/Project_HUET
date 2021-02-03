#Project Web Crawler
#Trần Lý Bửu - K1 :)

# Đây là file nháp

import re
import os
from datetime import date, datetime
import requests
from bs4 import BeautifulSoup
import sys
import time


"""
txt = "The rain in Span"
x = re.search("^The.*Spain$", txt)
n=str(type(x))
print("--  " + n)
#<class 'NoneType'>
#<class 're.Match'>

x = re.search("^The.*Spain$", txt)
print(x.string)
"""

"""
arr = [1,2,3,4,5,6,7,8,9,0]
check = 5
arr_new = arr[:check]
print(arr_new)
array = [arr, arr_new]
print(array)
"""

"""
path = "C:\\CRAWLER"
os.chdir(path)
a = "1"
b = " test"
name = a + b
os.mkdir(name)
array = os.listdir(path)
count = len(array)
print(count)
for i in array:
    print(i)
    print(type(i))
"""

"""
a1 = "Hello"
f = open("test.txt",mode = 'w',encoding = 'utf-8')
f.write("Xin chào = ")
f.close()
"""

"""
now = datetime.now()            # \ Lấy dữ liệu thời gian hiện tại
time = now.strftime("%H:%M")    # / Định dạng về kiểu giờ:phút
today = date.today()                # \ Lấy dữ liệu ngày tháng năm
day = today.strftime("%d %B, %Y")   # / Định dạng về kiểu
print(time)
print(day)
"""

"""
name_folder = "Trang_web_đã_cào_dữ_liệu_thứ_31"
path = 'C:\\CRAWLER\\'
path = path + name_folder
os.chdir(path)
f = open("test.txt",mode = 'w',encoding = 'utf-8')
f.write("Xin chào = ")
f.close()
print(path)
"""

"""
path = 'C:\\CRAWLER\\'
os.chdir(path)
line_1 = "\t+------------------------------------------------------+\n"
line_2 = "\t|  Đây là file ghi lại lịch sử các url đã cào dữ liệu  |\n\t"
line_3 = "\t+------------------------------------------------------+\n\n"
line_4 = "Số thứ tự của đường link chính là số thứ tự của thư mục chứa nội dung đường dẫn đã cào\n"
line_5 = "Ví dụ đường dẫn có số thứ tự 1 thì thư mục chứ nội dung là Trang_web_đã_cào_dữ_liệu_thứ_1\n"
content = [line_1, line_2, line_3, line_4, line_5]
file = open("History.txt", "w+", encoding="utf-8")
for item in content:
    file.write(item)
file.close()

"""

"""
line_1 = "\t+-----------------------------------------------------+\n"
line_2 = "\t|  Đây là file ghi lại các url không thể cào dữ liệu  |\n\t"
line_3 = "\t+-----------------------------------------------------+\n\n"
line_4 = "Số thứ tự của đường link chính là số thứ tự của thư mục chứa nội dung đường dẫn đã cào\n"
line_5 = "<Ví dụ đường dẫn có số thứ tự 1 thì thư mục chứ nội dung là Trang_web_đã_cào_dữ_liệu_thứ_1>\n\n"
content = [line_1, line_2, line_3, line_4, line_5]
for i in content:
    print(i)
"""


"""
toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    # update the bar
    time.sleep(0.1)
    sys.stdout.write("=")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar
"""

a = False
if not a:
    print("F")
else:
    print("T")











