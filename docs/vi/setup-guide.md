# Hướng dẫn setup VulnShop-Lab

## 1. Yêu cầu

- Docker Desktop đã được cài và đang chạy
- Git
- Python 3.10+ nếu muốn chạy test hoặc report generator ngoài Docker

## 2. Clone repo

```bash
git clone https://github.com/hisubow/VulnShop-Lab.git
cd VulnShop-Lab
```

## 3. Tạo file `.env`

Windows PowerShell:

```powershell
copy .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Lệnh này chỉ cần chạy một lần đầu tiên sau khi clone hoặc giải nén project.

## 4. Chạy lab

```bash
docker compose up --build
```

Mở trình duyệt:

```text
http://localhost:5000/guide
http://localhost:5001/guide
```

## 5. Tắt lab

```bash
docker compose down
```

## 6. Chạy lại sau này

```bash
docker compose up
```
