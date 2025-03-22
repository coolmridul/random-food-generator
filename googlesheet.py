import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import datetime
import json
import streamlit as st

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds_dict = json.loads(st.secrets["google"]["creds"])

creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

client = gspread.authorize(creds)

sheet_id = "1_zPrH5E1fAlk_Q9jf6-U4vid7fQigxK7LOinL2CAUlo"
spreadsheet = client.open_by_key(sheet_id)


def get_data_from_google_sheet(name):
    worksheet = spreadsheet.worksheet(name)
    table_data = worksheet.get_all_values()

    df = pd.DataFrame(table_data[1:], columns=table_data[0])  # Skip header row for data

    return df['Name'].to_list()

def push_data_to_google_sheet(name,data):
    worksheet = spreadsheet.worksheet(name)

    worksheet.append_row(data)

    return 'True'


# def modify_data_google_sheet_based_on_df(name,data,is_done_value,date_value):
#     worksheet = spreadsheet.worksheet(name)
#     for i in range(0,data.shape[0]):
#         worksheet.update_cell(data['ID'].astype(int).iloc[i]+2, is_done_value, value="1")
#         worksheet.update_cell(data['ID'].astype(int).iloc[i]+2, date_value, value=datetime.datetime.now().strftime("%d/%m/%Y"))
    
#     return 'True'

# if new_worksheet_name in worksheet_list:
#     sheet = workbook.worksheet(new_worksheet_name)
# else:
#     sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)

# sheet.clear()

# sheet.update(f"A1:C{len(values)}", values)

# sheet.update_cell(len(values) + 1, 2, "=sum(B2:B4)")
# sheet.update_cell(len(values) + 1, 3, "=sum(C2:C4)")

# sheet.format("A1:C1", {"textFormat": {"bold": True}})