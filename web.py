#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import requests
from bs4 import BeautifulSoup


#Các hàm cần thiết

#Hàm này để lấy đoạn code HTML
#Kết quả trả về là kiểu dữ liệu văn bản chứa code HTML
def doc_noi_dung(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    return content

#Hàm này dùng để lọc ra các đường dẫn
#Kết quả trả về là list chứa các đường dẫn hợp lệ
def lay_cac_duong_link(content):
    url_list = []
    result = []
    raw = content.find_all("a")
    for item in raw:
        link = item.get("href")
        url_list.append(link)
    for item in url_list:
        item = str(item)
        # Lấy các đường dẫn đầy đủ
        if not(item.find("http", 0, 4)):
            result.append(item)
        # Lấy các đường dẫn còn thiếu http...
        if not (item.find("http", 0, 4)):   #Lấy các đường dẫn chưa có http
            if not (item.find("java", 0, 4)):   #Loại các phần tử Javascript
                    if not (item.find("#", 0, 4)):   #Loại các phần tử "#"
                        if not (item.find("None", 0, 4)):   #Loại các phần tử None
                            if len(item) > 2:
                                result.append(item)
    return result

#Hàm này dùng để chỉnh sửa đường dẫn
#Kết quả trả về là True nếu đường dẫn đầy đủ và False nếu đường dẫn chưa đầy đủ
def kiem_tra_link(link):
    if link[:4] == "http":
        return True
    else:
        return False


def chinh_sua_link(url,item):
    item = item.split(" ")
    url_new= str(url) + item[0]
    return url_new