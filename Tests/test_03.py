import os
import pandas as pd
import pytest
from openpyxl.reader.excel import load_workbook

from utils.excel_class import get_column_values,get_cell_value, insert_headers
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage

@pytest.mark.usefixtures("setup")
class Test_webpage:
    os.chdir(os.path.join(os.getcwd(), '..'))
    os.chdir(os.path.join(os.getcwd(), 'Resource'))

    def test_TC_03(self,setup):
        driver, path = setup
        login_page = LoginPage(driver)
        driver.implicitly_wait(2)
        os.chdir(path)
        error = login_page.login('', 'Dummypassword', 3)
        assert error is not None, "Logged in with wrong credentials"