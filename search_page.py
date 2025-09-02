# Autor: Vuk Aleksic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pytest
import random
import string


def open_forbes():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
    driver.maximize_window()
    driver.get('https://forbes.n1info.rs/')
    return driver


def forbes_close(driver, test_num):
    driver.quit()
    print('Uspesan kraj testa', str(test_num))


def forbes_back(driver):
    driver.back()


def check_social_icon(driver, icon_id):
    verify_element_is_displayed(driver, icon_id)
    driver.find_element(By.ID, icon_id).click()
    sleep(2)
    close_window(driver)


def remove_popups(driver):
    remove_forbes_ad(driver)
    address_notification(driver)
    address_qr(driver)


def navigate_to_section(driver, menu_item_id):
    driver.find_element(By.ID, menu_item_id).click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)  # Use WebDriverWait ideally


def assert_forbes_logo(driver):
    if driver.find_element(By.XPATH, "//img[@alt='Chameleon']"):
        print("Logo Forbes je prisutan!")
    else:
        print("Logo je promenjen, uklonjen ili ne postoji na stranici!!!")


def remove_forbes_ad(driver):
    try:
        ad = driver.find_element(By.ID, 'banner-close-btn')
        ad.click()
    except NoSuchElementException:
        print('There is no add on the page')
    finally:
        return driver


def address_notification(driver):
    try:
        notif = driver.find_element(By.ID, 'onesignal-slidedown-cancel-button')
        notif.click()
    except NoSuchElementException:
        print('There is no notifications on the page')
    finally:
        return driver


def address_qr(driver):
    try:
        qr = driver.find_element(By.ID, 'close-qr-menu')
        qr.click()
    except NoSuchElementException:
        print('There is no qr notifications on the page')
    finally:
        return driver

def ca_vesti(driver):
    driver.find_element(By.ID, 'menu-item-19327').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def ca_biznis(driver):
    driver.find_element(By.ID, 'menu-item-1685').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def ca_lifestyle(driver):
    driver.find_element(By.ID, 'menu-item-1698').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def ca_lideri(driver):
    driver.find_element(By.ID, 'menu-item-1703').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def ca_novac(driver):
    driver.find_element(By.ID, 'menu-item-1714').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def ca_inovacije(driver):
    driver.find_element(By.ID, 'menu-item-1724').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def ca_liste(driver):
    driver.find_element(By.ID, 'menu-item-4794').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def ca_events(driver):
    driver.find_element(By.ID, 'menu-item-92520').click()
    assert driver.find_elements(By.XPATH, '//h1')
    sleep(1)


def forbes_scroll_down(driver):
    driver.execute_script("window.scrollTo(0, 1000);")
    sleep(2)


def close_window(driver):
    prva = driver.window_handles[0]
    druga = driver.window_handles[1]
    driver.switch_to.window(druga)
    driver.close()
    driver.switch_to.window(prva)


def search(search_term):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
    driver.maximize_window()
    driver.get('https://forbes.n1info.rs/')
    sleep(1)
    remove_forbes_ad(driver)
    address_qr(driver)
    assert driver.find_element(By.ID, 'searchIcon')
    driver.find_element(By.ID, 'searchIcon').click()
    sleep(2)
    driver.find_element(By.ID, 'searchInput').send_keys(search_term)
    driver.find_element(By.ID, 'searchInput').send_keys(Keys.ENTER)
    sleep(1)
    driver.quit()


def prolaz_kroz_rubriku():
    fr = open_forbes()
    sleep(1)
    remove_popups(fr)
    sections = [
        'menu-item-19327', 'menu-item-1685', 'menu-item-1698', 'menu-item-226780',
        'menu-item-1703', 'menu-item-1714', 'menu-item-1724',
        'menu-item-4794', 'menu-item-92520'
    ]

    for section in sections:
        navigate_to_section(fr, section)
    forbes_close(fr, 1)


def provera_linka_drustvenih_mreza():
    fr = open_forbes()
    sleep(2)
    remove_popups(fr)
    ca_vesti(fr)
    sleep(1)
    fr.find_element(By.CSS_SELECTOR, '.card-wrap:nth-child(1) .font-bold').click()
    sleep(1)
    assert fr.find_elements(By.CSS_SELECTOR, '.text-2xl')
    forbes_scroll_down(fr)
    for icon in ['social-icon-facebook', 'social-icon-viber', 'social-icon-whatsapp', 'social-icon-twitter']:
        check_social_icon(fr, icon)
    verify_element_is_displayed(fr, 'social-icon-copy-link')
    fr.find_element(By.ID, 'social-icon-copy-link').click()
    sleep(2)
    fr.execute_script("window.open('https://www.google.com/');")
    sleep(3)
    fr.switch_to.window(fr.window_handles[1])
    sleep(2)
    fr.find_element(By.ID, 'APjFqb').send_keys(Keys.CONTROL + 'v')
    sleep(2)
    fr.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
    sleep(3)
    forbes_close(fr, 2)


def forbes_scroll_down_more(driver):
    driver.execute_script("window.scrollTo(0, 1500);")
    sleep(2)


def verify_element_is_displayed(driver, id):
    sleep(1)
    assert driver.find_element(By.ID, id).is_displayed()
    return driver


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def email_provera():
    fr = open_forbes()
    sleep(2)
    assert_forbes_logo(fr)
    remove_forbes_ad(fr)
    address_notification(fr)
    address_qr(fr)
    ca_vesti(fr)
    sleep(1)
    fr.find_element(By.CSS_SELECTOR, '.card-wrap:nth-child(1) .font-bold').click()
    sleep(2)
    assert fr.find_elements(By.CSS_SELECTOR, '.text-2xl')
    remove_forbes_ad(fr)
    address_notification(fr)
    forbes_scroll_down_more(fr)
    sleep(3)
    assert fr.find_elements(By.XPATH, "//fieldset[3]/input")
    fr.find_element(By.XPATH, "//fieldset[3]/input").click()
    sleep(2)
    fr.find_element(By.XPATH, "//fieldset[3]/input").send_keys('Vuk')
    sleep(2)
    fr.find_element(By.XPATH, "//fieldset[4]/input")
    fr.find_element(By.XPATH, "//fieldset[4]/input").click()
    sleep(1)
    fr.find_element(By.XPATH, "//fieldset[4]/input").send_keys(str(get_random_string(5)) + '@gmail.com')
    sleep(2)
    fr.find_element(By.XPATH, "//fieldset[5]/div").click()
    sleep(2)
    assert fr.find_elements(By.XPATH, "//div[@id='dv_2']/div/div/div/div/h4/span/strong")
    sleep(1)
    fr.find_element(By.XPATH, "//div[@id='dv_3']/div/div/span/a").click()
    sleep(3)
    forbes_close(fr, 4)
