# VulnShop-Lab

[Tiếng Việt](#-tiếng-việt) | [English](#-english)

![CI](https://github.com/hisubow/VulnShop-Lab/actions/workflows/basic-check.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Lab-black)
![Security Lab](https://img.shields.io/badge/Security-Learning%20Platform-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> **Learn web security by exploiting, fixing, collecting evidence, and generating reports in a local Dockerized lab.**

---

## 🇻🇳 Tiếng Việt

## Tổng quan

**VulnShop-Lab** là một nền tảng học bảo mật web chạy bằng Docker, được thiết kế cho người mới học Cyber Security. Project cung cấp hai phiên bản của cùng một web app bán hàng mini:

| Ứng dụng | URL | Mục đích |
|---|---|---|
| Vulnerable App | `http://localhost:5000/guide` | Bản cố tình có lỗ hổng để thực hành |
| Secure App | `http://localhost:5001/guide` | Bản đã sửa lỗi để so sánh secure coding |

Điểm chính của project không chỉ là “có lỗi để test”, mà là một workflow học tập rõ ràng:

```text
Run Lab → Explore → Challenge → Collect Evidence → Compare Fix → Generate Report
```

Project phù hợp để:

- Học OWASP-style vulnerabilities ở mức cơ bản.
- Hiểu sự khác nhau giữa code sai và code đã fix.
- Luyện quy trình ghi bằng chứng khi pentest.
- Tạo report Markdown từ evidence JSON.
- Làm portfolio GitHub cho sinh viên Cyber Security.

---

## Tính năng chính

- Docker Compose chạy hai app song song.
- Vulnerable app và secure app tách riêng rõ ràng.
- Guided Challenge Mode cho người mới.
- Evidence Checklist để ghi nhận bằng chứng kiểu pentest.
- Code Comparison để so sánh vulnerable vs secure implementation.
- Report Generator tự động sinh báo cáo Markdown.
- Sample report, sample evidence JSON, tests và GitHub Actions CI.
- Tài liệu song ngữ Việt / Anh, dễ tiếp cận.

---

## Lỗ hổng được mô phỏng

| ID | Lỗ hổng | Ý nghĩa học tập |
|---|---|---|
| VULN-01 | SQL Injection in Login | Truy vấn SQL không an toàn |
| VULN-02 | SQL Injection in Search | Xử lý input không an toàn |
| VULN-03 | Reflected XSS | Render dữ liệu người dùng không an toàn |
| VULN-04 | Stored XSS | Lưu và hiển thị nội dung người dùng nhập không an toàn |
| VULN-05 | Weak Password Storage | Lưu trữ mật khẩu yếu |
| VULN-06 | IDOR in Profile Page | Thiếu kiểm tra quyền truy cập object |
| VULN-07 | Missing Admin Authorization | User thường truy cập được chức năng admin |

> Lưu ý: các lỗi này được tạo có chủ đích để học trong local lab. Không deploy vulnerable app ra Internet.

---

## Cài đặt nhanh

### Yêu cầu

- Docker Desktop
- Git
- Python 3.10+ nếu muốn chạy tests hoặc report generator ngoài Docker

### 1. Clone repo

```bash
git clone https://github.com/hisubow/VulnShop-Lab.git
cd VulnShop-Lab
```

### 2. Tạo file cấu hình môi trường

Linux/macOS:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
copy .env.example .env
```

### 3. Chạy lab

```bash
docker compose up --build
```

### 4. Mở trình duyệt

```text
Vulnerable App: http://localhost:5000/guide
Secure App:     http://localhost:5001/guide
```

---

## Tài khoản demo

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| User | `alice` | `alice123` |
| User | `bob` | `bob123` |

Các tài khoản này chỉ dùng cho môi trường local lab.

---

## Cách học khuyến nghị

1. Mở `http://localhost:5000/guide` để xem hướng dẫn trong vulnerable app.
2. Đọc `docs/vi/challenges.md`.
3. Thực hiện từng challenge trên port `5000`.
4. Ghi evidence theo `docs/vi/evidence-checklist.md`.
5. Mở secure app tại `http://localhost:5001/guide`.
6. Thử lại cùng thao tác để xem bản fix hoạt động thế nào.
7. Đọc `docs/vi/code-comparison.md` để hiểu nguyên nhân và cách sửa.
8. Sinh report bằng report generator.

---

## Report Generator

Ví dụ sinh report từ evidence JSON:

```bash
python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md
```

Kết quả:

```text
reports/generated-admin-auth-report.md
```

---

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

Chạy tests:

```bash
python -m pytest tests/
```

Sinh report mẫu:

```bash
python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md
```

---

## Cấu trúc project

```text
VulnShop-Lab/
├── vulnerable-app/          # Web app có lỗi cố ý
├── secure-app/              # Web app đã sửa lỗi
├── docs/
│   ├── vi/                  # Tài liệu tiếng Việt
│   └── en/                  # English documentation
├── examples/                # Evidence JSON mẫu
├── report-generator/        # Tool sinh report Markdown
├── reports/                 # Report mẫu / generated report
├── tests/                   # Behavioral tests
├── assets/                  # Workflow diagram
├── .github/workflows/       # GitHub Actions CI
├── docker-compose.yml
├── .env.example
├── Makefile
├── SECURITY.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Định vị portfolio

Bạn có thể mô tả project trong CV như sau:

> Built **VulnShop-Lab**, a Dockerized web security learning platform that helps beginners practice OWASP-style vulnerabilities through vulnerable/secure app comparison, guided challenges, evidence collection, code comparison, and automated Markdown report generation.

---

## Ethical Use

Project này chỉ dành cho học tập trong môi trường local hoặc môi trường được cấp quyền. Không sử dụng project để tấn công hệ thống thật hoặc hệ thống không thuộc quyền kiểm thử của bạn.

---

## 🇬🇧 English

## Overview

**VulnShop-Lab** is a Dockerized web security learning platform for beginners. It provides two versions of the same mini shop application:

| Application | URL | Purpose |
|---|---|---|
| Vulnerable App | `http://localhost:5000/guide` | Contains intentional security flaws for learning |
| Secure App | `http://localhost:5001/guide` | Shows fixed implementations for comparison |

The goal is not only to expose vulnerabilities, but to guide learners through a practical workflow:

```text
Run Lab → Explore → Challenge → Collect Evidence → Compare Fix → Generate Report
```

This project is useful for:

- Learning beginner-friendly OWASP-style vulnerabilities.
- Comparing insecure and secure code.
- Practicing evidence collection during pentesting.
- Generating Markdown reports from structured evidence.
- Building a Cyber Security portfolio project.

---

## Key Features

- Docker Compose setup with vulnerable and secure apps.
- Clear separation between insecure and secure implementations.
- Guided Challenge Mode for beginners.
- Evidence checklist for pentest-style documentation.
- Code comparison between vulnerable and secure code.
- Automated Markdown report generator.
- Sample reports, sample evidence JSON files, tests, and GitHub Actions CI.
- Bilingual documentation in Vietnamese and English.

---

## Covered Vulnerabilities

| ID | Vulnerability | Learning Concept |
|---|---|---|
| VULN-01 | SQL Injection in Login | Unsafe SQL query construction |
| VULN-02 | SQL Injection in Search | Unsafe input handling |
| VULN-03 | Reflected XSS | Unsafe output rendering |
| VULN-04 | Stored XSS | Unsafe stored user content rendering |
| VULN-05 | Weak Password Storage | Insecure credential handling |
| VULN-06 | IDOR in Profile Page | Missing object-level authorization |
| VULN-07 | Missing Admin Authorization | Broken access control |

> These vulnerabilities are intentionally implemented for local educational use only. Do not deploy the vulnerable app to the public Internet.

---

## Quick Start

### Requirements

- Docker Desktop
- Git
- Python 3.10+ if you want to run tests or the report generator outside Docker

### 1. Clone the repository

```bash
git clone https://github.com/hisubow/VulnShop-Lab.git
cd VulnShop-Lab
```

### 2. Create the environment file

Linux/macOS:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
copy .env.example .env
```

### 3. Start the lab

```bash
docker compose up --build
```

### 4. Open the apps

```text
Vulnerable App: http://localhost:5000/guide
Secure App:     http://localhost:5001/guide
```

---

## Demo Accounts

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| User | `alice` | `alice123` |
| User | `bob` | `bob123` |

These accounts are intentionally simple because this is a local educational lab.

---

## Recommended Learning Flow

1. Open `http://localhost:5000/guide`.
2. Read `docs/en/challenges.md`.
3. Complete each challenge on the vulnerable app.
4. Record evidence using `docs/en/evidence-checklist.md`.
5. Open the secure app at `http://localhost:5001/guide`.
6. Repeat the same actions and compare behavior.
7. Read `docs/en/code-comparison.md`.
8. Generate a Markdown report using the report generator.

---

## Report Generator

Generate a report from evidence JSON:

```bash
python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md
```

Output:

```text
reports/generated-admin-auth-report.md
```

---

## Common Commands

Start the lab:

```bash
docker compose up --build
```

Run in detached mode:

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

Generate a sample report:

```bash
python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md
```

---

## Ethical Use

This project is designed only for local educational and authorized environments. Do not use this project to attack systems you do not own or do not have explicit permission to test.

---

## License

This project is licensed under the MIT License.
