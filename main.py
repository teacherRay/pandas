import pandas as pd
df= pd.read_csv('pokemon_data.csv', encoding = "ISO-8859-1")
#xdf= pd.read_excel('pokemon_data.xlsx')
#tdf= pd.read_txt('pokemon_data.txt' delimited = "/t")
#print("Heads", df.head(5))
#print("Tails", xdf.tail(5))
print (df.columns) #column names
print(df[['Name','HP']][0:5]) #top five names and HP