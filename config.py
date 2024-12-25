import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

db_path = os.getenv('db_path')
print(db_path)