# Write-up: SQL Injection ở chức năng Login

## Tóm tắt

Write-up này giải thích vì sao việc nối chuỗi SQL trực tiếp từ input người dùng là nguy hiểm và parameterized query giúp chặn lỗi này như thế nào.

## Khu vực ảnh hưởng

- Vulnerable app: `http://localhost:5000/login`
- Secure app: `http://localhost:5001/login`

## Hành vi ở bản vulnerable

Route login trong bản vulnerable tạo SQL query bằng cách đưa input người dùng trực tiếp vào chuỗi truy vấn.

Điều này khiến database có thể hiểu một phần input là cú pháp SQL thay vì dữ liệu bình thường.

## Nguyên nhân gốc

Pattern dễ lỗi là:

```text
SQL query = câu SQL cố định + input người dùng thô
```

Pattern an toàn hơn là:

```text
SQL query = câu SQL có placeholder + giá trị được bind riêng
```

## Cách bản secure sửa lỗi

Bản secure dùng parameterized query để tìm user và dùng hàm kiểm tra password hash thay vì so sánh password plaintext.

## Tác động

Trong ứng dụng thật, SQL Injection ở login có thể dẫn đến bypass xác thực, chiếm tài khoản hoặc lộ dữ liệu, tùy quyền của database và cách query được viết.

## Khuyến nghị khắc phục

- Dùng parameterized query cho toàn bộ database access.
- Không nối raw user input trực tiếp vào SQL.
- Lưu password bằng cơ chế hashing phù hợp.
- Thêm behavioral tests cho các pattern login không an toàn.

## Kết quả retest

- Vulnerable app: input không an toàn có thể thay đổi hành vi query trong lab.
- Secure app: cùng input đó được xem là dữ liệu và bị từ chối.
