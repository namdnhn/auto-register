from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
import string


def generate_random_string(length: int):
    characters = string.ascii_letters + string.digits + "_"
    result = "".join(random.choice(characters) for _ in range(length))
    return result

def generate_random_password(length: int):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


service_obj = Service("E:\Test Selenium\py\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://hoclieu.vn/auth/registration")

wait = WebDriverWait(driver, 5)
element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()= 'ĐĂNG KÝ TÀI KHOẢN']")))


element_regis_button = driver.find_element(
    By.XPATH, "//span[text()='Đăng ký bằng email/Tên đăng nhập']//parent::button[@type='button']"
)
element_regis_button.click()

random_length = random.randint(3, 30)

# auto gen and fill username
username = generate_random_string(random_length)
element_username_input = driver.find_element(
    By.XPATH, '//input[@name="userName"]'
)
element_username_input.send_keys(username)

#auto fill email
email = "21020358@vnu.edu.vn"
element_email_input = driver.find_element(
    By.XPATH, '//input[@name = "email"]'
)
element_email_input.send_keys(email)

#auto fill password
password = generate_random_password(random.randint(8, 30))
element_password_input = driver.find_element(
    By.XPATH, '//input[@id="passwordText"]'
)

element_password_input.send_keys(password)

element_password_input_again = driver.find_element(
    By.XPATH, '//input[@id="passwordAgainText"]'
)

element_password_input_again.send_keys(password)

# agree
element_agree_checkbox = driver.find_element(
    By.XPATH, '//label[@for="agree-text"]'
)
element_agree_checkbox.click()

# button register click
element_button_regis = driver.find_element(
    By.XPATH, "//button[@type='submit' and text()='Đăng ký']"
)
element_button_regis.click()


print("Username:", username)
print("Password:", password)

element = wait.until(ec.presence_of_element_located((By.XPATH, "//img[@alt='banner']")))
driver.find_element(By.XPATH, "//*[name()='svg' and @class='icon-exit']").click()

wait = WebDriverWait(driver, 15)
element_choose_type_account = wait.until(ec.presence_of_element_located((By.XPATH, "//h6[text()='CHỌN LOẠI TÀI KHOẢN']//parent::div")))

element_choose_type_account_student = driver.find_element(
    By.XPATH, "//div[text()='HỌC SINH']//parent::button"
).click()

wait = WebDriverWait(driver, 15)
element_choose_type_account = wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='ĐỊA CHỈ HỌC TẬP']")))

driver.find_element(By.XPATH, "//div[text()='Chọn tỉnh thành']//following::div//child::div//child::input").send_keys("Thành phố Hà Nội")
driver.find_element(By.XPATH, "//div[text()='Thành phố Hà Nội' and @tabindex='-1']").click()

driver.find_element(By.XPATH, "//div[text()='Chọn quận huyện']//following::div//child::div//child::input").send_keys("Quận Thanh Xuân")
driver.find_element(By.XPATH, "//div[text()='Quận Thanh Xuân' and @tabindex='-1']").click()

driver.find_element(By.XPATH, "//div[text()='Chọn trường']//following::div//child::div//child::input").send_keys("Trường THPT chuyên Khoa Học Tự Nhiên")
driver.find_element(By.XPATH, "//div[text()='Trường THPT chuyên Khoa Học Tự Nhiên' and @tabindex='-1']").click()

driver.find_element(By.XPATH, "//div[text()='Chọn khối']//following::div//child::div//child::input").send_keys("Lớp 12")
driver.find_element(By.XPATH, "//div[text()='Lớp 12' and @tabindex='-1']").click()

driver.find_element(By.XPATH, "//button[text()='Tiếp theo']").click()

wait = WebDriverWait(driver, 15)
element_choose_type_account = wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='THÔNG TIN CÁ NHÂN']")))
driver.find_element(By.XPATH, "//input[@name='familyName']").send_keys('Nguyễn')
driver.find_element(By.XPATH, "//input[@name='givenName']").send_keys('Văn A')
driver.find_element(By.XPATH, "//input[@name='phoneNumber']").send_keys('0321654987')
driver.find_element(By.XPATH, "//button[text()='Tiếp theo']").click()

wait = WebDriverWait(driver, 15)
element_choose_type_account = wait.until(ec.presence_of_element_located((By.XPATH, "//div[text()='ĐĂNG KÝ THÀNH CÔNG']")))
driver.find_element(By.XPATH, "//button[text()='Bắt đầu ngay']").click()