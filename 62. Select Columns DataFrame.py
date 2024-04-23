import pandas as pd

data = {
    'name':['Aniket','Vamshi','Sudhanshu','Harsh'],
    'age':[19,20,21,20],
    'hobby':['football','cricket','cricket','badminton'],
    'score':[95,80,98,90]
}

df = pd.DataFrame(data)
selected_cols = df[['name','score']]
print(selected_cols)
