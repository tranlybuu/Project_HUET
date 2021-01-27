#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import  folder, web, function

def start(first_url, max_page):
    url_list = []
    url_list_const=10000
    error = []
    history=[]
    max_page = n
    count=0
    folder.kiem_tra("C:\\")
    data_folder = 'C:\\CRAWLER'
    url_list.append(str(first_url))

    #kịch bản các trang web
    while (count < max_page) and (len(url_list) > 0):
        if (count == 0) or (count % 5 == 0):
            function.lam_sach_va_tom_tat_lai(first_url, max_page, count)
        url_new = []
        url_new_const = 500
        url = url_list.pop(0)

        try:
            page = web.doc_noi_dung(url)
            links = web.lay_cac_duong_link(page)
            for item in links:
                if web.kiem_tra_link(item)==False:
                    item = web.chinh_sua_link(url,item)
                if (item not in url_list) and (item not in history) and (item not in url_new) and (item != url):
                    if len(url_new)>=url_new_const:
                        continue
                    else:
                        url_new.append(item)
            if (len(url_list) + len(url_new) <= url_list_const):
                url_list = url_list + url_new
            else:
                check = int(url_list_const - len(url_list))
                array =url_new[:check]
                url_list = url_list + array

            history.append(url)
            count += 1

            data_array = [page, url_new, url, url_new_const]
            name_folder = folder.tao_ten_folder_tu_dong(data_folder,url)
            folder.luu_file(data_array, name_folder)
            folder.luu_lich_su_cac_url(url)
            print("\tĐã duyệt " + str(count) + " url")
        except:
            print("\tCó đường dẫn bị lỗi ")
            error.append(url)
            folder.error_url(url)

    function.lam_sach_va_tom_tat_lai(first_url, max_page, count)

    if len(error) != 0:
        print("\tCó " + str(len(error)) +  " đường dẫn không lấy được dữ liệu:")
        for i in range(len(error)):
            print(str(i+1) + " - " + str(error[i]))
    else:
        print("\tKhông có đường dẫn nào bị lỗi")
    print("\n\t+-------------------------------------------+\n\t| Dữ liệu đã cào đã được lưu tại C:\\CRAWLER |\n\t+-------------------------------------------+\n\t")

if __name__ == '__main__':
    first_url = str(input("Nhập đường dẫn ban đầu bạn muốn cào dữ liệu: "))
    n = int(input("Bạn muốn cào tối đa bao nhiêu url: "))
    start(first_url, n)