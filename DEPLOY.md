# Деплой на VPS (Ubuntu 24)

## Быстрый старт

### 1. Установить Docker на сервере
```bash
ssh root@your_server_ip
apt update && apt install -y docker.io docker-compose
```

### 2. Скопировать проект на сервер
```bash
# Из локального терминала:
scp -r C:/Users/furer/PycharmProjects/DRF-API-SERVER/* user@your_server_ip:/opt/drf-api/
```

### 3. Запустить на сервере
```bash
ssh user@your_server_ip
cd /opt/drf-api
docker-compose up -d --build
```

### 4. Проверить работу
```bash
curl http://localhost:8000/api/users/
curl http://localhost:8000/api/posts/
```

## Управление

| Команда | Описание |
|---------|----------|
| `docker-compose logs -f` | Просмотр логов |
| `docker-compose restart` | Перезапуск |
| `docker-compose down` | Остановка |
| `docker-compose up -d --build` | Пересобрать и запустить |

## API эндпоинты

- `http://your_server_ip:8000/api/users/`
- `http://your_server_ip:8000/api/posts/`

## Требования

- Docker
- Docker Compose

## Структура файлов

```
DRF-API-SERVER/
├── Dockerfile
├── docker-compose.yml
├── .env              # переменные окружения
├── .env.example      # образец
├── requirements.txt
├── manage.py
├── backend/
└── DRF_API_SERVER/
```
