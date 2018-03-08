import numpy as np
import pandas as pd

df = pd.read_csv("../Python-Data-Science-and-Machine-Learning-Bootcamp/Python-For-Data-Analysis/Pandas/example")
print(df)

df.to_csv("../Python-Data-Science-and-Machine-Learning-Bootcamp/Python-For-Data-Analysis/Pandas/MyOutput", index=False)
df_two = pd.read_csv("../Python-Data-Science-and-Machine-Learning-Bootcamp/Python-For-Data-Analysis/Pandas/MyOutput")

# read from excel(can only import data, not formulas etc.)

df = pd.read_excel("../Python-Data-Science-and-Machine-Learning-Bootcamp/Python-For-Data-Analysis/Pandas/Excel_Sample.xlsx", sheet_name="Sheet1")
df.to_excel("../Python-Data-Science-and-Machine-Learning-Bootcamp/Python-For-Data-Analysis/Pandas/Excel_Sample_2.xlsx", sheet_name="newSheet")

# read from html

data = pd.read_html("https://www.fdic.gov/bank/individual/failed/banklist.html")
print(data)
