import datetime
import os
import pandas as pd
import openpyxl
def create_workbook():
    workbook = openpyxl.Workbook()
    return workbook

#values should be a list
def insert_headers(worksheet, values):
    for i, value in enumerate(values):
        letter = chr(ord('A')+i)
        worksheet[f"{letter}1"] = value

def fill_header(worksheet,row_index,values):
    for i, value in enumerate(values):
        letter = chr(ord('A')+i)
        worksheet[f'{letter}{row_index}'] = value

def fill_header_by_index(worksheet, column_index, row_index, values):
    for i, value in enumerate(values):
        letter = chr(ord(column_index)+i)
        worksheet[f'{letter}{row_index}'] = value


# values should be a list
# it will fill the row with giving values[name, price, quantity, texture etc..]
def fill_row(worksheet, row_index, values):
    # here values are list[], it will fill the list in single row only
    # A1 B1 C1 D1 ...
    for i, value in enumerate(values):
        letter = chr(ord('A')+i)
        worksheet[f'{letter}{row_index}'] = value


def fill_cell(worksheet, value, row_index, col_index):
    worksheet[f'{col_index}{row_index}'] = value

def save_excel(self, workbook, path):
    # now = datetime.datetime.now()
    # timestamp = now.strftime("%S%H%d%m%Y")
    # timestamp = now.strftime("%d-%m-%Y %I-%M %p")

    # os.chdir(os.path.join(os.getcwd(), '..'))
    # os.chdir(os.path.join(os.getcwd(), 'Resource'))
    os.chdir(path)
    path = os.path.join(os.getcwd(), "product.xlsx")
    workbook.save(path)
def close_excel(workbook):
    workbook.close()

# it will fill the row with giving values[name, price, quantity, texture etc..] with particular starting value of row and col
# method overloading of above fill value function
def fill_row_with_index(worksheet, starting_col_index, starting_row_index, values):
    for i, value in enumerate(values):
        letter = chr(ord(starting_col_index)+i)
        worksheet[f'{letter}{starting_row_index}'] = value

def get_row_count(worksheet):
    return worksheet.max_row

def get_cell_value(worksheet, col_value, row_value):
    return worksheet[f"{col_value}{row_value}"].value
def get_column_values(worksheet, column_name):
    values = worksheet[column_name]
    list = []
    for x in values:
        list.append(x.value)
    return list









