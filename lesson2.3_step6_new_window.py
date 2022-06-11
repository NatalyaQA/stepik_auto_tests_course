# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

# Сценарий для реализации выглядит так:

# 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
# 2. Нажать на кнопку
# 3. Переключиться на новую вкладку
# 4. Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #browser.find_element_by_xpath('//*[@type="submit"]').click()
    browser.find_element(By.XPATH, '//*[@type="submit"]').click()
    #button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print("x element: ", x)
    print("result : ", y)
    
    browser.find_element(By.ID, "answer").send_keys(y)
    time.sleep(1)
    
    browser.find_element(By.XPATH, '//*[@type="submit"]').click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта    
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
        
    #python lesson2.3_step6_new_window.py