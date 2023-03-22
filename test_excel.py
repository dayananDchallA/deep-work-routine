import pandas as pd

df = pd.read_excel("test_excel.xlsx", engine="openpyxl")
print(df)