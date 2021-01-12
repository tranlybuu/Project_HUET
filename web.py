#Các thư viện cần dùng
import requests
from bs4 import BeautifulSoup
import re


#Các hàm cần thiết

#Hàm đọc nội dung trang web chỉ định
#Kết quả trả về là 1 văn bản dạng chuỗi
def doc_noi_dung(url):
    #Gửi yêu cầu truy cập url
    page = requests.get(url)
    #Lấy code html của trang web được trả về theo url
    content = BeautifulSoup(page.content, 'html.parser')
    return content

#Hàm lấy các đường link web trong nội dung đọc về
#Kết quả trả về là 1 list chứa các đường link
def lay_cac_duong_link(content):
    url_list = []
    result = []
    raw = content.find_all("a")
    for item in raw:
        link = item.get("href")
        url_list.append(link)
    for item in url_list:
        item = str(item)
        if (item.find("http", 0, 4)):
            if (item.find("java", 0, 4)):
                if item.find("html", (len(item) - 4), len(item)):
                    if (item.find("#", 0, 4)):
                        if (item.find("None", 0, 4)):
                            if len(item) > 2:
                                result.append(item)
        if not(item.find("http", 0, 4)):
            result.append(item)
    return result


#Hàm kiểm tra tính hợp lệ của 1 đường link
#Kết quả trả về: True nếu hợp lệ / False nếu không hợp lệ
def kiem_tra_link(link):
    check = re.search("^http", link)
    try:
        if link == check.string:
            return True
    except:
        return False


#Hàm chỉnh sửa đường link nếu đường link không đầy đủ
#Kết quả trả về là 1 đường link đầy đủ
def chinh_sua_link(url,item):
    item = item.split(" ")      #Loại bỏ khoảng trống 2 đầu chuỗi
    url_new= str(url) + item[0]
    return url_new