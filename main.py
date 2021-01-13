#Project Web Crawler
#Trần Lý Bửu - K1

#Các thư viện cần dùng
import  folder, web

def start():
    url_list = ['https://vietnamnet.vn/']  #Chứa các đường link chưa duyệt
    url_list_const=10000        #Số lượng tối đa mà danh sách chờ duyệt có thể chứa
    history=[]  #Chứa các đường link đã duyệt
    max_page=10    #Quy định số lượng trang web được tải về
    count=0     #Đếm số lượng trang web đã tải
    data_folder = 'C:\\CRAWLER'     #Lưu vào ổ C thư mục CRAWLER

    #kịch bản các trang web
    while (count < max_page) and (len(url_list) > 0):
        url_new = []  # Chứa các đường link mới được tìm thấy
        url_new_const = 300  #Số lượng tối đa mà danh sách các đường dẫn mới tìm thấy có thể chứa
        url = url_list.pop(0)   #Lấy đường dẫn đầu tiên trong danh sách chưa duyệt
        page = web.doc_noi_dung(url)
        links = web.lay_cac_duong_link(page)
        for item in links:     #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web.kiem_tra_link(item)==False:
                item = web.chinh_sua_link(url,item)     #Chỉnh sửa nếu thiếu phần http://...
            if (item not in url_list) and (item not in history) and (item not in url_new):  #   <==\
            #Nếu đường link chưa được duyệt vào hàng đợi, chưa có trong lịch sử                   //
            #và chưa được tìm thấy trong danh sách các đường dẫn mới được tìm thấy      =========//
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
        data_array = [page, url_new]
        #Bao gồm:
        # 1. Danh sách chờ duyệt
        # 2. Danh sách mới tìm thấy
        folder.tao_ten_folder_tu_dong(url)
        folder.luu_file(data_folder, data_array)


    #TEST CODE
    """
    for i in history:
        print("Đã duyệt  -- ",i)
    print("================")
    print("Số lượng url đã duyệt:",count)
    print("Số lượng url chưa duyệt:", len(url_list))
    print("================")
    """
    print("--  Code không có lỗi  --")


if __name__ == '__main__':
    start()
