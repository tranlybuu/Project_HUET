#Các thư viện cần dùng
import requests
from bs4 import BeautifulSoup


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
    a_tags = content.find_all("a")
    result = []
    for item in a_tags:
        link = item.get("href")
        result.append(link)
    return result

#Hàm kiểm tra tính hợp lệ của 1 đường link
#Kết quả trả về: True nếu hợp lệ / False nếu không hợp lệ
def kiem_tra_link(link):
    pass

#Hàm chỉnh sửa đường link nếu đường link không đầy đủ
#Kết quả trả về là 1 đường link đầy đủ
def chinh_sua_link(content):
    pass
