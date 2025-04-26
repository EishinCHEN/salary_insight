# 選用官方輕量Python版本
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製專案檔案進去
COPY . .

# 安裝套件
RUN pip install --no-cache-dir -r requirements.txt

# 開放Port（Flask預設5000）
EXPOSE 5000

# 設定啟動指令
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]