import pytest

from selenium.webdriver.common.by import By

# тест с test_
def test_product_view_sku(browser):
    """
    Тест-кейс QA-1
    """
    url = "https://test.qa.studio"
    browser.get(url=url)
		# поиск по селектору элемента меню "Горячие товары" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
		# поиск по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    x_path_table = "//*[@id='rz-shop-content']/ul/li[1]/div/div[2]/h2/a"
    element = browser.find_element(By.XPATH, value=x_path_table)
    element.click()
		# поиск по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"