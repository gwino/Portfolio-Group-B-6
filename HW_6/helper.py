import pandas as pd
import numpy as np
import math
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

from scipy.stats import norm

def read_excel(file_name: str, index_col: int = 0, print_sheets: bool = False, sheet_name: str = None):
    """
    Reads an Excel file and returns a DataFrame with specified options

    Parameters:
    * file_name (str): The path to the Excel File
    * index_col (int, default = 0): Column to use as the row labels of the DataFrame
    * print_sheets (bool, default = False): If True, prints the names and first few rows of all sheets
    * sheet_name (str or int, default = None): Name or index of the sheet to read. If None, reads the first sheet)

    Returns:
    pd.DataFrame : DataFrame containing the data from the specified excel sheet

    Notes:
    - If 'print_sheets' is True, the function will print the names and first few rows of all sheets and return None
    - The function ensures that the index name is set to 'date'
    """

    if print_sheets:
        n = 0
        while True:
            try:
                sheet = pd.read_excel(file_name, sheet_name = n)
                print(f'Sheet {n}:')
                print(", ".join(list(sheet.columns)))
                print(sheet.head(3))
                n += 1

                print('\n')
            except:
                return

    returns = pd.read_excel(file_name, index_col = index_col, sheet_name = sheet_name)
    if returns.index.name is not None:
        if returns.index.name.lower() in ['date', 'dates']:
            returns.index.name = 'date'
        elif isinstance(returns.index[0], (datetime.date, datetime.datetime)):
            returns.index.name = 'date'
    return returns

def calculate_summary_stats(dataframe: dataFrame)