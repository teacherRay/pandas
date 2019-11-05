import pandas as pd
#df= pd.read_xls('pokemon_data.xlsx')
df= pd.read_csv('pokemon_data.csv', encoding = "ISO-8859-1")
print(df.head(10))