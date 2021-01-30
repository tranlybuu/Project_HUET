#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import os
from datetime import date, datetime

#Các hàm cần thiết

#Hàm này kiểm tra và tạo thư mục CRAWLER
#path: đường dẫn đến ổ C:\
def kiem_tra(path):
    os.chdir(path)  #Di chuển đến thư mục trong đường dẫn path
    check = os.listdir(path)    #List các thư mục hiện có ở ổ C:\
    if 'CRAWLER' not in check:      #Nếu chưa có thư mục CRAWLER thì tạo thư mục CRAWLER
        os.mkdir('CRAWLER')

    #Tạo file History.txt
    path = 'C:\\CRAWLER\\'
    os.chdir(path)  # Di chuển đến thư mục trong đường dẫn path
    check = os.listdir(path)  # List các thư mục hiện có ở ổ C:\CRAWLER

    # Nếu chưa có file History.txt thì tạo thư mục trong CRAWLER
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

    # Nếu chưa có file Error.txt thì tạo thư mục trong CRAWLER
    if 'Error.txt' not in check:
        line_1 = "\t+-----------------------------------------------------+\n"
        line_2 = "\t|  Đây là file ghi lại các url không thể cào dữ liệu  |\n"
        line_3 = "\t+-----------------------------------------------------+\n\n"
        content = [line_1, line_2, line_3]
        file = open("Error.txt", "w", encoding="utf-8")
        for item in content:
            file.write(item)
        file.close()


#Hàm tạo tên folder tự động <Trang web đã cào dữ liệu thứ + số_thứ_tự>
#Kết quả trả về là tên của thư mục
#Số thứ tự: Đếm số lượng folder trong folder CRAWLER rồi tạo folder với số thứ tự tiếp theo
#path: đường dẫn để tạo và lưu nội dung
def tao_ten_folder_tu_dong(path, url):
    os.chdir(path)      #Di chuển đến thư mục trong đường dẫn path
    const = "Trang_web_đã_cào_dữ_liệu_thứ_"
    count = len(os.listdir(path)) - 1       #Đếm số file và folder hiện có trong thư mục
    name_folder = const + str(count)     #Trang web đã cào dữ liệu thứ + số_thứ_tự
    os.mkdir(name_folder)   #Tạo thư mục
    return name_folder

#Hàm lưu file vào thư mục tự động
# Biến data là 1 list bao gồm:
# 1. Nội dung HTML
# 2. Danh sách mới tìm thấy
# 3. Đường dẫn gốc
# 4. #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
#Kết quả trả về là 3 file txt bao gồm:
# -- Thông_tin_url_đã_cào.txt
# -- Nội_dung.txt
# -- Các_url_mới_tìm_được.txt
def luu_file(data, name_folder):
    path = "C:\\CRAWLER\\"
    os.chdir(path + str(name_folder))    #Di chuyển đến thư mục vừa được tạo tự động
    now = datetime.now()            # \ Lấy dữ liệu thời gian hiện tại
    time = now.strftime("%H:%M")    # / Định dạng về kiểu giờ:phút
    today = date.today()                # \ Lấy dữ liệu ngày tháng năm
    day = today.strftime("%d %B, %Y")   # / Định dạng về kiểu ngày:tháng:năm

    # -- Thông_tin_url_đã_cào.txt
    line_info_1 = "\tĐây là thông tin về đường dẫn vừa cào được"
    line_info_2 = "\n\t------------------------------------------\n"
    line_info_3 = "\tURL: " + str(data[2]) + "\n"
    line_info_4 = "\tNgày: " + str(day) + "\n"
    line_info_5 = "\tThời gian: " + str(time) + "\n"
    # Ghi nội dung vào file txt
    info = [line_info_1,line_info_2,line_info_3,line_info_4,line_info_5]
    file = open("1 - Thông tin url đã cào.txt", "w+", encoding="utf-8")
    for item in info:
        file.write(item)
    file.close()

    # -- Nội_dung.txt
    line_content_1 = "\tĐây là file code HTML vừa cào được"
    line_content_2 = "\n\t------------------------------------------\n\n"
    line_content_3 = str(data[0])
    # Ghi nội dung vào file txt
    url = [line_content_1, line_content_2, line_content_3]
    file = open("2 - File HTML.txt", "w+", encoding="utf-8")
    for item in url:
        file.write(item)
    file.close()

    # -- Các_url_mới_tìm_được.txt
    line_url_1 = "\tĐây là những url mới được tìm thấy trong url này"
    line_url_2 = "\n\t------------------------------------------\n\n"
    line_url_3 = ""
    line_url_4 = data[1]
    #Nội dung của line_url_3
    max_url = data[3]      #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
    if len(line_url_4) == max_url:
        line_url_3 = "Đã tìm thấy nhiều hơn " + str(max_url) + " url mới:\n"
    else:
        line_url_3 = "Đã tìm thấy " + str(len(line_url_4)) + " url mới:\n"
    #Ghi nội dung vào file txt
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

    # Lấy số thứ tự
    file = open("History.txt", mode='r+', encoding='utf-8')
    STT = len(file.readlines()) - 6
    file.close()

    # Ghi thêm đường dẫn vừa được duyệt vào lịch sử
    file = open("History.txt", mode='a+', encoding='utf-8')
    content = str(STT) + " -- " + str(url) + "\n"
    file.write(content)
    file.close()

def error_url(url):
    path = "C:\\CRAWLER\\"
    os.chdir(path)  # Di chuyển đến thư mục vừa được tạo tự động

    # Lấy số thứ tự
    file = open("Error.txt", mode='r+', encoding='utf-8')
    STT = len(file.readlines()) - 3
    file.close()

    # Ghi thêm đường dẫn bị lỗi
    file = open("Error.txt", mode='a+', encoding='utf-8')
    content = str(STT) + " -- " + str(url) + "\n"
    file.write(content)
    file.close()
