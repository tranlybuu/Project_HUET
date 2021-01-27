#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import os

#Các hàm cần thiết

def lam_sach_va_tom_tat_lai(url, max_page, count):
    os.system('cls')
    print("\n\tBạn muốn cào dữ liệu bắt đầu từ url:",url)
    print("\tTổng số trang bạn muốn cào là:", max_page)
    print("\t----------------------------")
    print("\tĐã thực hiện được {}% \n".format(round((count / max_page) *100)))