# AnonFiles Direct Download and Link Generator
Script Python đơn giản để lấy liên kết tải trực tiếp từ host AnonFiles và tự động tải chúng về
## Hướng dẫn sử dụng
Các bạn tạo một file tên link.txt đặt cùng thư mục với file main.py
Đặt các link bạn cần tải vào file link.txt, mỗi link một dòng.
Lưu lại và chạy lệnh 
```bash
python3 main.py
```
Script sẽ tự lấy link và tải tuần tự từng file một cho đến khi hết danh sách link cần tải trong file link.txt thì thôi

Nếu bạn chưa có module bs4 thì chạy lệnh sau để cài

```bash 
pip install bs4

```
hoặc 
```bash
pip3 install bs4 --user 
```

Nếu bạn muốn lấy link direct hàng loạt thì tham khảo file main_old

Chúc vui vẻ :)
