import os
from datetime import datetime

from openpyxl import load_workbook
from utils.excel_class import  get_column_values, get_cell_value, get_row_count



os.chdir(os.path.join(os.getcwd(), '..'))
os.chdir(os.path.join(os.getcwd(), 'Resource'))
filePath = os.path.join(os.getcwd(), 'users.xlsx')
workbook = load_workbook(filePath)
worksheet = workbook['Sheet1']
username = get_cell_value(worksheet, 'A', 2)
password = get_cell_value(worksheet, 'B', 2)
col = get_column_values(worksheet, 'A')
# print(get_row_count(worksheet))
# print(username, " ", password)

now = datetime.now()
# file_name =  now.strftime("%d%m%Y%S%M%H")+f"{name}"
file_name = now.strftime("%d%m%Y%H%M%S") + "_" + "login1"

locators = {
        '__item_name' : ('CLASS_NAME', 'inventory_item_name'),
        '__item_price' : ('CLASS_NAME', 'inventory_item_price'),
        '__shopping_cart' : ('CLASS_NAME', 'shopping_cart_badge')}

print()