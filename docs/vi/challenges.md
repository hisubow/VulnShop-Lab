# Challenge Mode - Tiếng Việt

Challenge Mode giúp người học chủ động thực hành thay vì chỉ đọc lời giải. Dùng trang `/scoreboard` để theo dõi tiến độ trong phiên lab local.

## C01 - Thiếu kiểm tra quyền Admin

**Mục tiêu:** Kiểm tra user thường có truy cập được trang admin hay không.

Gợi ý:

1. Đăng nhập bản vulnerable bằng `alice / alice123`.
2. Truy cập `/admin`.
3. Ghi lại kết quả.
4. Lặp lại thao tác trên bản secure.

Quan sát mong đợi:

- Bản vulnerable cho user thường truy cập chức năng admin.
- Bản secure trả về `403 Forbidden`.

## C02 - SQL Injection ở Login

**Mục tiêu:** So sánh cách tạo SQL query không an toàn với cách xử lý login bằng parameterized query.

Gợi ý:

1. Mở `vulnerable-app/app.py` và tìm query login.
2. So sánh với `secure-app/app.py`.
3. Dùng behavioral tests làm bằng chứng rằng hai bản có hành vi khác nhau.

## C03 - Xử lý input ở Search

**Mục tiêu:** Quan sát ô search xử lý input người dùng như thế nào.

Gợi ý:

1. Search bằng từ khóa sản phẩm bình thường.
2. Thử input đặc biệt trong môi trường lab local.
3. So sánh hành vi giữa bản vulnerable và secure.

Ghi chú học tập:

- Khi input được render trong text node, output không an toàn có thể dẫn tới reflected XSS.
- Khi input được render trong HTML attribute như `value="..."`, output không an toàn có thể thành attribute injection.
- Context rất quan trọng: cách sửa đúng là escape theo ngữ cảnh và không dùng `safe` cho input người dùng.

## C04 - Profile IDOR

**Mục tiêu:** Kiểm tra user có xem được profile của user khác không.

Gợi ý:

1. Đăng nhập bằng `alice`.
2. Mở `/profile`.
3. Thử thay đổi query parameter `id`.
4. So sánh với bản secure.

## C05 - CSRF Settings Update

**Mục tiêu:** Hiểu vì sao request thay đổi trạng thái cần CSRF protection.

Gợi ý:

1. Đăng nhập bằng `alice`.
2. Mở `/settings` ở cả hai app.
3. So sánh form markup và logic phía server.
4. Quan sát bản secure yêu cầu CSRF token trước khi cập nhật email.

## C06 - Evidence Report

**Mục tiêu:** Sinh báo cáo Markdown từ structured evidence.

Gợi ý:

1. Mở một file trong `examples/`.
2. Chạy report generator.
3. So sánh report được sinh ra với `reports/sample-pentest-report.md`.
