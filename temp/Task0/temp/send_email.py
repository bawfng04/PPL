import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Cấu hình Mailpit server
SMTP_SERVER = "mailpit"
SMTP_PORT = 1025
SENDER_EMAIL = "test@example.com"
RECIPIENT_EMAIL = "recipient@example.com"

# Nội dung email
subject = "Test Email"
body = "This is a test email sent from Python using Mailpit."

# Tạo email
message = MIMEMultipart()
message["From"] = SENDER_EMAIL
message["To"] = RECIPIENT_EMAIL
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Gửi email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
