# Исторические Даты 🏛️

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.0-brightgreen.svg)](https://djangoproject.com)
[![Pylint](https://github.com/podobry-m/history-dates/actions/workflows/pylint.yml/badge.svg)](https://github.com/podobry-m/history-dates/actions)

Проект для изучения исторических дат через интерактивные тесты. Включает систему добавления событий и два вида тестов.

## 🌟 Особенности

- 📅 Добавление исторических событий
- ✏️ Два режима тестирования:
  - Угадай год по событию
  - Хронологическая последовательность
- 🔍 Поиск по событиям
- ✅ Автоматическая проверка кода (Pylint + GitHub Actions)

## 🛠 Технологии

- Python 3.9+
- Django 4.0+
- Bootstrap 5
- Pylint + pylint-django

## 🚀 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/podobry-m/history-dates.git
cd history-dates
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Настройте базу данных:
```bash
python manage.py migrate
```
4. Импортируйте события из файла:
```
python manage.py import_from_txt events.txt
```
5. Запустите сервер:
```bash
python manage.py runserver
```