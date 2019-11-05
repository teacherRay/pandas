import pandas as pd
df= pd.read_csv('pokemon_data.csv', encoding = "ISO-8859-1")
#xdf= pd.read_excel('pokemon_data.xlsx')
#tdf= pd.read_txt('pokemon_data.txt' delimited = "/t")
#print("Heads", df.head(5))
#print("Tails", xdf.tail(5))
#print (df.columns) #column names
#print(df[['Name','HP']][0:5]) #top five names and HP
#print(df.iloc[1])
#print(df.loc[df['Type 1'] == 'Grass']) #Search for String values
#print(df.loc[df['Attack'] > 45]) #Search for Integer values
#print(df.describe()) #Display mean , min, max, etc stats
print(df.sort_values('Name', ascending = False)) # Print sorted list