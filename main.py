#Project Web Crawler
#Trần Lý Bửu - K1 :)

#Các thư viện cần dùng
import  folder, web, function

def start(first_url, max_page):
    url_list = []  #Chứa các đường link chưa duyệt
    url_list_const=10000        #Số lượng tối đa mà danh sách chờ duyệt có thể chứa
    error = []  # Những đường dẫn không thể cào dữ liệu
    history=[]  #Chứa các đường link đã duyệt
    max_page = n    #Quy định số lượng trang web được tải về
    count=0     #Đếm số lượng trang web đã tải
    folder.kiem_tra("C:\\")    #Kiểm tra và tạo thư mục CRAWLER để lưu trữ
    data_folder = 'C:\\CRAWLER'     #Lưu vào ổ C thư mục CRAWLER

    url_list.append(str(first_url))

    #kịch bản các trang web
    while (count < max_page) and (len(url_list) > 0):
        if (count == 0) or (count % 20 == 0):
            function.lam_sach_man_hinh(first_url, max_page)
        url_new = []  # Chứa các đường link mới được tìm thấy
        url_new_const = 500  #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
        url = url_list.pop(0)   #Lấy đường dẫn đầu tiên trong danh sách chưa duyệt

        try:
            page = web.doc_noi_dung(url)
            links = web.lay_cac_duong_link(page)
            for item in links:     #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
                if web.kiem_tra_link(item)==False:
                    item = web.chinh_sua_link(url,item)     #Chỉnh sửa nếu thiếu phần http://...
                if (item not in url_list) and (item not in history) and (item not in url_new) and (item != url):   #  <=======\\
                #Nếu đường link chưa được duyệt vào hàng đợi, chưa có trong lịch sử, khác đường dẫn đang duyệt                //
                #và chưa được tìm thấy trong danh sách các đường dẫn mới được tìm thấy              [========================//
                    if len(url_new)>=url_new_const:     #Nếu danh sách các đường link vừa tìm thấy lớn hơn thì không thêm vào nữa
                        continue
                    else:
                        url_new.append(item)       #Thêm link mới vào danh sách chờ duyệt
            if (len(url_list) + len(url_new) <= url_list_const):    #Chuyển các đường dẫn mới tìm thấy vào danh sách chờ duyệt
                url_list = url_list + url_new
            else:
                check = int(url_list_const - len(url_list))      #Tính số lượng đường dẫn có thể thêm vào danh sách chờ duyệt
                array =url_new[:check]
                url_list = url_list + array

            history.append(url)        #Lưu url vừa duyệt vào lịch sử
            count += 1             #Đếm số url đã duyệt

            # Lưu lại dữ liệu vừa cào được vào thư mục
            data_array = [page, url_new, url, url_new_const]
            #Bao gồm:
            # 1. Nội dung HTML
            # 2. Danh sách mới tìm thấy
            # 3. Đường dẫn gốc
            # 4. #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
            name_folder = folder.tao_ten_folder_tu_dong(data_folder,url)    #Tạo thư mục tự động và kết quả trả về là tên thư mục vừa tạo
            folder.luu_file(data_array, name_folder)
            folder.luu_lich_su_cac_url(url)
            print("Đã duyệt " + str(count) + " url")
        except:
            print(" Có đường dẫn bị lỗi ")
            error.append(url)
            folder.error_url(url)

    #Thông báo
    if len(error) != 0:
        print("\n\tCó " + str(len(error)) +  " đường dẫn không lấy được dữ liệu:")
        for i in range(len(error)):
            print(str(i+1) + " - " + str(error[i]))
    else:
        print("\n\tKhông có đường dẫn nào bị lỗi")
    print("\n\t+--------------------------------------------+\n\t| Dữ liệu đã cào đã được lưu tại C:\\CRAWLER |\n\t+--------------------------------------------+\n\t")

if __name__ == '__main__':
    first_url = str(input("Nhập đường dẫn ban đầu bạn muốn cào dữ liệu: "))
    n = int(input("Bạn muốn cào tối đa bao nhiêu url: "))
    start(first_url, n)