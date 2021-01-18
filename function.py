#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import os

#Các hàm cần thiết

#Hàm này dùng để xóa sạch có dữ liệu đã được in ra trên màn hình
def lam_sach_man_hinh(url, count):
    os.system('cls')
    print("\tBạn muốn cào dữ liệu bắt đầu từ url:",url)
    print("\tTổng số trang bạn muốn cào là:",count)
    print("\t----------------------------")
    print("\tLoading...\n")