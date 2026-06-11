# Remediation Guide - Tiếng Việt

## Nguyên tắc chung

- Không ghép trực tiếp input người dùng vào SQL query.
- Không render dữ liệu người dùng bằng `safe` nếu không có lý do rõ ràng.
- Luôn kiểm tra quyền ở backend.
- Không lưu password plaintext.
- Không dựa vào ID trên URL mà bỏ qua user hiện tại.

## Mapping lỗi và cách fix

| ID | Cách khắc phục |
|---|---|
| VULN-01 | Dùng parameterized query và password hashing |
| VULN-02 | Dùng parameterized query cho search |
| VULN-03 | Escape output khi render |
| VULN-04 | Escape stored user content |
| VULN-05 | Dùng hash như Werkzeug password hashing |
| VULN-06 | Kiểm tra object ownership hoặc role |
| VULN-07 | Enforce role-based authorization |

## CSRF Protection

Với các request thay đổi trạng thái như cập nhật profile, đổi password hoặc chỉnh account settings:

- Yêu cầu CSRF token cho form submission.
- Lưu token phía server hoặc gắn với session của user.
- Từ chối request thiếu token hoặc token không hợp lệ.
- Với ứng dụng thật, nên dùng cơ chế CSRF protection có sẵn từ framework.
