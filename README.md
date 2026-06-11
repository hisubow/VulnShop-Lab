# VulnShop-Lab

Languages: [English](#english) | [Tiếng Việt](#tiếng-việt)

![Basic Check](https://github.com/hisubow/VulnShop-Lab/actions/workflows/basic-check.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Lab-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

> Learn web security by exploiting, fixing, collecting evidence, and generating reports in a local Dockerized lab.

---

## English

## What This Does

**VulnShop-Lab** is a Dockerized web security learning platform for beginners. It provides two versions of the same mini shop application:

| Application | URL | Purpose |
|---|---|---|
| Vulnerable App | `http://localhost:5000/guide` | Contains intentional security flaws for safe local practice |
| Secure App | `http://localhost:5001/guide` | Shows fixed implementations for comparison |

The learning workflow is:

```text
Run Lab → Explore → Challenge → Collect Evidence → Compare Fix → Generate Report
```

## Key Features

- Docker Compose setup with vulnerable and secure apps.
- Shared UI templates and static assets to reduce duplicate code.
- Guided Challenge Mode for beginner-friendly practice.
- Evidence checklist for pentest-style documentation.
- Code comparison between insecure and secure implementations.
- Automated Markdown report generator with JSON validation.
- Session-based Challenge Scoreboard for self-study progress tracking.
- Docker Compose network isolation for vulnerable and secure services.
- Sample evidence JSON files for multiple vulnerability types.
- Behavioral tests for admin access control, SQL injection, XSS reflection, CSRF protection, scoreboard behavior, Docker Compose network isolation, and report generation.
- Bilingual documentation in English and Vietnamese.

## Covered Vulnerabilities

| ID | Vulnerability | Learning Concept |
|---|---|---|
| VULN-01 | SQL Injection in Login | Unsafe SQL query construction |
| VULN-02 | SQL Injection in Search | Unsafe input handling |
| VULN-03 | Reflected XSS / Attribute Injection | Unsafe context-specific output rendering |
| VULN-04 | Stored XSS | Unsafe stored user content rendering |
| VULN-05 | Weak Password Storage | Insecure credential handling |
| VULN-06 | IDOR in Profile Page | Missing object-level authorization |
| VULN-07 | Missing Admin Authorization | Broken access control |
| VULN-08 | Missing CSRF Protection | Missing request intent verification |

> These vulnerabilities are intentionally implemented for local educational use only. Do not deploy the vulnerable app to the public Internet.

## Requirements

- Docker Desktop
- Git
- Python 3.10+ if you want to run tests or the report generator outside Docker

## Quick Start

Clone the repository:

```bash
git clone https://github.com/hisubow/VulnShop-Lab.git
cd VulnShop-Lab
```

Create the environment file:

```bash
cp .env.example .env
```

For Windows PowerShell:

```powershell
copy .env.example .env
```

Start the lab:

```bash
docker compose up --build
```

Open the apps:

```text
Vulnerable App: http://localhost:5000/guide
Secure App:     http://localhost:5001/guide
```

## Demo Accounts

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| User | `alice` | `alice123` |
| User | `bob` | `bob123` |

The accounts are intentionally simple because the project is a local learning lab.

## Learning Workflow

1. Open the vulnerable app at `http://localhost:5000/guide`.
2. Read `docs/en/challenges.md`.
3. Complete each challenge on port `5000`.
4. Collect evidence using `docs/en/evidence-checklist.md`.
5. Open the secure app at `http://localhost:5001/guide`.
6. Repeat the same action and compare the behavior.
7. Read `docs/en/code-comparison.md` to understand the fix.
8. Generate a Markdown report from an evidence JSON file.

## Report Generator

Generate a sample report:

```bash
python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md
```

Other sample evidence files:

```text
examples/evidence-sqli-login.json
examples/evidence-reflected-xss.json
examples/evidence-idor-profile.json
examples/evidence-csrf-settings.json
```

The report generator validates required fields before writing the Markdown report.

## Useful Commands

Start the lab:

```bash
docker compose up --build
```

Run in the background:

```bash
docker compose up -d
```

Stop the lab:

```bash
docker compose down
```

Run tests:

```bash
python -m pytest tests/
```

## Project Structure

```text
VulnShop-Lab/
├── vulnerable-app/          # Intentionally vulnerable Flask app
├── secure-app/              # Secure comparison Flask app
├── common/                  # Shared templates and static assets
├── docs/
│   ├── en/                  # English documentation
│   └── vi/                  # Vietnamese documentation
├── examples/                # Evidence JSON examples
├── report-generator/        # Markdown report generator
├── reports/                 # Sample and generated reports
├── tests/                   # Behavioral tests
├── assets/                  # Workflow diagrams
├── .github/workflows/       # GitHub Actions CI
├── docker-compose.yml
├── .env.example
├── Makefile
├── SECURITY.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Documentation

| File | Purpose |
|---|---|
| `docs/en/learning-path.md` | Suggested learning path |
| `docs/en/challenges.md` | Guided hands-on challenges |
| `docs/en/evidence-checklist.md` | Evidence collection checklist |
| `docs/en/code-comparison.md` | Vulnerable vs secure code comparison |
| `docs/en/vulnerability-list.md` | Vulnerability reference |
| `docs/en/remediation-guide.md` | Fixing and prevention guidance |
| `docs/en/writeups/admin-authorization.md` | Complete write-up for admin authorization |
| `docs/en/writeups/sqli-login.md` | Complete write-up for login SQL injection |
| `docs/release-notes.md` | Release notes |

## Ethical Use

This project is intentionally vulnerable and must only be used in local, educational, and authorized environments.

Do not deploy the vulnerable app to the public Internet.

Do not use this project to attack systems you do not own or do not have permission to test.

---

## Tiếng Việt

## Dự án này làm gì?

**VulnShop-Lab** là một nền tảng học bảo mật web chạy bằng Docker, được thiết kế cho người mới bắt đầu. Dự án cung cấp hai phiên bản của cùng một ứng dụng web bán hàng mini:

| Ứng dụng | URL | Mục đích |
|---|---|---|
| Ứng dụng có lỗ hổng | `http://localhost:5000/guide` | Bản cố tình có lỗi bảo mật để thực hành an toàn trên máy cá nhân |
| Ứng dụng đã bảo vệ | `http://localhost:5001/guide` | Bản đã khắc phục lỗi để so sánh cách lập trình an toàn |

Quy trình học tập:

```text
Chạy lab → Khám phá → Làm thử thách → Ghi bằng chứng → So sánh bản sửa lỗi → Sinh báo cáo
```

## Tính năng chính

- Chạy hai ứng dụng song song bằng Docker Compose.
- Dùng chung giao diện và tài nguyên tĩnh để giảm lặp mã nguồn.
- Có chế độ bài thực hành có hướng dẫn cho người mới.
- Có checklist ghi bằng chứng theo phong cách báo cáo pentest.
- Có tài liệu so sánh giữa cách viết mã không an toàn và cách viết mã đã khắc phục.
- Có công cụ sinh báo cáo Markdown từ evidence JSON và kiểm tra các trường bắt buộc.
- Có bảng điểm theo phiên làm việc để người học tự theo dõi tiến độ.
- Có tách biệt mạng trong Docker Compose cho hai dịch vụ.
- Có nhiều file evidence JSON mẫu cho các nhóm lỗ hổng khác nhau.
- Có kiểm thử hành vi cho kiểm soát quyền admin, SQL Injection, XSS phản hồi, CSRF, bảng điểm, tách biệt mạng trong Docker Compose và công cụ sinh báo cáo.
- Có tài liệu song ngữ tiếng Việt và tiếng Anh.

## Lỗ hổng được mô phỏng

| ID | Lỗ hổng | Ý nghĩa học tập |
|---|---|---|
| VULN-01 | Chèn lệnh SQL ở đăng nhập | Tạo truy vấn SQL không an toàn |
| VULN-02 | Chèn lệnh SQL ở tìm kiếm | Xử lý dữ liệu đầu vào không an toàn |
| VULN-03 | XSS phản hồi / chèn thuộc tính HTML | Hiển thị dữ liệu đầu ra sai theo ngữ cảnh HTML |
| VULN-04 | XSS lưu trữ | Lưu và hiển thị nội dung người dùng nhập không an toàn |
| VULN-05 | Lưu trữ mật khẩu yếu | Lưu trữ và xử lý thông tin đăng nhập không an toàn |
| VULN-06 | Truy cập đối tượng trực tiếp không an toàn ở trang hồ sơ | Thiếu kiểm tra quyền truy cập theo từng đối tượng |
| VULN-07 | Thiếu kiểm tra quyền admin | Thiếu kiểm soát truy cập theo vai trò |
| VULN-08 | Thiếu bảo vệ CSRF | Thiếu xác thực ý định của request |

> Các lỗi này được tạo có chủ đích để học trong lab cục bộ. Không triển khai ứng dụng có lỗ hổng lên Internet công khai.

## Yêu cầu

- Docker Desktop
- Git
- Python 3.10+ nếu muốn chạy kiểm thử hoặc công cụ sinh báo cáo bên ngoài Docker

## Cài đặt nhanh

Clone repo:

```bash
git clone https://github.com/hisubow/VulnShop-Lab.git
cd VulnShop-Lab
```

Tạo file môi trường:

```bash
cp .env.example .env
```

Trên Windows PowerShell:

```powershell
copy .env.example .env
```

Chạy lab:

```bash
docker compose up --build
```

Mở trình duyệt:

```text
Ứng dụng có lỗ hổng: http://localhost:5000/guide
Ứng dụng đã bảo vệ:  http://localhost:5001/guide
```

## Tài khoản demo

| Vai trò | Tên đăng nhập | Mật khẩu |
|---|---|---|
| Quản trị viên | `admin` | `admin123` |
| Người dùng | `alice` | `alice123` |
| Người dùng | `bob` | `bob123` |

Các tài khoản này được tạo đơn giản vì dự án chỉ dùng trong lab cục bộ.

## Cách học khuyến nghị

1. Mở ứng dụng có lỗ hổng tại `http://localhost:5000/guide`.
2. Đọc `docs/vi/challenges.md`.
3. Thực hiện từng bài thực hành trên cổng `5000`.
4. Ghi bằng chứng theo `docs/vi/evidence-checklist.md`.
5. Mở ứng dụng đã bảo vệ tại `http://localhost:5001/guide`.
6. Thử lại cùng thao tác để so sánh hành vi.
7. Đọc `docs/vi/code-comparison.md` để hiểu nguyên nhân và cách sửa.
8. Sinh báo cáo Markdown từ file evidence JSON.

## Công cụ sinh báo cáo

Sinh report mẫu:

```bash
python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md
```

Các file evidence JSON mẫu khác:

```text
examples/evidence-sqli-login.json
examples/evidence-reflected-xss.json
examples/evidence-idor-profile.json
examples/evidence-csrf-settings.json
```

Công cụ sinh báo cáo sẽ kiểm tra các trường bắt buộc trước khi tạo file Markdown.

## Lệnh thường dùng

Chạy lab:

```bash
docker compose up --build
```

Chạy nền:

```bash
docker compose up -d
```

Tắt lab:

```bash
docker compose down
```

Chạy kiểm thử:

```bash
python -m pytest tests/
```

## Cấu trúc dự án

```text
VulnShop-Lab/
├── vulnerable-app/          # Ứng dụng cố tình có lỗi bảo mật
├── secure-app/              # Ứng dụng đã khắc phục lỗi
├── common/                  # Giao diện và tài nguyên tĩnh dùng chung
├── docs/
│   ├── en/                  # Tài liệu tiếng Anh
│   └── vi/                  # Tài liệu tiếng Việt
├── examples/                # File evidence JSON mẫu
├── report-generator/        # Công cụ sinh báo cáo Markdown
├── reports/                 # Báo cáo mẫu / báo cáo được tạo ra
├── tests/                   # Kiểm thử hành vi
├── assets/                  # Sơ đồ quy trình
├── .github/workflows/       # Quy trình CI của GitHub Actions
├── docker-compose.yml
├── .env.example
├── Makefile
├── SECURITY.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Tài liệu

| File | Mục đích |
|---|---|
| `docs/vi/learning-path.md` | Lộ trình học đề xuất |
| `docs/vi/challenges.md` | Bài thực hành có hướng dẫn |
| `docs/vi/evidence-checklist.md` | Checklist ghi nhận bằng chứng |
| `docs/vi/code-comparison.md` | So sánh mã nguồn có lỗi và mã nguồn đã sửa |
| `docs/vi/vulnerability-list.md` | Danh sách lỗ hổng |
| `docs/vi/remediation-guide.md` | Hướng dẫn khắc phục |
| `docs/release-notes.md` | Ghi chú phiên bản |

## Sử dụng có đạo đức

Dự án này chỉ dành cho học tập trong môi trường cục bộ hoặc môi trường được cấp quyền.

Không triển khai ứng dụng có lỗ hổng lên Internet công khai.

Không sử dụng dự án để tấn công hệ thống thật hoặc hệ thống không thuộc quyền kiểm thử của bạn.

---

## License

This project is licensed under the MIT License.
