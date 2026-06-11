# GitHub Upload Guide

## 1. Create a GitHub repository

Repository name:

```text
VulnShop-Lab
```

Description:

```text
A Dockerized web security learning platform for practicing OWASP-style vulnerabilities through vulnerable/secure app comparison, guided challenges, evidence collection, and automated report generation.
```

Topics:

```text
web-security, owasp, flask, docker, cybersecurity, pentest, vulnerable-web-app, secure-coding, security-lab, education
```

## 2. Push from local machine

```bash
git init
git add .
git commit -m "Initial release: VulnShop-Lab v1.0.0"
git branch -M main
git remote add origin https://github.com/hisubow/VulnShop-Lab.git
git push -u origin main
```

## 3. Create a release tag

```bash
git tag v1.0.0
git push origin v1.0.0
```
