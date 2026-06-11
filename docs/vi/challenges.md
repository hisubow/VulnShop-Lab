# Challenge Mode - Tiếng Việt

Mục tiêu của Challenge Mode là giúp người học tự thao tác thay vì chỉ đọc đáp án.

## C01 - Missing Admin Authorization

**Mục tiêu:** Kiểm tra user thường có truy cập được trang admin hay không.

Gợi ý:

1. Login vào vulnerable app bằng `alice / alice123`.
2. Truy cập `/admin`.
3. Ghi lại kết quả.
4. Thử lại trên secure app.

Kết quả cần quan sát:

- Vulnerable app cho user thường vào admin.
- Secure app trả về `403 Forbidden`.

## C02 - Profile IDOR

**Mục tiêu:** Kiểm tra user có xem được profile của user khác không.

Gợi ý:

1. Login bằng `alice`.
2. Mở `/profile`.
3. Thử thay đổi query `id` trên URL.
4. So sánh với secure app.

## C03 - Search Input Handling

**Mục tiêu:** Quan sát cách ô search xử lý input người dùng.

Gợi ý:

1. Nhập từ khóa bình thường.
2. Thử input đặc biệt trong môi trường local lab.
3. So sánh cách vulnerable app và secure app trả kết quả.

## C04 - Feedback Rendering

**Mục tiêu:** Kiểm tra dữ liệu feedback được lưu và hiển thị lại như thế nào.

Gợi ý:

1. Gửi một feedback bình thường.
2. Gửi một feedback có ký tự HTML đơn giản.
3. So sánh cách hai app render nội dung.

## C05 - Weak Password Storage

**Mục tiêu:** Hiểu vì sao lưu password không an toàn là vấn đề nghiêm trọng.

Gợi ý:

1. Xem admin panel ở vulnerable app.
2. Đọc source code trong `vulnerable-app/app.py`.
3. So sánh với `secure-app/app.py`.
