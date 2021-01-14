# Project_HUET
# Trần Lý Bửu

Web Crawler là phần mềm được thiết kế với mục đích có thể duyệt website trên mạng World Wide Web một cách có hệ thống.
=> Giúp thu thập thông tin của những trang web đó về cho công cụ tìm kiếm.
Việc này sẽ mang lại khả năng lưu chỉ mục các trang web đó vào bộ cơ sở dữ liệu của Search Engine. 
Đồng thời, giúp các công cụ tìm kiếm đó tìm ra những đánh giá chính xác nhất về website được thu thập dữ liệu.

Mô hình crawler bao gồm như sau:
B1: Chọn URL để khởi đầu
B2: Sử dụng HTML protocol để có thể lấy trang web
B3: Trích xuất ra các link và lưu trữ lại trong queue
B4: Lặp đi lặp lại nhiều lần các bước 2,3
