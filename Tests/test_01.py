from openpyxl.reader.excel import load_workbook
from utils.excel_class import get_column_values, get_cell_value, insert_headers
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
import os
import pytest

@pytest.mark.usefixtures("setup")
class Test_webpage:
    os.chdir(os.path.join(os.getcwd(), '..'))
    os.chdir(os.path.join(os.getcwd(), 'Resource'))
    filePath = os.path.join(os.getcwd(), 'users.xlsx')
    workbook = load_workbook(filePath)
    worksheet = workbook['Sheet1']
    username = get_cell_value(worksheet, 'A', 2)
    password = get_cell_value(worksheet, 'B', 2)

    def test_TC_01(self, setup):
        driver, path = setup
        login_page = LoginPage(driver)
        driver.implicitly_wait(2)
        os.chdir(path)
        error = login_page.login('','', 1)
        # error = login_page.login(self.username,self.password, 1)
        assert error is not None, "Logged in with wrong credentials"
