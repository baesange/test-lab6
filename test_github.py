import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubRepoManager:
    def __init__(self, user, token):
        self.user = user
        self.token = token
        self.api_url = "https://api.github.com"
        self.session = requests.Session()
        self.session.auth = (self.user, self.token)

    def create_repo(self, repo_name, description="Test repo", private=False):
        url = f"{self.api_url}/user/repos"
        payload = {"name": repo_name, "description": description, "private": private}
        resp = self.session.post(url, json=payload)
        if resp.status_code == 201:
            print(f"✅ Репозиторий '{repo_name}' успешно создан.")
        elif resp.status_code == 422 and "already exists" in resp.text:
            print(f"⚠️ Репозиторий '{repo_name}' уже существует.")
        else:
            raise Exception(f"Ошибка создания репозитория: {resp.status_code} {resp.text}")

    def repo_exists(self, repo_name):
        url = f"{self.api_url}/repos/{self.user}/{repo_name}"
        resp = self.session.get(url)
        return resp.status_code == 200

    def delete_repo(self, repo_name):
        url = f"{self.api_url}/repos/{self.user}/{repo_name}"
        resp = self.session.delete(url)
        if resp.status_code == 204:
            print(f"🗑️ Репозиторий '{repo_name}' удалён.")
        elif resp.status_code == 404:
            print(f"⚠️ Репозиторий '{repo_name}' не найден.")
        else:
            raise Exception(f"Ошибка удаления репозитория: {resp.status_code} {resp.text}")

if __name__ == "__main__":
    USER = os.getenv("GITHUB_USER")
    TOKEN = os.getenv("GITHUB_TOKEN")
    REPO = os.getenv("REPO_NAME")

    manager = GitHubRepoManager(USER, TOKEN)
    manager.create_repo(REPO)
    if manager.repo_exists(REPO):
        print("🔍 Репозиторий найден на GitHub.")
    else:
        print("❌ Репозиторий не найден на GitHub.")
    manager.delete_repo(REPO)