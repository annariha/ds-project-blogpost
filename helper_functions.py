# functions for data cleaning

import pandas as pd
import numpy as np

def row_to_header(df, index_row: int):
    headers = df.iloc[index_row]
    # first element of header should be empty, remove old index from header row
    headers.name = None
    # define a new df with the correct column names
    new_df = pd.DataFrame(df.values[1:], columns=headers)
    return new_df
