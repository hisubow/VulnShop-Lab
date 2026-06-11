# Write-up: Thiếu kiểm tra quyền Admin

## Tóm tắt

Write-up này giải thích vì sao user thường có thể truy cập trang admin trong bản vulnerable và bản secure đã chặn hành vi đó như thế nào.

## Khu vực ảnh hưởng

- Vulnerable app: `http://localhost:5000/admin`
- Secure app: `http://localhost:5001/admin`
- Role dùng để kiểm thử: `alice` / `user`

## Hành vi ở bản vulnerable

Trong bản vulnerable, route `/admin` chỉ kiểm tra user đã đăng nhập hay chưa. Nó không kiểm tra user đó có role `admin` hay không.

Hành vi an toàn mong đợi:

```text
User thường không được truy cập chức năng chỉ dành cho admin.
```

Hành vi vulnerable quan sát được:

```text
User thường vẫn mở được trang admin sau khi đăng nhập.
```

## Nguyên nhân gốc

Bản vulnerable có authentication nhưng thiếu authorization. Nói cách khác, app chỉ hỏi:

```text
User đã đăng nhập chưa?
```

nhưng không hỏi:

```text
User này có được phép truy cập chức năng admin không?
```

## Cách bản secure sửa lỗi

Bản secure kiểm tra role trong session trước khi render trang admin. Nếu user không phải admin, app trả về `403 Forbidden`.

## Tác động

Nếu lỗi này tồn tại trong ứng dụng thật, user thường có thể xem hoặc thao tác dữ liệu quản trị. Đây là lỗi Broken Access Control.

## Khuyến nghị khắc phục

- Kiểm tra quyền ở phía server cho các route nhạy cảm.
- Không chỉ dựa vào việc ẩn nút hoặc link trên giao diện.
- Viết test để đảm bảo user thường nhận `403 Forbidden` khi truy cập endpoint admin.

## Kết quả retest

- Vulnerable app: user thường truy cập được `/admin`.
- Secure app: user thường bị chặn với `403 Forbidden`.
