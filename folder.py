#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import os
from datetime import date, datetime

#Các hàm cần thiết


def kiem_tra(path):
    os.chdir(path)
    check = os.listdir(path)
    if 'CRAWLER' not in check:
        os.mkdir('CRAWLER')
    path = 'C:\\CRAWLER\\'
    os.chdir(path)
    check = os.listdir(path)
    if 'History.txt' not in check:
        line_1 = "\t+------------------------------------------------------+\n"
        line_2 = "\t|  Đây là file ghi lại lịch sử các url đã cào dữ liệu  |\n"
        line_3 = "\t+------------------------------------------------------+\n\n"
        line_4 = "Số thứ tự của đường link chính là số thứ tự của thư mục chứa nội dung đường dẫn đã cào\n"
        line_5 = "<Ví dụ đường dẫn có số thứ tự 1 thì thư mục chứ nội dung là Trang_web_đã_cào_dữ_liệu_thứ_1>\n\n"
        content = [line_1, line_2, line_3, line_4, line_5]
        file = open("History.txt", "w", encoding="utf-8")
        for item in content:
            file.write(item)
        file.close()
    if 'Error.txt' not in check:
        line_1 = "\t+-----------------------------------------------------+\n"
        line_2 = "\t|  Đây là file ghi lại các url không thể cào dữ liệu  |\n"
        line_3 = "\t+-----------------------------------------------------+\n\n"
        content = [line_1, line_2, line_3]
        file = open("Error.txt", "w", encoding="utf-8")
        for item in content:
            file.write(item)
        file.close()


def tao_ten_folder_tu_dong(path, url):
    os.chdir(path)
    const = "Trang_web_đã_cào_dữ_liệu_thứ_"
    count = len(os.listdir(path)) - 1
    name_folder = const + str(count)
    os.mkdir(name_folder)
    return name_folder


def luu_file(data, name_folder):
    path = "C:\\CRAWLER\\"
    os.chdir(path + str(name_folder))
    now = datetime.now()
    time = now.strftime("%H:%M")
    today = date.today()
    day = today.strftime("%d %B, %Y")
    line_info_1 = "\tĐây là thông tin về đường dẫn vừa cào được"
    line_info_2 = "\n\t------------------------------------------\n"
    line_info_3 = "\tURL: " + str(data[2]) + "\n"
    line_info_4 = "\tNgày: " + str(day) + "\n"
    line_info_5 = "\tThời gian: " + str(time) + "\n"
    info = [line_info_1,line_info_2,line_info_3,line_info_4,line_info_5]
    file = open("1 - Thông tin url đã cào.txt", "w+", encoding="utf-8")
    for item in info:
        file.write(item)
    file.close()
    line_content_1 = "\tĐây là file code HTML vừa cào được"
    line_content_2 = "\n\t------------------------------------------\n\n"
    line_content_3 = str(data[0])
    url = [line_content_1, line_content_2, line_content_3]
    file = open("2 - File HTML.txt", "w+", encoding="utf-8")
    for item in url:
        file.write(item)
    file.close()
    line_url_1 = "\tĐây là những url mới được tìm thấy trong url này"
    line_url_2 = "\n\t------------------------------------------\n\n"
    line_url_3 = ""
    line_url_4 = data[1]
    max_url = data[3]
    if len(line_url_4) == max_url:
        line_url_3 = "Đã tìm thấy nhiều hơn " + str(max_url) + " url mới:\n"
    else:
        line_url_3 = "Đã tìm thấy " + str(len(line_url_4)) + " url mới:\n"
    url = [line_url_1, line_url_2, line_url_3]
    file = open("3 - Những url mới được tìm thấy.txt", "w+", encoding="utf-8")
    for item in url:
        file.write(item)
    for item in range(len(line_url_4)):
        add_url = str(item + 1) + " - " + str(line_url_4[item]) + "\n"
        file.write(str(add_url))
    file.close()

def luu_lich_su_cac_url(url):
    path = "C:\\CRAWLER\\"
    os.chdir(path)
    file = open("History.txt", mode='r+', encoding='utf-8')
    STT = len(file.readlines()) - 6
    file.close()
    file = open("History.txt", mode='a+', encoding='utf-8')
    content = str(STT) + " -- " + str(url) + "\n"
    file.write(content)
    file.close()

def error_url(url):
    path = "C:\\CRAWLER\\"
    os.chdir(path)
    file = open("Error.txt", mode='r+', encoding='utf-8')
    STT = len(file.readlines()) - 3
    file.close()
    file = open("Error.txt", mode='a+', encoding='utf-8')
    content = str(STT) + " -- " + str(url) + "\n"
    file.write(content)
    file.close()
