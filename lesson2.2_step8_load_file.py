# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.

# Напишите скрипт, который будет выполнять следующий сценарий:

# 1. Открыть страницу http://suninjuly.github.io/file_input.html
# 2. Заполнить текстовые поля: имя, фамилия, email
# 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# 4. Нажать кнопку "Submit"

from selenium import webdriver
import time
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os 

  
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

        
    browser.find_element(By.NAME, "firstname").send_keys("Olga")
    browser.find_element(By.NAME, "lastname").send_keys("Rogova")
    browser.find_element(By.NAME, "email").send_keys("o1.ru")

    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'les.txt')           # добавляем к этому пути имя файла 
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
       
    
    
    # ждем загрузки страницы
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
        
    #python lesson2.2_step8_load_file.py