FROM python:3.11-slim

# نصب کتابخانه‌های گرافیکی و سیستمی لینوکس که فلت شدیداً به آن‌ها نیاز دارد
RUN apt-get update && apt-get install -y \
    python3-pip \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# باز کردن پورت استاندارد هاگینگ فیس
EXPOSE 7860

# دستور نهایی برای اجرای برنامه وب فلت
CMD ["python", "AbdulHabib.py"]
