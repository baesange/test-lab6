import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class SauceDemoTester:
    def __init__(self):
        options = Options()
        prefs = {
            "profile.password_manager_leak_detection": False,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def __enter__(self):
        self.driver.maximize_window()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(2)
        self.driver.quit()

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        print("Вход выполнен.")

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id^=add-to-cart]"))).click()
        print("Товар добавлен в корзину.")

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Test")
        self.wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("User")
        self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("12345")
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
        print("Оформление заказа завершено.")

    def verify_success(self):
        completion = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.complete-header"))).text
        assert completion == "Thank you for your order!", f"Ожидалось подтверждение заказа, получено: {completion}"
        print("Покупка успешно завершена!")

def test_purchase_flow():
    with SauceDemoTester() as tester:
        try:
            tester.login("standard_user", "secret_sauce")
            tester.add_to_cart()
            tester.checkout()
            tester.verify_success()
        except Exception as e:
            print(f"Ошибка во время теста: {e}")
            raise

if __name__ == "__main__":
    test_purchase_flow()