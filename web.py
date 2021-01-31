#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import requests
from bs4 import BeautifulSoup


#Các hàm cần thiết


def doc_noi_dung(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    return content


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
                    if (item.find("#", 0, 4)):
                        if (item.find("None", 0, 4)):
                            if len(item) > 2:
                                result.append(item)
        if not(item.find("http", 0, 4)):
            result.append(item)
    return result


def kiem_tra_link(link):
    if link[:4] == "http":
        return True
    else:
        return False

def chinh_sua_link(url,item):
    item = item.split(" ")
    url_new= str(url) + item[0]
    return url_new