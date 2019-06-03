import pandas as pd
metadata = pd.read_csv("movies_metadata.csv", low_memory=False)
metadata = metadata.iloc[0:1000]
metadata = metadata.sample(100)
print(metadata.head(5))
#print(metadata.dtypes)
#print(metadata.loc[:,['imdb_id','title']])
lis1 = metadata.loc[:,['imdb_id','title']]
movlis = lis1.sort_values(by=['title'])
#print(movlis.sort_values(by=['title']))
