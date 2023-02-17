import pandas as pd

df = pd.read_csv("./files/TopSellingAlbums.csv")
df.head() #First five rows

df[['Artist','Length','Genre']] # Show columns

# iloc: row(s), col(s)
df.iloc[1,0] # Access the value on the second row and the first column
print(df.iloc[0::2, 0:3])

print(df.loc[:, 'Artist':'Released']) # Using column's name instead of index