# VulnShop-Lab Setup Guide

## 1. Requirements

- Docker Desktop installed and running
- Git
- Python 3.10+ if you want to run tests or the report generator outside Docker

## 2. Clone the repository

```bash
git clone https://github.com/hisubow/VulnShop-Lab.git
cd VulnShop-Lab
```

## 3. Create the `.env` file

Windows PowerShell:

```powershell
copy .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

This command is only needed once after cloning or extracting the project.

## 4. Start the lab

```bash
docker compose up --build
```

Open:

```text
http://localhost:5000/guide
http://localhost:5001/guide
```

## 5. Stop the lab

```bash
docker compose down
```

## 6. Start again later

```bash
docker compose up
```
