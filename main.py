#Các thư viện cần dùng
import folder, web

def start():
    url_list = ['https://codelearn.io/']  #Chứa các đường link chưa duyệt
    history=[]  #Chứa các đường link đã duyệt
    max_page=100    #Quy định số lượng trang web được tải về
    count=0     #Đếm số lượng trang web đã tải
    data_folder = 'C:\\Users\\DELL\\Downloads\\CRAWLER'

    #kịch bản các trang web
    while (count < max_page) and (len(url_list) > 0):
        url = url_list.pop(0)
        page = web.doc_noi_dung(url)
        links = web.lay_cac_duong_link(page)
        for item in links:  #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if web.kiem_tra_link(item)==False:
                item = web.chinh_sua_link(url,item)     #Chỉnh sửa nếu thiếu phần http://...
            if (item not in url_list) and (item not in history):    #Nếu đường link chưa được duyệt vào hàng đợi và chưa có trong lịch sử
                url_list.append(item)       #Thêm link mới vào danh sách chờ duyệt

        folder.luu_file(page, data_folder)
        history.append(url)
        count += 1

    #TEST CODE
    for i in history:
        print("Đã duyệt  -- ",i)
    print("================")
    print("Số lượng url đã duyệt:",count)
    print("Số lượng url chưa duyệt:", len(url_list))
    print("================")
    print("{} url đang ở hàng chờ".format(count//2))
    for i in range(count//2):
        print("Chưa duyệt  -- ",url_list[i])


if __name__ == '__main__':
    start()
