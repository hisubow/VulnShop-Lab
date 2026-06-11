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
| VULN-07 | Thiếu kiểm tra quyền Admin | Broken access control |
| VULN-08 | Thiếu CSRF Protection | Thiếu xác thực ý định request |

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

**VulnShop-Lab** là một nền tảng học bảo mật web chạy bằng Docker, được thiết kế cho người mới học. Project cung cấp hai phiên bản của cùng một web app bán hàng mini:

| Ứng dụng | URL | Mục đích |
|---|---|---|
| Vulnerable App | `http://localhost:5000/guide` | Bản cố tình có lỗ hổng để thực hành local an toàn |
| Secure App | `http://localhost:5001/guide` | Bản đã sửa lỗi để so sánh secure coding |

Workflow học tập:

```text
Run Lab → Explore → Challenge → Collect Evidence → Compare Fix → Generate Report
```

## Tính năng chính

- Docker Compose chạy hai app song song.
- Dùng chung templates và static assets để giảm duplicate code.
- Guided Challenge Mode cho người mới.
- Evidence Checklist để ghi nhận bằng chứng theo kiểu pentest.
- Code Comparison để so sánh implementation sai và implementation đã fix.
- Report Generator sinh báo cáo Markdown từ evidence JSON và có validate field bắt buộc.
- Challenge Scoreboard lưu tiến độ học trong session.
- Docker Compose có network isolation cho hai service.
- Nhiều evidence JSON mẫu cho các nhóm lỗ hổng khác nhau.
- Behavioral tests cho admin access control, SQL injection, XSS reflection, CSRF protection, scoreboard, Docker Compose network isolation và report generator.
- Tài liệu song ngữ tiếng Việt và tiếng Anh.

## Lỗ hổng được mô phỏng

| ID | Lỗ hổng | Ý nghĩa học tập |
|---|---|---|
| VULN-01 | SQL Injection ở Login | Truy vấn SQL không an toàn |
| VULN-02 | SQL Injection ở Search | Xử lý input không an toàn |
| VULN-03 | Reflected XSS / Attribute Injection | Render output sai theo context HTML |
| VULN-04 | Stored XSS | Lưu và hiển thị nội dung user nhập không an toàn |
| VULN-05 | Weak Password Storage | Lưu trữ mật khẩu yếu |
| VULN-06 | IDOR ở Profile Page | Thiếu kiểm tra quyền truy cập object |
| VULN-07 | Thiếu kiểm tra quyền Admin | Broken access control |
| VULN-08 | Thiếu CSRF Protection | Thiếu xác thực ý định request |

> Các lỗi này được tạo có chủ đích để học trong local lab. Không deploy vulnerable app ra Internet.

## Yêu cầu

- Docker Desktop
- Git
- Python 3.10+ nếu muốn chạy tests hoặc report generator ngoài Docker

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
Vulnerable App: http://localhost:5000/guide
Secure App:     http://localhost:5001/guide
```

## Tài khoản demo

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| User | `alice` | `alice123` |
| User | `bob` | `bob123` |

Các tài khoản này được tạo đơn giản vì project chỉ dùng trong local lab.

## Cách học khuyến nghị

1. Mở vulnerable app tại `http://localhost:5000/guide`.
2. Đọc `docs/vi/challenges.md`.
3. Thực hiện từng challenge trên port `5000`.
4. Ghi evidence theo `docs/vi/evidence-checklist.md`.
5. Mở secure app tại `http://localhost:5001/guide`.
6. Thử lại cùng thao tác để so sánh hành vi.
7. Đọc `docs/vi/code-comparison.md` để hiểu nguyên nhân và cách sửa.
8. Sinh báo cáo Markdown từ evidence JSON.

## Report Generator

Sinh report mẫu:

```bash
python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md
```

Các evidence JSON mẫu khác:

```text
examples/evidence-sqli-login.json
examples/evidence-reflected-xss.json
examples/evidence-idor-profile.json
examples/evidence-csrf-settings.json
```

Report generator sẽ kiểm tra các field bắt buộc trước khi tạo file Markdown.

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

## Cấu trúc project

```text
VulnShop-Lab/
├── vulnerable-app/          # Web app có lỗi cố ý
├── secure-app/              # Web app đã sửa lỗi
├── common/                  # Templates và static assets dùng chung
├── docs/
│   ├── en/                  # Tài liệu tiếng Anh
│   └── vi/                  # Tài liệu tiếng Việt
├── examples/                # Evidence JSON mẫu
├── report-generator/        # Tool sinh report Markdown
├── reports/                 # Report mẫu / generated report
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

## Tài liệu

| File | Mục đích |
|---|---|
| `docs/vi/learning-path.md` | Lộ trình học đề xuất |
| `docs/vi/challenges.md` | Challenge thực hành có hướng dẫn |
| `docs/vi/evidence-checklist.md` | Checklist ghi nhận evidence |
| `docs/vi/code-comparison.md` | So sánh code vulnerable và secure |
| `docs/vi/vulnerability-list.md` | Danh sách lỗ hổng |
| `docs/vi/remediation-guide.md` | Hướng dẫn khắc phục |
| `docs/release-notes.md` | Ghi chú phiên bản |

## Sử dụng có đạo đức

Project này chỉ dành cho học tập trong môi trường local hoặc môi trường được cấp quyền.

Không deploy vulnerable app ra Internet.

Không sử dụng project để tấn công hệ thống thật hoặc hệ thống không thuộc quyền kiểm thử của bạn.

---

## License

This project is licensed under the MIT License.
