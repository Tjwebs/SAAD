import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_page_loads(driver):
    driver.get('http://127.0.0.1:5000/')
    assert 'CMS Login' in driver.title
    assert driver.find_element(By.ID, 'email')
    assert driver.find_element(By.ID, 'password')

def test_login_success(driver):
    driver.get('http://127.0.0.1:5000/')
    
    email_input = driver.find_element(By.ID, 'email')
    password_input = driver.find_element(By.ID, 'password')
    
    email_input.send_keys('test@barclays.com')
    password_input.send_keys('password123')
    
    driver.find_element(By.TAG_NAME, 'button').click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains('/dashboard')
    )
    
    assert '/dashboard' in driver.current_url

def test_login_failure(driver):
    driver.get('http://127.0.0.1:5000/')
    
    email_input = driver.find_element(By.ID, 'email')
    password_input = driver.find_element(By.ID, 'password')
    
    email_input.send_keys('test@barclays.com')
    password_input.send_keys('wrongpassword')
    
    driver.find_element(By.TAG_NAME, 'button').click()
    
    time.sleep(1)
    
    error_div = driver.find_element(By.ID, 'error')
    assert error_div.is_displayed()

def test_create_problem_flow(driver):
    
    driver.get('http://127.0.0.1:5000/')
    driver.find_element(By.ID, 'email').send_keys('test@barclays.com')
    driver.find_element(By.ID, 'password').send_keys('password123')
    driver.find_element(By.TAG_NAME, 'button').click()
    
    WebDriverWait(driver, 10).until(EC.url_contains('/dashboard'))
    
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Create Problem')]").click()
    
    WebDriverWait(driver, 10).until(EC.url_contains('/create'))
    
    
    driver.find_element(By.ID, 'title').send_keys('Selenium Test Problem')
    driver.find_element(By.ID, 'desc').send_keys('This problem was created by Selenium')
    
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    
    WebDriverWait(driver, 10).until(EC.url_contains('/dashboard'))
    
    assert 'Selenium Test Problem' in driver.page_source