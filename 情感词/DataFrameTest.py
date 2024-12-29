import pandas as pd
x=pd.DataFrame({'a': ['David', 'Tina', 'Lucy', 'Jone', 'Tom'],
             'b': [18, 19, 20, 21, 25],
             'c': ['M', 'F', 'F', 'F', 'M']})
y=pd.DataFrame({'d': ['David', 'Tina', 'Lucy', 'Jone', 'Tom'],
             'b': [18, 19, 20, 21, 25],
             'e': ['M', 'F', 'F', 'F', 'M']})

z=x.append(y)
z.fillna(0, inplace=True)
print(z)
print(z.iloc[0:2])