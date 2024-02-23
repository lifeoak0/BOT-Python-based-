import csv
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# 读取日程表csv
def read_schedule(file_path):
    schedule = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            event_time = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            event_name = row[1]
            schedule.append((event_time, event_name))
    return schedule

# 发送提醒邮件
def send_reminder(event_time, event_name, recipient_email):
    message = MIMEText(f"Reminder: {event_name} at {event_time}")
    message["From"] = "your_email@gmail.com"
    message["To"] = recipient_email
    message["Subject"] = f"Reminder: {event_name}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail("your_email@gmail.com", recipient_email, message.as_string())

# 主程序
def main():
    schedule = read_schedule("schedule.csv")
    current_time = datetime.now()

    for event_time, event_name in schedule:
        if current_time < event_time <= current_time + timedelta(hours=1):
            send_reminder(event_time, event_name, "recipient_email@gmail.com")

if __name__ == "__main__":
    main()

