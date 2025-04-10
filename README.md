# 🔐 Password Manager API

Менеджер паролей с шифрованием, FastAPI и PostgreSQL.

## 🚀 Запуск

1. Склонировать репозиторий
2. Сгенерировать Fernet ключ:
   ```bash
   python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
3. Записать его в .env и docker-compose.yml
4. Запустить сервис:
docker-compose up --build
