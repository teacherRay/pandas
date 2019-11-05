import pandas as pd
df= pd.read_csv('pokemon_data.csv', encoding = "ISO-8859-1")
print("Heads", df.head(5))
print("Tails", df.tail(5))