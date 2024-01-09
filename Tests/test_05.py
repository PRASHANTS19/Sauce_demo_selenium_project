import os
import pandas as pd
import pytest
from openpyxl.reader.excel import load_workbook

from utils.excel_class import get_column_values,get_cell_value, insert_headers
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage

@pytest.mark.usefixtures("setup")
class Test_webpage:
    # read username and password from Excel
    os.chdir(os.path.join(os.getcwd(), '..'))
    os.chdir(os.path.join(os.getcwd(), 'Resource'))
    filePath = os.path.join(os.getcwd(), 'users.xlsx')
    workbook = load_workbook(filePath)
    worksheet = workbook['Sheet1']
    username = get_cell_value(worksheet, 'A', 2)
    password = get_cell_value(worksheet, 'B', 2)

    def test_TC_05(self,setup):
        driver, path = setup
        os.chdir(path)
        login_page = LoginPage(driver)
        login_page.login(self.username, self.password, 5)

    def test_TC_06(self, setup):
        driver, path = setup
        os.chdir(path)
        login_page = LoginPage(driver)
        login_page.login(self.username, self.password, 6)
        products_page = ProductPage(driver)
        heading = products_page.verify_product_heading('Products')
        assert heading is not None, "'Product' Heading is not present"

    def test_TC_07(self, setup):
        driver, path = setup
        os.chdir(path)
        login_page = LoginPage(driver)
        login_page.login(self.username, self.password, 7)
        products_page = ProductPage(driver)
        cartIcon = products_page.verify_cart_icon()
        assert cartIcon is not None, "Cart icon is not present"

    def test_TC_08(self, setup):
        driver, path = setup
        os.chdir(path)
        login_page = LoginPage(driver)
        login_page.login(self.username, self.password, 8)
        products_page = ProductPage(driver)
        inventory_items = products_page.get_inventory_items()

        for item_number, item in enumerate(inventory_items, start=1):
            image = products_page.verify_image(item)
            assert image is not None, f"Image is not present in item number: {item_number}"

    def test_TC_09(self, setup):
        driver, path = setup
        login_page = LoginPage(driver)
        os.chdir(path)
        login_page.login(self.username, self.password, 9)
        products_page = ProductPage(driver)
        inventory_items = products_page.get_inventory_items()

        for item_number, item in enumerate(inventory_items, start=1):
            item_name = products_page.verify_name(item, item_number)
            assert item_name is not None, f"Item_name is not present in item number: {item_number}"

    def test_TC_10(self, setup):
        driver, path = setup
        os.chdir(path)
        login_page = LoginPage(driver)
        login_page.login(self.username, self.password, 10)
        products_page = ProductPage(driver)
        inventory_items = products_page.get_inventory_items()

        for item_number, item in enumerate(inventory_items, start=1):
            item_price = products_page.verify_price(item, item_number)
            assert item_price is not None, f"Item_price is not present in item number: {item_number}"

    def test_TC_11(self, setup):
        driver, path = setup
        login_page = LoginPage(driver)
        login_page.login(self.username, self.password, 11)
        products_page = ProductPage(driver)
        # get product list
        inventory_items = products_page.get_inventory_items()

        row = 2
        col = 'A'
        __product = ["Product Name", "Product Price"]
        # products_page.fill_header(1,__product)
        products_page.fill_header_by_index(col, row - 1, __product)
        for index, item in enumerate(inventory_items, start=2):
            # get item name and price
            item_name = products_page.get_name(item)
            item_price = products_page.get_price(item)

            product = [item_name, item_price]
            # fill value in excel
            # products_page.fill_row(index, product)

            products_page.fill_row_with_index(col, row, product)
            row = row + 1

            # verify text and click Add to cart button
            add_to_cart = products_page.add_item_to_cart(index - 2)

            assert add_to_cart is not None, "Add to cart button not found"

            driver.implicitly_wait(2)

            # verify remove button text
            products_page.removeButton(index - 2)

            # Fetch cart value
            cart_count = products_page.cart_value()

            # match cart value
            products_page.match_cart_value(cart_count)

            print("------------------")
        products_page.save_to_excel(path)
        products_page.close_excel()
        driver.quit()
