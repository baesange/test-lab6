# lab6

## Требования
- Python 3.x
- Google Chrome
- Учётная запись GitHub и персональный токен с правами `repo`.

## Установка

### 1. Клонировать репозиторий
```bash
git clone https://github.com/kerls/lab6.git
cd lab6
```

### 2. Создать и активировать виртуальное окружение
```bash
python3 -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows cmd.exe
.venv\Scripts\activate.bat
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

## E2E Test: SauceDemo Purchase

Этот файл содержит автоматизированный E2E-тест для проверки сценария покупки на сайте [saucedemo.com](https://www.saucedemo.com/).

**Запуск теста:**
```bash
python test_purchase.py
```
или через pytest:
```bash
pytest -v test_purchase.py
```

## GitHub API Test

Файл автоматизации теста для проверки работы с GitHub API: создание, проверка и удаление репозитория.

**Переменные окружения:**
Переименуйте файл `.env.example` в `.env` и укажите свои значения.

GITHUB_USER=ваш_логин
GITHUB_TOKEN=ваш_токен
REPO_NAME=имя_тестового_репозитория

**Запуск теста:**
```bash
python test_github.py
```
или через pytest:
```bash
pytest -v test_github.py
```
