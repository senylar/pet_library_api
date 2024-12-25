#!/usr/bin/env bash

PROJECT_NAME="library_project"

# Создаём корневую папку проекта
mkdir -p "${PROJECT_NAME}"

# В корне
touch "${PROJECT_NAME}/__init__.py"
touch "${PROJECT_NAME}/main.py"

# requirements.txt
touch "${PROJECT_NAME}/requirements.txt"

# Папка api
mkdir -p "${PROJECT_NAME}/api"
touch "${PROJECT_NAME}/api/__init__.py"
touch "${PROJECT_NAME}/api/books.py"
touch "${PROJECT_NAME}/api/readers.py"
touch "${PROJECT_NAME}/api/issues.py"

# Папка core
mkdir -p "${PROJECT_NAME}/core"
touch "${PROJECT_NAME}/core/__init__.py"
touch "${PROJECT_NAME}/core/config.py"

# Папка db
mkdir -p "${PROJECT_NAME}/db"
touch "${PROJECT_NAME}/db/__init__.py"
touch "${PROJECT_NAME}/db/base.py"
touch "${PROJECT_NAME}/db/session.py"
touch "${PROJECT_NAME}/db/models.py"

# Папка models
mkdir -p "${PROJECT_NAME}/models"
touch "${PROJECT_NAME}/models/__init__.py"
touch "${PROJECT_NAME}/models/book.py"
touch "${PROJECT_NAME}/models/reader.py"
touch "${PROJECT_NAME}/models/issue.py"

# Папка services
mkdir -p "${PROJECT_NAME}/services"
touch "${PROJECT_NAME}/services/__init__.py"
touch "${PROJECT_NAME}/services/books_service.py"
touch "${PROJECT_NAME}/services/readers_service.py"
touch "${PROJECT_NAME}/services/issues_service.py"

# Папка tests
mkdir -p "${PROJECT_NAME}/tests"
touch "${PROJECT_NAME}/tests/__init__.py"
touch "${PROJECT_NAME}/tests/test_books.py"
touch "${PROJECT_NAME}/tests/test_readers.py"
touch "${PROJECT_NAME}/tests/test_issues.py"

echo "Структура проекта '${PROJECT_NAME}' создана."