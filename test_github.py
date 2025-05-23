import os
import requests
import time
from dotenv import load_dotenv
# Загружаем переменные окружения из .env
load_dotenv()

GITHUB_API = "https://api.github.com"
USER = os.getenv("GITHUB_USER")
TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("REPO_NAME")


def test_create_repo():
    load_dotenv()

    GITHUB_API = "https://api.github.com"
    USER = os.getenv("GITHUB_USER")
    TOKEN = os.getenv("GITHUB_TOKEN")
    REPO = os.getenv("REPO_NAME")

    url = f"{GITHUB_API}/user/repos"
    payload = {"name": REPO, "description": "Test repo", "private": False}
    resp = requests.post(url, json=payload, auth=(USER, TOKEN))
    # Обработка возможной ошибки: репозиторий уже существует
    if resp.status_code == 201:
        print("✅ Репозиторий создан.")
    elif resp.status_code == 422 and 'already exists' in resp.text:
        print("ℹ️ Репозиторий уже существует.")
    else:
        raise Exception(f"Не удалось создать репозиторий: {resp.status_code} {resp.text}")
    time.sleep(10)

def test_list_repos():
    load_dotenv()

    GITHUB_API = "https://api.github.com"
    USER = os.getenv("GITHUB_USER")
    TOKEN = os.getenv("GITHUB_TOKEN")
    REPO = os.getenv("REPO_NAME")


    url = f"{GITHUB_API}/user/repos"
    resp = requests.get(url, auth=(USER, TOKEN))
    assert resp.status_code == 200, f"Не удалось получить список: {resp.text}"
    names = [r["name"] for r in resp.json()]
    assert REPO in names, "Репозиторий не найден в списке"
    print("✅ Репозиторий найден в списке.")


def test_delete_repo():
    load_dotenv()

    GITHUB_API = "https://api.github.com"
    USER = os.getenv("GITHUB_USER")
    TOKEN = os.getenv("GITHUB_TOKEN")
    REPO = os.getenv("REPO_NAME")

    url = f"{GITHUB_API}/repos/{USER}/{REPO}"
    resp = requests.delete(url, auth=(USER, TOKEN))
    assert resp.status_code == 204, f"Не удалось удалить репозиторий: {resp.text}"
    print("✅ Репозиторий удален.")


if __name__ == "__main__":
    test_create_repo()
    test_list_repos()
    test_delete_repo()