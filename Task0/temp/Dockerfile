FROM python:3.9-slim

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép file requirements.txt và cài đặt các gói cần thiết
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn vào container
COPY . .

# Chạy script Python để gửi email
CMD ["python", "send_email.py"]


# build image
#docker build -t send-email .
# run container
#docker run send-email

# Create a Docker network:
# docker network create mailpit-network
# Run Mailpit server on the created network:
# docker run -d --name mailpit --network mailpit-network mailpit/mailpit
# Run your container on the same network:
# docker run --network mailpit-network send-email
