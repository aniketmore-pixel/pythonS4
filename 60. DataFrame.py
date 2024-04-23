import pandas as pd

data = {
    'name':['Aniket','Vamshi','Sudhanshu','Harsh'],
    'age':[19,20,21,20],
    'hobby':['football','cricket','cricket','badminton']
}

df = pd.DataFrame(data)
print(df)
