import os
import time
from datetime import datetime
import pyautogui

import openpyxl
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.excel_class import insert_headers, fill_row, fill_row_with_index, create_workbook, save_excel,close_excel, fill_header,fill_header_by_index

class ProductPage():
    locators = {
        'item_name' : ('CLASS_NAME', 'inventory_item_name'),
        'item_price' : ('CLASS_NAME', 'inventory_item_price'),
        'shopping_cart' : ('CLASS_NAME', 'shopping_cart_badge'),
        'remove' : ('XPATH', '//div[@class="pricebar"]//button[text()="Remove"]'),
        'product_heading' : ('XPATH', '//div[@class="header_secondary_container"]//span[@class="title"]'),
        'inventory_items' : ('CLASS_NAME', 'inventory_item'),
        'addToCart' : ('XPATH', '//div[@class="pricebar"]//button[text()="Add to cart"]'),
        'cart_icon' : ('ID', 'shopping_cart_container'),
        'image' : ('CLASS_NAME', 'inventory_item_img'),
        'cart_header' : ('CLASS_NAME', 'primary_header'),
        'header_section' : ('CLASS_NAME', 'header_secondary_container'),
        'body' : ('TAG_NAME', 'body')
    }
    __item_name = (By.CLASS_NAME, 'inventory_item_name')
    __item_price = (By.CLASS_NAME, 'inventory_item_price')
    __shopping_cart = (By.CLASS_NAME, 'shopping_cart_badge')
    __remove = (By.XPATH, '//div[@class="pricebar"]//button[text()="Remove"]')
    __product_heading = (By.XPATH, '//div[@class="header_secondary_container"]//span[@class="title"]')
    __product = ["Product Name", "Product Price"]
    __cart_icon = (By.ID, 'shopping_cart_container')
    __cart_header = (By.CLASS_NAME, 'primary_header')
    __count = 0
    __image = (By.CLASS_NAME, 'inventory_item_img')
    __inventory_items = (By.CLASS_NAME, 'inventory_item')
    __addToCart = (By.XPATH, '//div[@class="pricebar"]//button[text()="Add to cart"]')
    __workbook = create_workbook()
    __worksheet = __workbook.active
    __header_section = (By.CLASS_NAME, 'header_secondary_container')
    __body = (By.TAG_NAME, 'body')
    insert_headers(__worksheet, __product)


    def __init__(self, driver):
        self.driver = driver
        self.__add_to_cart_buttons = self.driver.find_elements(*self.__addToCart)

    def verify_product_heading(self, expected_text):
        product = self.driver.find_element(*self.__product_heading)
        self.save_screenshot('Product_heading.png')
        if product.text == expected_text:
            print("'Product' heading is visible")
        else:
            print("Product heading is not visible")
        return product.text


    def fill_row(self, index, values):
        fill_row(self.__worksheet, index, values)

    def fill_row_with_index(self,col_index, row_index, values):
        fill_row_with_index(self.__worksheet,col_index, row_index, values)

    def save_to_excel(self, path):
        save_excel(self, self.__workbook, path)

    def close_excel(self):
        close_excel(self.__workbook)

    def get_inventory_items(self):
        return self.driver.find_elements(*self.__inventory_items)
        # return self.inventory_items

    def add_item_to_cart(self, index):
        time.sleep(2)
        button = self.__add_to_cart_buttons[index]
        if button.text == "Add to cart":
            print("Text of button is Add to Cart")
            button.click()
            self.__count = self.__count + 1
        else:
            print("Button text is incorrect")
        return button

    def removeButton(self, index):
        self.remove_buttons = self.driver.find_elements(*self.__remove)
        # self.remove_buttons = self.__remove
        button = self.remove_buttons[index]
        if button.text == "Remove":
            print("Text of button is Remove")

    def get_name(self, item):
        return item.find_element(*self.__item_name).text
    def get_price(self, item):
        return item.find_element(*self.__item_price).text

    def cart_value(self):
        return self.driver.find_element(*self.__shopping_cart).text

    def verify_cart_icon(self):
        cartIcon = self.driver.find_element(*self.__cart_icon)
        self.save_screenshot("cartIcon.png")
        if cartIcon.is_displayed():
            print("Cart Icon is visible on the page.")
        else:
            print("Cart Icon is not visible on the page.")
        return cartIcon

    def match_cart_value(self,cart_value):
        if int(cart_value)==int(self.__count):
            print("Cart value is correct that is: ", cart_value)
        else:
            print("cart value is incorrect")

    def verify_image(self, item):
        image = item.find_element(*self.__image)
        item_name = self.get_name(item)
        if image is None:
            print(f"Image is not visible for item: {item_name}")
        else:
            print(f"Image is visible for item: {item_name}")
        return image

    def verify_name(self, item, item_number):
        item_name = self.get_name(item)
        if item_name is None:
            print(f"Item name is not present product number: {item_number}")
        else:
            print(f"Item name is present product number: {item_number}")
        return item_name

    def verify_price(self, item, item_number):
        item_price = self.get_price(item)
        if item_price is None:
            print(f"Item price is not present in product number: {item_number}")
        else:
            print(f"Item price is present in product number: {item_number}")
        return item_price

    def fill_header(self,index,values):
        fill_header(self.__worksheet, index,values)

    def fill_header_by_index(self,col, row, values):
        fill_header_by_index(self.__worksheet,col, row,values)

    def save_screenshot(self, name):
        time.sleep(2)
        now = datetime.now()
        # file_name = now.strftime("%d%m%Y%H%M%S") + "_" + name
        file_name = name
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f"{file_name}")

