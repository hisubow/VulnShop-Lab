FROM python:3.11-slim
WORKDIR /app
COPY secure-app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY common ./common
COPY secure-app/app.py ./app.py
ENV VULNSHOP_COMMON_DIR=/app/common
EXPOSE 5000
CMD ["python", "app.py"]
